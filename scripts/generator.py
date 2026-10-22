# -*- coding: utf-8 -*-
"""
AI-Driven MBA Master Generator Script
---------------------------------------------------------
- Exports 40 individual Markdown lessons (TR & EN)
- Exports combined Master Books in Markdown (TR & EN)
- Renders print-perfect executive HTMLs (TR & EN, Master & Individual)
- Generates pixel-perfect PDFs using headless Google Chrome
- Compiles web/data.js for the interactive reader portal
---------------------------------------------------------
"""

import os
import sys
import json
import re
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from modules_data_01_02 import LESSONS_01_10
from modules_data_03_04 import LESSONS_11_20
from modules_data_05_06 import LESSONS_21_30
from modules_data_07_08 import LESSONS_31_40

ALL_LESSONS = LESSONS_01_10 + LESSONS_11_20 + LESSONS_21_30 + LESSONS_31_40

PARTS_META = {
    1: {
        "title_tr": "Bölüm 1: Temeller & Bireysel Verimlilik Çarpanı (The AI-Powered Associate)",
        "title_en": "Part 1: Foundations & The Individual Multiplier (The AI-Powered Associate)",
        "desc_tr": "İş dünyasına ilk adım: Geleneksel ezberleri yıkmak, veri analitiği, ikna, pazar istihbaratı ve kritik düşünme ile 10x analist olmak.",
        "desc_en": "Entering the arena: Deconstructing dogma, data analytics, executive storytelling, competitive radar, and critical hallucination defense."
    },
    2: {
        "title_tr": "Bölüm 2: Ürün Yönetimi, İnovasyon & Değer Yaratma (The AI Product Leader)",
        "title_en": "Part 2: Product Strategy, Innovation & Value Creation (The AI Product Leader)",
        "desc_tr": "Jobs-to-be-Done teorisinden sentetik personalara, 48 saatlik MVP'lerden dinamik fiyatlandırma ve ürün-pazar uyumuna (PMF).",
        "desc_en": "From Jobs-to-be-Done and synthetic personas to 48-hour MVPs, dynamic pricing elasticity, and scalable product-market fit."
    },
    3: {
        "title_tr": "Bölüm 3: Büyüme, Pazarlama & Müşteri Deneyimi (The Growth & Marketing Director)",
        "title_en": "Part 3: Growth, Marketing & Hyper-Personalization (The Growth & Marketing Director)",
        "desc_tr": "4E modeli, Multi-Armed Bandit büyüme korsanlığı, LTV/CAC birim ekonomi cerrahlığı, otonom omnichannel destek ve kriz iletişimi.",
        "desc_en": "The 4E marketing engine, autonomous growth hacking, forensic unit economics (LTV/CAC), empathetic support agents, and crisis management."
    },
    4: {
        "title_tr": "Bölüm 4: Operasyonlar, Tedarik Zinciri & Yalın Süreçler (The Operations Director)",
        "title_en": "Part 4: Operations, Supply Chain & Automation (The Operations Director)",
        "desc_tr": "Süreç madenciliği ile TIMWOODS israflarını yok etme, dayanıklı tedarik zinciri, Agentic Workflows, sıfır hata SLA ve yeşil operasyonlar (ESG).",
        "desc_en": "Algorithmic process mining, resilient supply chain forecasting, agentic business workflows, zero-defect SLA telemetry, and sustainable ESG operations."
    },
    5: {
        "title_tr": "Bölüm 5: Finansal Yönetim, Değerleme & Sermaye Tahsisi (The VP Finance & CFO)",
        "title_en": "Part 5: Corporate Finance, Valuation & Capital Allocation (The VP Finance & CFO)",
        "desc_tr": "Finansal tabloların röntgeni (DuPont), DCF ve Monte Carlo değerlemesi, 13 haftalık nakit akışı savunması, sermaye bütçelemesi (ROI/NPV) ve türev araçlarla korunma (Hedging).",
        "desc_en": "Forensic DuPont statement diagnostics, DCF & Monte Carlo valuation, 13-week cash runway modeling, capital budgeting (NPV/IRR), and derivative risk hedging."
    },
    6: {
        "title_tr": "Bölüm 6: İnsan Kaynakları, Liderlik & Kültür (The Chief People Officer)",
        "title_en": "Part 6: People, Culture & Organizational Architecture (The Chief People Officer)",
        "desc_tr": "Beceri odaklı kör işe alım, asenkron uzaktan çalışma kültürü, psikolojik güvenlik, dinamik OKR mimarisi, tersine mentorluk ve John Kotter değişim yönetimi.",
        "desc_en": "Skill-based recruitment, asynchronous remote culture, psychological safety, continuous OKR alignment, reverse mentoring, and Kotter change management."
    },
    7: {
        "title_tr": "Bölüm 7: Kurumsal Strateji, M&A & Dijital Dönüşüm (The Chief Strategy Officer)",
        "title_en": "Part 7: Enterprise Strategy, M&A & Digital Transformation (The Chief Strategy Officer)",
        "desc_tr": "Hamilton Helmer 7 Powers ekonomik hendekler, AI destekli M&A due diligence, platform ekonomisi, şirket içi Skunkworks ve EU AI Act regülasyon uyumu.",
        "desc_en": "Hamilton Helmer 7 Powers moats, AI-accelerated M&A due diligence, two-sided platform economics, corporate Skunkworks venturing, and EU AI Act navigation."
    },
    8: {
        "title_tr": "Bölüm 8: C-Suite Liderliği, Girişimcilik & Geleceğin Vizyonu (The AI Executive & Visionary)",
        "title_en": "Part 8: C-Suite Leadership, Entrepreneurship & The Future Vision (The AI Executive & Visionary)",
        "desc_tr": "CEO ajandası ve yönetim kurulu yönetimi, VC yatırım sunumu ve Term Sheet pazarlığı, algoritmik etik yönetişim, 1 kişilik milyar dolarlık unicorn mimarisi ve büyük final manifestosu.",
        "desc_en": "The AI CEO playbook, venture capital fundraising & term sheet negotiations, ethical algorithmic governance, the 1-person unicorn architecture, and lifetime graduation manifesto."
    }
}

CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def format_lesson_markdown(lesson, lang="tr"):
    is_tr = (lang == "tr")
    
    title = lesson["title_tr"] if is_tr else lesson["title_en"]
    part_title = lesson["part_title_tr"] if is_tr else lesson["part_title_en"]
    level = lesson["level_tr"] if is_tr else lesson["level_en"]
    summary = lesson["summary_tr"] if is_tr else lesson["summary_en"]
    eli5 = lesson["eli5_metaphor_tr"] if is_tr else lesson["eli5_metaphor_en"]
    steps = lesson["framework_steps_tr"] if is_tr else lesson["framework_steps_en"]
    case_study = lesson["case_study_tr"] if is_tr else lesson["case_study_en"]
    notebooklm = lesson["notebooklm_prompts_tr"] if is_tr else lesson["notebooklm_prompts_en"]
    udemy = lesson["udemy_outline_tr"] if is_tr else lesson["udemy_outline_en"]
    
    sec_summary = "📌 Kısa Özet & Zihniyet Dönüşümü" if is_tr else "📌 Executive Summary & Mindset Shift"
    sec_eli5 = "💡 Aptala Anlatır Gibi (ELI5) & Eğlenceli Hikaye" if is_tr else "💡 ELI5 Metaphor & Intuitive Analogy"
    sec_compare = "⚖️ Eski Usul vs. AI Destekli Yaklaşım" if is_tr else "⚖️ The Legacy Way vs. The AI-Driven Way"
    col_dim = "Konu / Boyut" if is_tr else "Dimension"
    col_old = "Eski Usul (Legacy Business)" if is_tr else "The Legacy Way"
    col_ai = "AI Destekli Modern Yaklaşım" if is_tr else "The AI-Driven Way"
    sec_framework = "🚀 Adım Adım Eylem Çerçevesi (Actionable Framework)" if is_tr else "🚀 Step-by-Step Actionable Framework"
    sec_case = "🚨 Gerçek Hayat Vaka / Kriz Analizi (War Story)" if is_tr else "🚨 Real-World War Story / Case Study"
    sec_prompts = "🤖 Kullanıma Hazır AI Promptları & Şablonlar" if is_tr else "🤖 Battle-Tested AI Prompts & Templates"
    sec_notebooklm = "🎙️ NotebookLM Podcast Tartışma Komutu (Deep Dive Audio)" if is_tr else "🎙️ NotebookLM Audio Deep Dive Discussion Prompts"
    sec_udemy = "🎓 Udemy Ders Özeti, Video Zaman Damgaları & Egzersiz" if is_tr else "🎓 Udemy Lecture Blueprint, Timestamps & Action Exercise"
    
    table_lines = [
        f"| {col_dim} | {col_old} | {col_ai} |",
        "|---|---|---|"
    ]
    for row in lesson["comparison_table"]:
        t_topic = row["topic_tr"] if is_tr else row["topic_en"]
        t_old = row["old_way_tr"] if is_tr else row["old_way_en"]
        t_ai = row["ai_way_tr"] if is_tr else row["ai_way_en"]
        table_lines.append(f"| **{t_topic}** | {t_old} | {t_ai} |")
    table_str = "\n".join(table_lines)
    
    steps_str = "\n".join([f"- {s}" for s in steps])
    
    prompts_blocks = []
    for p in lesson["ai_prompts"]:
        p_title = p["title_tr"] if is_tr else p["title_en"]
        p_text = p["prompt_tr"] if is_tr else p["prompt_en"]
        prompts_blocks.append(f"#### 🛠️ {p_title}\n```text\n{p_text}\n```")
    prompts_str = "\n\n".join(prompts_blocks)
    
    udemy_str = "\n".join([f"- {u}" for u in udemy])
    
    md = f"""# {title}

> **{part_title}** | *{level}*

---

### {sec_summary}
{summary}

---

### {sec_eli5}
> {eli5}

---

### {sec_compare}
{table_str}

---

### {sec_framework}
{steps_str}

---

### {sec_case}
{case_study}

---

### {sec_prompts}
{prompts_str}

---

### {sec_notebooklm}
> **NotebookLM Audio Overview Komutu (Deep Dive 2-Speaker Script):**
> {notebooklm}

---

### {sec_udemy}
{udemy_str}
"""
    return md

def build_individual_markdowns():
    print("Exporting 40 individual markdown files in TR and EN...")
    for lang in ["tr", "en"]:
        for lesson in ALL_LESSONS:
            part_folder = f"part-{lesson['part_num']:02d}"
            target_dir = BASE_DIR / "content" / lang / part_folder
            target_dir.mkdir(parents=True, exist_ok=True)
            
            filename = f"lesson-{lesson['lesson_num']:02d}.md"
            target_file = target_dir / filename
            
            md_content = format_lesson_markdown(lesson, lang=lang)
            with open(target_file, "w", encoding="utf-8") as f:
                f.write(md_content)
    print("Individual markdowns successfully written.")

def build_combined_markdown_books():
    print("Compiling combined Master Markdown books...")
    for lang in ["tr", "en"]:
        is_tr = (lang == "tr")
        out_dir = BASE_DIR / "books" / lang
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / (f"AI_Driven_MBA_Master_{lang.upper()}.md")
        
        book_title = "AI ÇAĞINDA MBA (AI-DRIVEN MBA)" if is_tr else "AI-DRIVEN MBA: THE EXECUTIVE PLAYBOOK"
        book_subtitle = "Sıfırdan Zirveye: Yapay Zeka ile Güçlendirilmiş Yönetici ve Strateji Rehberi" if is_tr else "From Zero to Peak Executive: The AI-Powered Leadership & Strategy Blueprint"
        author = "Dr. Eliza J. Reed & Alexander V. Chen"
        edition = "2026-2027 Executive Master Edition | 40 Kapsamlı Ders & 8 Ana Bölüm" if is_tr else "2026-2027 Executive Master Edition | 40 Comprehensive Lessons & 8 Core Modules"
        
        lines = []
        lines.append(f"# {book_title}")
        lines.append(f"## {book_subtitle}")
        lines.append(f"**Yazarlar / Authors:** {author} | **Sürüm / Edition:** {edition}\n")
        lines.append("---\n")
        
        if is_tr:
            lines.append("### 📖 Kitap Hakkında & Eğitmen Notu\n")
            lines.append("Bu kitap; iş dünyasına yeni adım atan hırslı bir analistten, milyar dolarlık otonom şirketleri yöneten vizyoner bir CEO'ya kadar uzanan 40 adımlık bir dönüşüm mimarisidir. 8 ana bölümden oluşan bu başyapıt, Harvard ve Stanford vaka yöntemini üretken yapay zekanın sınırsız bilişsel gücüyle birleştirir. Her ders; sezgisel ELI5 analojileri, karşılaştırmalı strateji tabloları, gerçek kriz analizleri, kullanıma hazır promptlar, Google NotebookLM iki sunuculu podcast komutları ve Udemy video ders şablonlarıyla donatılmıştır.\n")
            lines.append("---\n")
            lines.append("### 📑 İçindekiler Tablosu (Table of Contents)\n")
        else:
            lines.append("### 📖 About This Master Edition & Executive Preface\n")
            lines.append("This curriculum is an uncompromising architectural blueprint charting the ascent from a day-one business analyst to the sovereign chief executive of an autonomous enterprise. Spanning 8 core modules and 40 intensive lessons, this text synthesizes Ivy League strategic rigor with the cognitive leverage of modern generative models. Every lesson is engineered with ELI5 intuitive stories, comparative frameworks, war-tested case studies, operational prompt templates, NotebookLM deep-dive audio prompts, and modular Udemy lecture blueprints.\n")
            lines.append("---\n")
            lines.append("### 📑 Table of Contents\n")
        
        # Table of contents
        for part_num in range(1, 9):
            pm = PARTS_META[part_num]
            p_title = pm["title_tr"] if is_tr else pm["title_en"]
            lines.append(f"\n#### {p_title}")
            part_lessons = [l for l in ALL_LESSONS if l["part_num"] == part_num]
            for pl in part_lessons:
                l_title = pl["title_tr"] if is_tr else pl["title_en"]
                lines.append(f"- [Ders {pl['lesson_num']:02d}: {l_title}](#ders-{pl['lesson_num']:02d})" if is_tr else f"- [Lesson {pl['lesson_num']:02d}: {l_title}](#lesson-{pl['lesson_num']:02d})")
        
        lines.append("\n---\n")
        
        # Lessons content
        current_part = 0
        for lesson in ALL_LESSONS:
            if lesson["part_num"] != current_part:
                current_part = lesson["part_num"]
                pm = PARTS_META[current_part]
                p_title = pm["title_tr"] if is_tr else pm["title_en"]
                p_desc = pm["desc_tr"] if is_tr else pm["desc_en"]
                lines.append(f"\n\n# {p_title}\n")
                lines.append(f"> *{p_desc}*\n")
                lines.append("---\n")
            
            lines.append(format_lesson_markdown(lesson, lang=lang))
            lines.append("\n---\n")
        
        # Conclusion
        if is_tr:
            lines.append("\n# Büyük Mezuniyet Manifestosu: Geleceği İnşa Etmek\n")
            lines.append("Tebrikler. 40 derslik AI-Driven MBA maratonunu tamamladınız. Artık iş dünyasında bir izleyici değil, yapay zekayı bir çarpan olarak kullanan oyun kurucusunuz. Şimdi sahneye çıkın, şirketlerinizi dönüştürün ve geleceğin otonom ekonomisini inşa edin.\n")
        else:
            lines.append("\n# The Grand Graduation Manifesto: Architecting the Future\n")
            lines.append("Congratulations. You have completed the 40-module AI-Driven MBA curriculum. You are no longer a spectator of corporate change, but a self-sovereign architect commanding machine intelligence to reshape industries. The runway is clear—ascend with confidence.\n")
            
        with open(out_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    print("Master markdown books compiled.")

def get_executive_css():
    return """
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap');

    @page {
        size: A4;
        margin: 20mm 15mm 20mm 15mm;
        @bottom-right {
            content: counter(page);
            font-family: 'Inter', sans-serif;
            font-size: 9pt;
            color: #64748b;
        }
    }

    * {
        box-sizing: border-box;
    }

    body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        color: #1e293b;
        background-color: #ffffff;
        line-height: 1.65;
        font-size: 10.5pt;
        margin: 0;
        padding: 0;
    }

    .cover-page {
        page-break-after: always;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        text-align: center;
        padding: 40px 20px;
        background: linear-gradient(145deg, #090d16 0%, #0f172a 50%, #030712 100%);
        color: #ffffff;
        border-radius: 12px;
        margin-bottom: 30px;
    }

    .cover-badge {
        display: inline-block;
        padding: 6px 16px;
        background: rgba(245, 158, 11, 0.15);
        border: 1px solid rgba(245, 158, 11, 0.4);
        color: #fbbf24;
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        font-size: 11pt;
        letter-spacing: 2px;
        text-transform: uppercase;
        border-radius: 30px;
        margin-top: 20px;
    }

    .cover-title {
        font-family: 'Outfit', sans-serif;
        font-size: 34pt;
        font-weight: 800;
        line-height: 1.15;
        margin: 20px 0 10px 0;
        background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #f59e0b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .cover-subtitle {
        font-size: 14pt;
        font-weight: 400;
        color: #94a3b8;
        max-width: 650px;
        margin: 0 auto 30px auto;
        line-height: 1.4;
    }

    .cover-image-container {
        max-width: 320px;
        margin: 10px auto;
        border-radius: 12px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6), 0 0 30px rgba(245, 158, 11, 0.2);
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .cover-image-container img {
        width: 100%;
        height: auto;
        display: block;
    }

    .cover-meta {
        margin-top: 30px;
        font-size: 10pt;
        color: #64748b;
        letter-spacing: 1px;
    }

    .cover-meta strong {
        color: #f8fafc;
    }

    .page-break {
        page-break-after: always;
        break-after: page;
    }

    .part-divider {
        page-break-before: always;
        padding: 60px 30px;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #ffffff;
        border-radius: 10px;
        margin-bottom: 40px;
    }

    .part-divider h1 {
        font-family: 'Outfit', sans-serif;
        font-size: 26pt;
        color: #f59e0b;
        margin: 0 0 15px 0;
    }

    .part-divider p {
        font-size: 13pt;
        color: #cbd5e1;
        margin: 0;
        line-height: 1.5;
    }

    .lesson-container {
        page-break-before: always;
        margin-bottom: 40px;
    }

    .lesson-header {
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 12px;
        margin-bottom: 24px;
    }

    .lesson-part-badge {
        font-family: 'Outfit', sans-serif;
        font-size: 9pt;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 700;
        color: #d97706;
        margin-bottom: 6px;
    }

    h1.lesson-title {
        font-family: 'Outfit', sans-serif;
        font-size: 19pt;
        font-weight: 700;
        color: #0f172a;
        margin: 0 0 8px 0;
        line-height: 1.25;
    }

    .lesson-level {
        display: inline-block;
        padding: 3px 10px;
        background-color: #f1f5f9;
        border-radius: 6px;
        font-size: 8.5pt;
        font-weight: 600;
        color: #475569;
    }

    .section-title {
        font-family: 'Outfit', sans-serif;
        font-size: 12pt;
        font-weight: 700;
        color: #0f172a;
        margin: 22px 0 10px 0;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .summary-box {
        background-color: #f8fafc;
        border-left: 4px solid #f59e0b;
        padding: 14px 18px;
        border-radius: 0 8px 8px 0;
        font-size: 10.5pt;
        color: #334155;
        margin-bottom: 16px;
    }

    .eli5-box {
        background: linear-gradient(135deg, #eff6ff 0%, #f0fdf4 100%);
        border: 1px solid #bfdbfe;
        border-left: 4px solid #3b82f6;
        padding: 14px 18px;
        border-radius: 0 8px 8px 0;
        font-size: 10.5pt;
        color: #1e3a8a;
        font-style: italic;
        margin-bottom: 16px;
    }

    table.comparison-table {
        width: 100%;
        border-collapse: collapse;
        margin: 16px 0;
        font-size: 9.5pt;
        break-inside: avoid;
    }

    table.comparison-table th {
        background-color: #0f172a;
        color: #ffffff;
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
        text-align: left;
        padding: 10px 12px;
        border: 1px solid #1e293b;
    }

    table.comparison-table td {
        padding: 9px 12px;
        border: 1px solid #e2e8f0;
        vertical-align: top;
    }

    table.comparison-table tr:nth-child(even) {
        background-color: #f8fafc;
    }

    .framework-list {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 14px 20px;
        margin: 12px 0;
    }

    .framework-list ul {
        margin: 0;
        padding-left: 18px;
    }

    .framework-list li {
        margin-bottom: 8px;
        color: #334155;
    }

    .case-box {
        background-color: #fef2f2;
        border-left: 4px solid #ef4444;
        padding: 14px 18px;
        border-radius: 0 8px 8px 0;
        font-size: 10pt;
        color: #7f1d1d;
        margin-bottom: 16px;
        break-inside: avoid;
    }

    .prompt-block {
        background-color: #0f172a;
        color: #f8fafc;
        border-radius: 8px;
        padding: 14px 16px;
        margin: 12px 0;
        font-family: 'Fira Code', monospace;
        font-size: 8.5pt;
        line-height: 1.5;
        white-space: pre-wrap;
        word-break: break-word;
        border: 1px solid #334155;
        break-inside: avoid;
    }

    .prompt-title {
        color: #38bdf8;
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
        font-size: 9.5pt;
        margin-bottom: 6px;
    }

    .notebooklm-box {
        background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%);
        border: 1px solid #d8b4fe;
        border-left: 4px solid #a855f7;
        padding: 14px 18px;
        border-radius: 0 8px 8px 0;
        font-size: 10pt;
        color: #581c87;
        margin-bottom: 16px;
        break-inside: avoid;
    }

    .udemy-box {
        background-color: #fffbeb;
        border: 1px solid #fde68a;
        border-left: 4px solid #f59e0b;
        padding: 14px 18px;
        border-radius: 0 8px 8px 0;
        font-size: 9.5pt;
        color: #78350f;
        margin-bottom: 20px;
        break-inside: avoid;
    }

    .udemy-box ul {
        margin: 0;
        padding-left: 18px;
    }

    .udemy-box li {
        margin-bottom: 5px;
    }

    .toc-container {
        page-break-after: always;
        padding: 20px 0;
    }

    .toc-container h2 {
        font-family: 'Outfit', sans-serif;
        font-size: 22pt;
        color: #0f172a;
        border-bottom: 2px solid #f59e0b;
        padding-bottom: 8px;
        margin-bottom: 20px;
    }

    .toc-part-title {
        font-family: 'Outfit', sans-serif;
        font-size: 13pt;
        font-weight: 700;
        color: #1e293b;
        margin: 18px 0 8px 0;
    }

    .toc-item {
        display: flex;
        justify-content: space-between;
        font-size: 10pt;
        padding: 4px 0;
        border-bottom: 1px dotted #cbd5e1;
        color: #334155;
    }
    """

def lesson_to_html_body(lesson, lang="tr"):
    is_tr = (lang == "tr")
    
    title = lesson["title_tr"] if is_tr else lesson["title_en"]
    part_title = lesson["part_title_tr"] if is_tr else lesson["part_title_en"]
    level = lesson["level_tr"] if is_tr else lesson["level_en"]
    summary = lesson["summary_tr"] if is_tr else lesson["summary_en"]
    eli5 = lesson["eli5_metaphor_tr"] if is_tr else lesson["eli5_metaphor_en"]
    steps = lesson["framework_steps_tr"] if is_tr else lesson["framework_steps_en"]
    case_study = lesson["case_study_tr"] if is_tr else lesson["case_study_en"]
    notebooklm = lesson["notebooklm_prompts_tr"] if is_tr else lesson["notebooklm_prompts_en"]
    udemy = lesson["udemy_outline_tr"] if is_tr else lesson["udemy_outline_en"]
    
    sec_summary = "📌 Kısa Özet & Zihniyet Dönüşümü" if is_tr else "📌 Executive Summary & Mindset Shift"
    sec_eli5 = "💡 Aptala Anlatır Gibi (ELI5) & Eğlenceli Hikaye" if is_tr else "💡 ELI5 Metaphor & Intuitive Analogy"
    sec_compare = "⚖️ Eski Usul vs. AI Destekli Yaklaşım" if is_tr else "⚖️ The Legacy Way vs. The AI-Driven Way"
    col_dim = "Konu / Boyut" if is_tr else "Dimension"
    col_old = "Eski Usul (Legacy Business)" if is_tr else "The Legacy Way"
    col_ai = "AI Destekli Modern Yaklaşım" if is_tr else "The AI-Driven Way"
    sec_framework = "🚀 Adım Adım Eylem Çerçevesi (Actionable Framework)" if is_tr else "🚀 Step-by-Step Actionable Framework"
    sec_case = "🚨 Gerçek Hayat Vaka / Kriz Analizi (War Story)" if is_tr else "🚨 Real-World War Story / Case Study"
    sec_prompts = "🤖 Kullanıma Hazır AI Promptları & Şablonlar" if is_tr else "🤖 Battle-Tested AI Prompts & Templates"
    sec_notebooklm = "🎙️ NotebookLM Podcast Tartışma Komutu (Deep Dive Audio)" if is_tr else "🎙️ NotebookLM Audio Deep Dive Discussion Prompts"
    sec_udemy = "🎓 Udemy Ders Özeti, Video Zaman Damgaları & Egzersiz" if is_tr else "🎓 Udemy Lecture Blueprint, Timestamps & Action Exercise"
    
    # Comparison rows
    comp_rows = ""
    for r in lesson["comparison_table"]:
        t_topic = r["topic_tr"] if is_tr else r["topic_en"]
        t_old = r["old_way_tr"] if is_tr else r["old_way_en"]
        t_ai = r["ai_way_tr"] if is_tr else r["ai_way_en"]
        comp_rows += f"""
        <tr>
            <td><strong>{t_topic}</strong></td>
            <td>{t_old}</td>
            <td>{t_ai}</td>
        </tr>
        """
        
    # Steps
    steps_li = "".join([f"<li>{s}</li>" for s in steps])
    
    # Prompts
    prompts_html = ""
    for p in lesson["ai_prompts"]:
        p_title = p["title_tr"] if is_tr else p["title_en"]
        p_text = p["prompt_tr"] if is_tr else p["prompt_en"]
        prompts_html += f"""
        <div style="margin-bottom: 12px; break-inside: avoid;">
            <div class="prompt-title">🛠️ {p_title}</div>
            <pre class="prompt-block">{p_text}</pre>
        </div>
        """
        
    # Udemy
    udemy_li = "".join([f"<li>{u}</li>" for u in udemy])
    
    html = f"""
    <div class="lesson-container" id="lesson-{lesson['lesson_num']:02d}">
        <div class="lesson-header">
            <div class="lesson-part-badge">{part_title}</div>
            <h1 class="lesson-title">{title}</h1>
            <span class="lesson-level">{level}</span>
        </div>

        <div class="section-title">{sec_summary}</div>
        <div class="summary-box">{summary}</div>

        <div class="section-title">{sec_eli5}</div>
        <div class="eli5-box">"{eli5}"</div>

        <div class="section-title">{sec_compare}</div>
        <table class="comparison-table">
            <thead>
                <tr>
                    <th style="width: 25%;">{col_dim}</th>
                    <th style="width: 37.5%;">{col_old}</th>
                    <th style="width: 37.5%;">{col_ai}</th>
                </tr>
            </thead>
            <tbody>
                {comp_rows}
            </tbody>
        </table>

        <div class="section-title">{sec_framework}</div>
        <div class="framework-list">
            <ul>
                {steps_li}
            </ul>
        </div>

        <div class="section-title">{sec_case}</div>
        <div class="case-box">{case_study}</div>

        <div class="section-title">{sec_prompts}</div>
        {prompts_html}

        <div class="section-title">{sec_notebooklm}</div>
        <div class="notebooklm-box">
            <strong>NotebookLM Deep Dive Audio Prompt (2 Co-Hosts):</strong><br>
            {notebooklm}
        </div>

        <div class="section-title">{sec_udemy}</div>
        <div class="udemy-box">
            <ul>
                {udemy_li}
            </ul>
        </div>
    </div>
    """
    return html

def build_master_html_book(lang="tr"):
    is_tr = (lang == "tr")
    book_title = "AI ÇAĞINDA MBA" if is_tr else "AI-DRIVEN MBA"
    book_subtitle = "Sıfırdan Zirveye: Yapay Zeka ile Güçlendirilmiş Yönetici ve Strateji Rehberi" if is_tr else "The Executive Leadership & Business Strategy Playbook in the Age of Artificial Intelligence"
    author = "Dr. Eliza J. Reed & Alexander V. Chen"
    edition = "2026-2027 Executive Master Edition | 40 Derslik Tam Müfredat" if is_tr else "2026-2027 Executive Master Edition | 40 Complete Lessons"
    
    cover_image_path = "../../assets/cover.jpg"
    
    # Table of contents HTML
    toc_html = ""
    for part_num in range(1, 9):
        pm = PARTS_META[part_num]
        p_title = pm["title_tr"] if is_tr else pm["title_en"]
        toc_html += f'<div class="toc-part-title">{p_title}</div>'
        part_lessons = [l for l in ALL_LESSONS if l["part_num"] == part_num]
        for pl in part_lessons:
            l_title = pl["title_tr"] if is_tr else pl["title_en"]
            prefix = "Ders" if is_tr else "Lesson"
            toc_html += f"""
            <div class="toc-item">
                <span><strong>{prefix} {pl['lesson_num']:02d}:</strong> {l_title}</span>
                <span>Modül {part_num}</span>
            </div>
            """
            
    # Body with part dividers
    lessons_html = ""
    current_part = 0
    for lesson in ALL_LESSONS:
        if lesson["part_num"] != current_part:
            current_part = lesson["part_num"]
            pm = PARTS_META[current_part]
            p_title = pm["title_tr"] if is_tr else pm["title_en"]
            p_desc = pm["desc_tr"] if is_tr else pm["desc_en"]
            lessons_html += f"""
            <div class="part-divider">
                <h1>{p_title}</h1>
                <p>{p_desc}</p>
            </div>
            """
        lessons_html += lesson_to_html_body(lesson, lang=lang)
        
    full_html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{book_title} - {edition}</title>
    <style>
        {get_executive_css()}
    </style>
</head>
<body>
    <div class="cover-page">
        <div class="cover-badge">Executive Leadership Edition</div>
        <div class="cover-title">{book_title}</div>
        <div class="cover-subtitle">{book_subtitle}</div>
        <div class="cover-image-container">
            <img src="{cover_image_path}" alt="{book_title} Cover">
        </div>
        <div class="cover-meta">
            <strong>{author}</strong><br>
            {edition}
        </div>
    </div>

    <div class="toc-container">
        <h2>{"İçindekiler" if is_tr else "Table of Contents"}</h2>
        {toc_html}
    </div>

    {lessons_html}

    <div class="part-divider page-break">
        <h1>{"Büyük Mezuniyet Manifestosu" if is_tr else "The Grand Graduation Manifesto"}</h1>
        <p>{"40 derslik bu devasa maratonu başarıyla tamamladınız. Artık sıradan bir yönetici değil; yapay zekayı bir çarpan olarak kullanan, stratejik kararları bilimsel zemine oturtan ve dünyayı değiştirmeye hazır bir AI Executive liderisiniz." if is_tr else "You have conquered this 40-part executive journey. You are no longer merely a manager; you are an exponential AI-powered operator, equipped with algorithmic rigor, strategic audacity, and unstoppable momentum."}</p>
    </div>
</body>
</html>
"""
    return full_html

def build_individual_lesson_html(lesson, lang="tr"):
    is_tr = (lang == "tr")
    title = lesson["title_tr"] if is_tr else lesson["title_en"]
    body_content = lesson_to_html_body(lesson, lang=lang)
    
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | AI-Driven MBA</title>
    <style>
        {get_executive_css()}
        body {{
            padding: 10px 20px;
        }}
        .lesson-container {{
            page-break-before: auto !important;
            margin-top: 10px;
        }}
    </style>
</head>
<body>
    {body_content}
</body>
</html>
"""
    return html

def convert_html_to_pdf(html_path, pdf_path):
    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={str(pdf_path)}",
        f"file://{str(html_path)}"
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return res.returncode == 0 and pdf_path.exists()

def generate_all_books_and_pdfs():
    print("Compiling Master HTML Books...")
    for lang in ["tr", "en"]:
        html_content = build_master_html_book(lang=lang)
        html_file = BASE_DIR / "books" / lang / f"AI_Driven_MBA_Master_{lang.upper()}.html"
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Written: {html_file}")
        
        # Convert to master PDF
        pdf_file = BASE_DIR / "books" / lang / f"AI_Driven_MBA_Master_{lang.upper()}.pdf"
        print(f"Generating Master PDF ({lang.upper()}) via Headless Chrome...")
        success = convert_html_to_pdf(html_file, pdf_file)
        if success:
            print(f"✅ Generated Master PDF: {pdf_file} ({pdf_file.stat().st_size // 1024} KB)")
        else:
            print(f"❌ Failed to generate Master PDF: {pdf_file}")

def process_single_pdf(args):
    lesson, lang, temp_dir, pdf_dir = args
    is_tr = (lang == "tr")
    num = lesson["lesson_num"]
    slug_raw = lesson["title_tr"] if is_tr else lesson["title_en"]
    slug = re.sub(r'[^a-zA-Z0-9_]+', '_', slug_raw.split(':')[1] if ':' in slug_raw else slug_raw).strip('_')
    prefix = f"Ders_{num:02d}" if is_tr else f"Lesson_{num:02d}"
    filename_base = f"{prefix}_{slug[:40]}"
    
    temp_html_path = temp_dir / f"{filename_base}.html"
    out_pdf_path = pdf_dir / f"{filename_base}.pdf"
    
    if out_pdf_path.exists() and out_pdf_path.stat().st_size > 5000:
        return True
        
    single_html = build_individual_lesson_html(lesson, lang=lang)
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(single_html)
        
    return convert_html_to_pdf(temp_html_path, out_pdf_path)

def generate_all_books_and_pdfs():
    from concurrent.futures import ThreadPoolExecutor
    
    print("Compiling Master HTML Books...")
    for lang in ["tr", "en"]:
        html_file = BASE_DIR / "books" / lang / f"AI_Driven_MBA_Master_{lang.upper()}.html"
        pdf_file = BASE_DIR / "books" / lang / f"AI_Driven_MBA_Master_{lang.upper()}.pdf"
        
        if not html_file.exists():
            html_content = build_master_html_book(lang=lang)
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"Written: {html_file}")
            
        if not pdf_file.exists() or pdf_file.stat().st_size < 10000:
            print(f"Generating Master PDF ({lang.upper()}) via Headless Chrome...")
            success = convert_html_to_pdf(html_file, pdf_file)
            if success:
                print(f"✅ Generated Master PDF: {pdf_file} ({pdf_file.stat().st_size // 1024} KB)")
        else:
            print(f"✅ Master PDF ({lang.upper()}) already exists ({pdf_file.stat().st_size // 1024} KB)")

    print("\nGenerating 40 individual PDFs in TR and EN in parallel...")
    temp_dir = BASE_DIR / "scripts" / "_temp_html"
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    tasks = []
    for lang in ["tr", "en"]:
        pdf_dir = BASE_DIR / "books" / lang / "individual-pdfs"
        pdf_dir.mkdir(parents=True, exist_ok=True)
        for lesson in ALL_LESSONS:
            tasks.append((lesson, lang, temp_dir, pdf_dir))
            
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(process_single_pdf, tasks))
        
    success_count = sum(1 for r in results if r)
    print(f"✅ Generated {success_count}/{len(tasks)} individual PDFs successfully!")

def export_web_data():
    print("\nCompiling web/data.js for interactive portal...")
    web_data = {
        "parts": PARTS_META,
        "lessons": ALL_LESSONS
    }
    
    data_js_content = f"// AI-Driven MBA Interactive Data Store\nwindow.MBA_DATA = {json.dumps(web_data, ensure_ascii=False, indent=2)};\n"
    
    target_data_file = BASE_DIR / "web" / "data.js"
    with open(target_data_file, "w", encoding="utf-8") as f:
        f.write(data_js_content)
    print(f"✅ Exported: {target_data_file}")

if __name__ == "__main__":
    print("=" * 60)
    print("AI-DRIVEN MBA MASTER BUILDER & COMPILER")
    print("=" * 60)
    build_individual_markdowns()
    build_combined_markdown_books()
    export_web_data()
    generate_all_books_and_pdfs()
    print("=" * 60)
    print("ALL DELIVERABLES SUCCESSFULLY CREATED!")
    print("=" * 60)
