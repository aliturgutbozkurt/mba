// AI-Driven MBA Interactive Portal Logic (Root & Subpath Adaptive)
document.addEventListener('DOMContentLoaded', () => {
    let currentLang = 'tr';
    let currentLessonId = 1;
    let searchQuery = '';

    const data = window.MBA_DATA;
    if (!data) {
        console.error('MBA_DATA not loaded!');
        return;
    }

    // Adapt paths based on whether running at root or subpath /web/ or /docs/
    const isSubfolder = window.location.pathname.includes('/web/') || window.location.pathname.includes('/docs/');
    const basePath = isSubfolder ? '../' : '';

    const sidebarNav = document.getElementById('sidebar-nav');
    const lessonContainer = document.getElementById('lesson-content');
    const searchInput = document.getElementById('search-input');
    const langBtns = document.querySelectorAll('.lang-btn');
    const masterPdfBtn = document.getElementById('btn-master-pdf');

    // Language Toggle
    langBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            langBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentLang = btn.dataset.lang;
            updateMasterPdfLink();
            renderSidebar();
            renderLesson(currentLessonId);
        });
    });

    // Search Input
    searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value.toLowerCase().trim();
        renderSidebar();
        if (searchQuery) {
            const matched = data.lessons.find(l => {
                const title = (currentLang === 'tr' ? l.title_tr : l.title_en).toLowerCase();
                const summary = (currentLang === 'tr' ? l.summary_tr : l.summary_en).toLowerCase();
                return title.includes(searchQuery) || summary.includes(searchQuery);
            });
            if (matched) {
                currentLessonId = matched.id;
                renderLesson(matched.id);
            }
        }
    });

    function updateMasterPdfLink() {
        if (masterPdfBtn) {
            const langUpper = currentLang.toUpperCase();
            masterPdfBtn.href = `${basePath}books/${currentLang}/AI_Driven_MBA_Master_${langUpper}.pdf`;
            masterPdfBtn.innerHTML = `<span>📥</span> ${currentLang === 'tr' ? 'Tam Kitap PDF İndir' : 'Download Master PDF'}`;
        }
    }

    function renderSidebar() {
        sidebarNav.innerHTML = '';

        for (let partNum = 1; partNum <= 8; partNum++) {
            const partMeta = data.parts[partNum];
            const partTitle = currentLang === 'tr' ? partMeta.title_tr : partMeta.title_en;
            
            const partLessons = data.lessons.filter(l => {
                if (l.part_num !== partNum) return false;
                if (!searchQuery) return true;
                const title = (currentLang === 'tr' ? l.title_tr : l.title_en).toLowerCase();
                const summary = (currentLang === 'tr' ? l.summary_tr : l.summary_en).toLowerCase();
                return title.includes(searchQuery) || summary.includes(searchQuery);
            });

            if (partLessons.length === 0) continue;

            const groupEl = document.createElement('div');
            groupEl.className = 'part-group';

            const headerEl = document.createElement('div');
            headerEl.className = `part-header ${partLessons.some(l => l.id === currentLessonId) ? 'active' : ''}`;
            headerEl.innerHTML = `
                <span>${partTitle.split(':')[0]}</span>
                <span style="font-size: 0.75rem; color: #64748b;">${partLessons.length} Ders</span>
            `;
            groupEl.appendChild(headerEl);

            const listEl = document.createElement('div');
            listEl.className = 'lesson-list';

            partLessons.forEach(lesson => {
                const title = currentLang === 'tr' ? lesson.title_tr : lesson.title_en;
                const shortTitle = title.includes(':') ? title.split(':')[1].trim() : title;

                const itemEl = document.createElement('a');
                itemEl.className = `lesson-nav-item ${lesson.id === currentLessonId ? 'active' : ''}`;
                itemEl.href = `#lesson-${lesson.id}`;
                itemEl.innerHTML = `
                    <span class="lesson-badge-num">#${String(lesson.lesson_num).padStart(2, '0')}</span>
                    <span style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${shortTitle}</span>
                `;
                itemEl.addEventListener('click', (e) => {
                    e.preventDefault();
                    currentLessonId = lesson.id;
                    renderSidebar();
                    renderLesson(lesson.id);
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                });
                listEl.appendChild(itemEl);
            });

            groupEl.appendChild(listEl);
            sidebarNav.appendChild(groupEl);
        }
    }

    function renderLesson(lessonId) {
        const lesson = data.lessons.find(l => l.id === lessonId);
        if (!lesson) return;

        const isTr = (currentLang === 'tr');
        const title = isTr ? lesson.title_tr : lesson.title_en;
        const partTitle = isTr ? lesson.part_title_tr : lesson.part_title_en;
        const level = isTr ? lesson.level_tr : lesson.level_en;
        const summary = isTr ? lesson.summary_tr : lesson.summary_en;
        const eli5 = isTr ? lesson.eli5_metaphor_tr : lesson.eli5_metaphor_en;
        const steps = isTr ? lesson.framework_steps_tr : lesson.framework_steps_en;
        const caseStudy = isTr ? lesson.case_study_tr : lesson.case_study_en;
        const notebooklm = isTr ? lesson.notebooklm_prompts_tr : lesson.notebooklm_prompts_en;
        const udemy = isTr ? lesson.udemy_outline_tr : lesson.udemy_outline_en;

        // Clean slug for PDF download
        const slugRaw = isTr ? lesson.title_tr : lesson.title_en;
        const slug = slugRaw.includes(':') ? slugRaw.split(':')[1] : slugRaw;
        const cleanSlug = slug.replace(/[^a-zA-Z0-9_]/g, '_').replace(/_+/g, '_').substring(0, 40).replace(/^_+|_+$/g, '');
        const prefix = isTr ? `Ders_${String(lesson.lesson_num).padStart(2, '0')}` : `Lesson_${String(lesson.lesson_num).padStart(2, '0')}`;
        const pdfFilename = `${prefix}_${cleanSlug}.pdf`;
        const pdfUrl = `${basePath}books/${currentLang}/individual-pdfs/${pdfFilename}`;

        // Table Rows
        let tableRows = '';
        lesson.comparison_table.forEach(row => {
            const tTopic = isTr ? row.topic_tr : row.topic_en;
            const tOld = isTr ? row.old_way_tr : row.old_way_en;
            const tAi = isTr ? row.ai_way_tr : row.ai_way_en;
            tableRows += `
                <tr>
                    <td style="font-weight: 600; color: #fff;">${tTopic}</td>
                    <td style="color: #94a3b8;">${tOld}</td>
                    <td style="color: #67e8f9;">${tAi}</td>
                </tr>
            `;
        });

        // Steps
        const stepsLi = steps.map(s => `<li>${s}</li>`).join('');

        // Prompts
        let promptsHtml = '';
        lesson.ai_prompts.forEach((p, idx) => {
            const pTitle = isTr ? p.title_tr : p.title_en;
            const pText = isTr ? p.prompt_tr : p.prompt_en;
            const promptId = `prompt-${lesson.id}-${idx}`;
            promptsHtml += `
                <div class="prompt-container">
                    <div class="prompt-header">
                        <span class="prompt-name">🛠️ ${pTitle}</span>
                        <button class="copy-btn" onclick="navigator.clipboard.writeText(document.getElementById('${promptId}').innerText); this.innerText='Kopyalandı!'; setTimeout(()=>this.innerText='Kopyala', 2000);">
                            📋 Kopyala
                        </button>
                    </div>
                    <div class="prompt-code" id="${promptId}">${pText}</div>
                </div>
            `;
        });

        // Udemy outline
        const udemyLi = udemy.map(u => `<li>${u}</li>`).join('');

        lessonContainer.innerHTML = `
            <div class="lesson-card">
                <div class="lesson-meta-bar">
                    <span class="lesson-part-badge">${partTitle}</span>
                    <div class="lesson-actions">
                        <a href="${pdfUrl}" target="_blank" class="action-btn primary" title="Download Lesson PDF">
                            <span>📄</span> PDF İndir
                        </a>
                        <button class="action-btn" onclick="navigator.clipboard.writeText(document.getElementById('nb-script-${lesson.id}').innerText); this.innerHTML='<span>✅</span> Kopyalandı!'; setTimeout(()=>this.innerHTML='<span>🎙️</span> NotebookLM Komutu', 2000);">
                            <span>🎙️</span> NotebookLM Komutu
                        </button>
                    </div>
                </div>

                <h2 class="lesson-title">${title}</h2>
                <div class="level-tag">🎯 ${level}</div>

                <!-- Section: Executive Summary -->
                <div class="section-block">
                    <div class="section-label">${isTr ? '📌 Kısa Özet & Zihniyet Dönüşümü' : '📌 Executive Summary & Mindset Shift'}</div>
                    <div class="summary-card">${summary}</div>
                </div>

                <!-- Section: ELI5 -->
                <div class="section-block">
                    <div class="section-label">${isTr ? '💡 Aptala Anlatır Gibi (ELI5) & Eğlenceli Hikaye' : '💡 ELI5 Metaphor & Intuitive Story'}</div>
                    <div class="eli5-card">"${eli5}"</div>
                </div>

                <!-- Section: Comparison -->
                <div class="section-block">
                    <div class="section-label">${isTr ? '⚖️ Eski Usul vs. AI Destekli Yaklaşım' : '⚖️ The Legacy Way vs. The AI-Driven Way'}</div>
                    <div class="table-responsive">
                        <table class="comp-table">
                            <thead>
                                <tr>
                                    <th style="width: 25%;">${isTr ? 'Boyut / Konu' : 'Dimension'}</th>
                                    <th style="width: 37.5%;">${isTr ? 'Eski Usul (Legacy)' : 'The Legacy Way'}</th>
                                    <th style="width: 37.5%;">${isTr ? 'AI Destekli Modern Yaklaşım' : 'The AI-Driven Way'}</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${tableRows}
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Section: Actionable Framework -->
                <div class="section-block">
                    <div class="section-label">${isTr ? '🚀 Adım Adım Eylem Çerçevesi (Actionable Framework)' : '🚀 Step-by-Step Actionable Framework'}</div>
                    <div class="framework-list">
                        <ul>${stepsLi}</ul>
                    </div>
                </div>

                <!-- Section: Case Study -->
                <div class="section-block">
                    <div class="section-label">${isTr ? '🚨 Gerçek Hayat Vaka / Kriz Analizi (War Story)' : '🚨 Real-World War Story / Case Study'}</div>
                    <div class="case-card">${caseStudy}</div>
                </div>

                <!-- Section: Prompts -->
                <div class="section-block">
                    <div class="section-label">${isTr ? '🤖 Kullanıma Hazır AI Promptları & Şablonlar' : '🤖 Battle-Tested AI Prompts & Templates'}</div>
                    ${promptsHtml}
                </div>

                <!-- Section: NotebookLM -->
                <div class="section-block">
                    <div class="section-label">${isTr ? '🎙️ NotebookLM Podcast Tartışma Komutu' : '🎙️ NotebookLM Deep Dive Audio Prompt'}</div>
                    <div class="notebooklm-card">
                        <div class="notebooklm-header">
                            <span class="notebooklm-badge">⚡ 2 Co-Hosts Deep Dive Prompt</span>
                        </div>
                        <div class="notebooklm-body" id="nb-script-${lesson.id}">${notebooklm}</div>
                    </div>
                </div>

                <!-- Section: Udemy Outline -->
                <div class="section-block">
                    <div class="section-label">${isTr ? '🎓 Udemy Ders Özeti & Zaman Damgaları' : '🎓 Udemy Lecture Blueprint & Timestamps'}</div>
                    <div class="udemy-card">
                        <ul>${udemyLi}</ul>
                    </div>
                </div>

                <!-- Bottom Navigation (Previous / Next Lesson) -->
                <div style="display: flex; justify-content: space-between; margin-top: 30px; padding-top: 20px; border-top: 1px solid var(--border-subtle);">
                    ${lesson.id > 1 ? `
                        <button class="action-btn" onclick="document.querySelector('a[href=\\'#lesson-${lesson.id - 1}\\']').click();">
                            ← ${isTr ? 'Önceki Ders' : 'Previous Lesson'}
                        </button>
                    ` : '<div></div>'}
                    ${lesson.id < 40 ? `
                        <button class="action-btn primary" onclick="document.querySelector('a[href=\\'#lesson-${lesson.id + 1}\\']').click();">
                            ${isTr ? 'Sonraki Ders' : 'Next Lesson'} →
                        </button>
                    ` : '<div></div>'}
                </div>
            </div>
        `;
    }

    // Initialize
    updateMasterPdfLink();
    renderSidebar();
    renderLesson(currentLessonId);
});
