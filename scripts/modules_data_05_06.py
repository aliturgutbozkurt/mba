# -*- coding: utf-8 -*-
"""
AI-Driven MBA - Modules 05 & 06 (Lessons 21 - 30)
Part 5: Finansal Yönetim, Değerleme & Sermaye Tahsisi (Corporate Finance & Capital Allocation)
Part 6: İnsan Kaynakları, Liderlik & Kültür (People, Culture & Organizational Architecture)
"""

LESSONS_21_30 = [
    # -----------------------------------------------------------------
    # PART 5: FİNANSAL YÖNETİM, DEĞERLEME & SERMAYE TAHSİSİ (LESSONS 21-25)
    # -----------------------------------------------------------------
    {
        "id": 21,
        "part_num": 5,
        "part_title_tr": "Bölüm 5: Finansal Yönetim, Değerleme & Sermaye Tahsisi (The Financial Leader & VP Finance)",
        "part_title_en": "Part 5: Corporate Finance, Valuation & Capital Allocation (The Financial Leader & VP Finance)",
        "lesson_num": 21,
        "level_tr": "Seviye 5: Finansal Liderlik / VP Finance",
        "level_en": "Level 5: Financial Leadership / VP Finance",
        "title_tr": "Ders 21: Finansal Tabloların Dili (Bilanço, Gelir Tablosu, Nakit Akışı): AI ile Finansal Röntgen Çekmek",
        "title_en": "Lesson 21: Financial Statements Decoded: Using AI for Instant Financial Audits & Ratio Diagnostics",
        "summary_tr": "Finans, iş dünyasının evrensel dilidir. Bilanço şirketin anlık fotoğrafı, Gelir Tablosu belirli bir dönemin video kaydı, Nakit Akışı Tablosu ise şirketin oksijen tüpüdür. Karmaşık finansal dipnotları ve oranları (DuPont analizi, Faiz Karşılama Oranı, Cari Oran) yapay zeka ile 30 saniyede tarayarak bir şirketin gerçek finansal sağlığını röntgen gibi ortaya çıkarın.",
        "summary_en": "Finance is the lingua franca of executive leadership. The Balance Sheet is a static photograph, the Income Statement is a period film, and the Cash Flow Statement is the corporate oxygen tank. By executing multi-layered ratio diagnostics (DuPont decompositions, interest coverage, quick liquidity) via generative finance interpreters, leaders audit corporate vitality in 30 seconds.",
        "eli5_metaphor_tr": "Bir şirketin finansal tabloları, bir insanın genel sağlık tahliline benzer. Gelir Tablosu insanın ne kadar yemek yediğini (kalori/gelir) gösterir, Bilanço vücudun kas ve yağ oranını (varlık/borç) gösterir, Nakit Akışı ise kalbin pompaladığı kandır. Kalp kan pompalamayı durdurursa (nakit biterse), kaslı ve yakışıklı olsan bile (kârlı görünsen bile) ölürsün!",
        "eli5_metaphor_en": "A company's financial filings are its medical vitals. The Income Statement is your daily calorie intake, the Balance Sheet is your bone density and muscle mass versus body fat, and the Cash Flow Statement is your circulating blood volume. If your blood stops circulating (cash dries up), you die on the table—even if you look handsome and muscular on paper.",
        "comparison_table": [
            {
                "topic_tr": "Mali Tablo Analizi",
                "topic_en": "Statement Analysis",
                "old_way_tr": "100 sayfalık faaliyet raporundaki dipnotları manuel okumak için 3 gün harcamak.",
                "old_way_en": "Manually sifting through 100 pages of dense annual filing footnotes over three days.",
                "ai_way_tr": "AI ile dipnotlardaki şüpheli muhasebe hilelerini ve gizli yükümlülükleri anında taramak.",
                "ai_way_en": "Prompting financial LLMs to isolate aggressive revenue recognition tricks in seconds."
            },
            {
                "topic_tr": "Kârlılık vs. Nakit",
                "topic_en": "Profitability vs. Cash",
                "old_way_tr": "'Şirket kâğıt üzerinde kâr ediyor, demek ki işler harika' yanılgısına kapılmak.",
                "old_way_en": "Equating positive net income with operational health, ignoring negative operating cash.",
                "ai_way_tr": "Faaliyet Nakit Akışı (CFO) ile Net Kâr makasını ölçerek 'kârın kalitesini' denetlemek.",
                "ai_way_en": "Auditing earnings quality: Tracking the divergence between Net Income and Operating Cash Flow."
            },
            {
                "topic_tr": "Oran Analizi (Ratios)",
                "topic_en": "Financial Ratio Diagnostics",
                "old_way_tr": "Sadece tekil oranlara (F/K, ROE) bakıp şirketin neden kâr ettiğini anlayamamak.",
                "old_way_en": "Looking at isolated P/E or ROE figures without decomposing the underlying drivers.",
                "ai_way_tr": "3 Aşamalı DuPont Analizi (Net Marj x Varlık Devir Hızı x Finansal Kaldıraç) çalıştırmak.",
                "ai_way_en": "Automating 3-stage DuPont decomposition: Net Margin x Asset Turnover x Financial Leverage."
            }
        ],
        "framework_steps_tr": [
            "1. Üç Tablonun Dansı: Bilanço ile Gelir Tablosunu birbirine bağlayan 'Dağıtılmamış Kârlar' (Retained Earnings) ve Nakit Akışı köprüsünü kur.",
            "2. DuPont Çözümlemesi: Özsermaye kârlılığının (ROE) gerçekte yüksek marjdan mı, hızlı envanter satışından mı yoksa tehlikeli borçlanmadan mı geldiğini ayrıştır.",
            "3. Kazanç Kalitesi (Earnings Quality) Testi: Faaliyet Nakit Akışı net kârdan düşükse, şirketin vadeli satışlarla sahte kâr yazıp yazmadığını denetle.",
            "4. Stres Testi Raporu: Faiz oranları 500 baz puan artarsa faiz karşılama oranının (EBIT/Faiz Gideri) 1'in altına inip inmeyeceğini simüle et."
        ],
        "framework_steps_en": [
            "1. Bridge the Triad: Trace how Net Income flows into Retained Earnings on the Balance Sheet and anchors Operating Cash Flow.",
            "2. Execute DuPont Decomposition: Dissect whether high Return on Equity (ROE) is driven by operational margin, asset velocity, or toxic leverage.",
            "3. Audit Earnings Quality: If Operating Cash Flow consistently lags Net Income, interrogate aggressive accounts receivable accruals.",
            "4. Run Solvency Stress-Tests: Simulate whether an interest rate spike threatens the Interest Coverage Ratio (EBIT / Interest Expense)."
        ],
        "case_study_tr": "Yazılım sektöründe hızlı büyüyen bir teknoloji şirketi, 2024 yılında 15 milyon TL net kâr açıkladı ve hisseleri tavan yaptı. Ancak şirketin yeni Finans Direktörü (CFO), AI yardımıyla nakit akışı tablosunu incelediğinde şok oldu: Faaliyetlerden nakit akışı eksi 22 milyon TL idi! Şirket, müşterilerine 12 ay vadeli yazılım satmış, gelir tablosuna hemen ciro yazmış ama kasaya tek kuruş para girmemişti. Şirketin sadece 60 günlük nakdi kalmıştı. CFO hemen vadeli satışları durdurdu, iskonto karşılığı peşin ödemeye geçti ve şirketi son andaki bir iflas fırtınasından kurtardı.",
        "case_study_en": "A high-growth enterprise software provider posted a triumphant $4M Net Income, driving a private valuation surge. The newly recruited VP of Finance initiated an automated earnings-quality audit. The analysis uncovered an existential divergence: Operating Cash Flow was negative $6.5M. The sales VP had offered 180-day deferred payment terms to inflate revenue recognition, but zero cash had entered corporate accounts, leaving only 45 days of runway. The VP structured aggressive factoring discounts for immediate cash conversion, averting a sudden terminal liquidity crisis.",
        "ai_prompts": [
            {
                "title_tr": "DuPont Analizi ve Adli Finans Dedektifi",
                "title_en": "Forensic Financial Ratio Diagnostician & DuPont Decomposition",
                "prompt_tr": "Sen dünyanın en kıdemli Wall Street Finans Analisti ve Adli Denetçisisin. Aşağıdaki finansal tablo özetini (Bilanço, Gelir Tablosu, Nakit Akışı) incele: [FİNANSAL VERİLERİ YAPIŞTIR]. 1) DuPont analizini çalıştırarak şirketin ROE kalitesini 3 bileşene (Kârlılık, Verimlilik, Kaldıraç) ayır, 2) Şirketin kârının nakit karşılığını (Earnings Quality) test et, 3) Şirketin önümüzdeki 12 ay içinde karşılaşabileceği en büyük likidite ve borç servisi riskini uyar.",
                "prompt_en": "Act as a Senior Wall Street Equity Research Analyst and Forensic Accountant. Dissect the following three-statement corporate snapshot: [PASTE FINANCIAL DATA]. 1) Execute a complete DuPont 3-stage decomposition explaining ROE dynamics, 2) Evaluate Earnings Quality by comparing Operating Cash Flow against Net Income, 3) Quantify corporate vulnerability to liquidity crunches and interest rate headwinds over the next 4 quarters."
            }
        ],
        "notebooklm_prompts_tr": "İki finans yöneticisi: Biri sadece ciroya ve kâğıt üzerindeki net kâra bakıp kendini zengin sanan saf kurucu, diğeri nakit akışı tablosunun röntgenini çekip 'Kâr bir görüştür, nakit ise gerçeğin ta kendisidir' diyen bilge CFO. 'Finansal tabloların gizli dili ve kârlı şirketlerin neden iflas ettiği' konusunu çarpıcı bir sohbet olarak ele alın.",
        "notebooklm_prompts_en": "A high-stakes boardroom dialogue between an entrepreneur celebrating record paper profits, and a seasoned CFO who reveals the company is three weeks away from payroll insolvency due to negative operating cash flow. Deconstruct why cash flow—not accounting profit—is the ultimate arbiter of corporate survival.",
        "udemy_outline_tr": [
            "00:00 - Finansal Körlüğün Bedeli: Neden Kârlı Şirketler İflas Eder?",
            "04:45 - Üç Temel Tablonun Dansı: Bilanço, Gelir Tablosu ve Nakit Akışı",
            "10:20 - DuPont Çözümlemesi ile Gerçek Şirket Röntgeni Çekmek",
            "16:15 - Canlı Uygulama: 10-K Raporunu AI ile 60 Saniyede Denetlemek",
            "22:50 - Eylem Görevi: Kendi Şirketinin Faaliyet Nakit Akışı / Net Kâr Makasını Hesapla"
        ],
        "udemy_outline_en": [
            "00:00 - The Deadly Cost of Financial Illiteracy: Why Profitable Firms Go Bust",
            "04:45 - The Architectural Symphony: Balancing Sheet, Income, and Cash Flows",
            "10:20 - Advanced DuPont Decomposition: Profit Margin vs. Toxic Leverage",
            "16:15 - Live Lab: Auditing SEC Filings for Aggressive Accruals in 60 Seconds",
            "22:50 - Action Assignment: Calculating the Cash Conversion Ratio for Your Enterprise"
        ]
    },
    {
        "id": 22,
        "part_num": 5,
        "part_title_tr": "Bölüm 5: Finansal Yönetim, Değerleme & Sermaye Tahsisi (The Financial Leader & VP Finance)",
        "part_title_en": "Part 5: Corporate Finance, Valuation & Capital Allocation (The Financial Leader & VP Finance)",
        "lesson_num": 22,
        "level_tr": "Seviye 5: Finansal Liderlik / VP Finance",
        "level_en": "Level 5: Financial Leadership / VP Finance",
        "title_tr": "Ders 22: Şirket Değerleme Metodolojileri: DCF, Çarpanlar ve AI Destekli Senaryo Simülasyonları",
        "title_en": "Lesson 22: Corporate Valuation Models: DCF, Comparables & Monte Carlo AI Simulations",
        "summary_tr": "Bir şirketin değeri ne kasanın büyüklüğüdür ne de sahibinin hayalleridir. Bir işletmenin değeri; gelecekte üreteceği serbest nakit akışlarının (FCF) bugünkü net değeridir. İndirgenmiş Nakit Akışı (DCF), Çarpanlar (EBITDA, ARR katları) ve Monte Carlo simülasyonlarını yapay zeka ile harmanlayarak şirket değerlemelerini spekülasyondan çıkarıp bilimsel bir zemine oturtun.",
        "summary_en": "Enterprise valuation is neither artistic fiction nor accounting arithmetic. The intrinsic value of any commercial organism is the discounted present value of its future free cash flows. By synthesizing Discounted Cash Flow (DCF) mechanics, peer trading comparables, and probabilistic Monte Carlo AI simulations, finance leaders establish defensible, rigorous valuation bounds.",
        "eli5_metaphor_tr": "Bir şirketi satın almak, her yıl altın yumurtlayan bir tavuk satın almaya benzer. Tavuğun değeri, tavuğun tüylerinin güzelliği (ofis binaları) değildir; ömrü boyunca yumurtlayacağı altınların bugünkü parayla ne ettiğidir. Eğer tavuk her yıl 1 altın veriyorsa ve 5 yıl yaşayacaksa, ona 20 altın ödeyen kişi fena halde kazıklanmıştır!",
        "eli5_metaphor_en": "Valuing a company is like buying a golden goose. Its worth is not determined by its feathers or the barn it sleeps in, but solely by the net present market value of the golden eggs it will lay before it expires. If you pay 25 golden eggs for a bird that can only lay 10 in its lifetime, you have committed financial suicide.",
        "comparison_table": [
            {
                "topic_tr": "Değerleme Yaklaşımı",
                "topic_en": "Valuation Philosophy",
                "old_way_tr": "Sektör dedikodularına veya yatırımcının keyfine göre kaba bir çarpan (Örn: 10x ARR) uydurmak.",
                "old_way_en": "Blindly applying arbitrary peer multiples ('Everyone in SaaS is trading at 15x ARR').",
                "ai_way_tr": "İçsel Değerleme (DCF) ile Piyasa Çarpanlarını (Comps) birleştiren hibrit değerleme.",
                "ai_way_en": "Triangulating intrinsic DCF mechanics with liquidity-adjusted peer trading multiples."
            },
            {
                "topic_tr": "İskonto Oranı (WACC)",
                "topic_en": "Discount Rate (WACC)",
                "old_way_tr": "WACC oranını sabit bir varsayımla %10 alıp piyasa faiz oynaklığını unutmak.",
                "old_way_en": "Assuming a static, hand-waved 10% discount rate without risk modeling.",
                "ai_way_tr": "Borç/Özsermaye maliyetini ve ülke risk primini AI ile anlık güncelleyerek dinamik WACC hesaplamak.",
                "ai_way_en": "Dynamically calculating Weighted Average Cost of Capital adjusted for sovereign risk spreads."
            },
            {
                "topic_tr": "Belirsizlik ve Risk Modelleme",
                "topic_en": "Uncertainty Modeling",
                "old_way_tr": "Sadece tek bir 'en iyi ihtimal' senaryosu çizipExcel'de kendini kandırmak.",
                "old_way_en": "Building a single static baseline model where revenues conveniently grow 40% every year.",
                "ai_way_tr": "10.000 farklı ekonomik senaryoyu koşturan olasılıksal Monte Carlo AI simülasyonu.",
                "ai_way_en": "10,000-iteration Monte Carlo AI runs generating full probability distributions of enterprise value."
            }
        ],
        "framework_steps_tr": [
            "1. Serbest Nakit Akışı (Unlevered FCF) Modelle: Faaliyet kârından vergiyi düş, amortismanı ekle, CapEx ve İşletme Sermayesi değişimini çıkar.",
            "2. WACC Hesapla: Şirketin ağırlıklı ortalama sermaye maliyetini (Borç Maliyeti x Borç Oranı + Özkaynak Maliyeti x Özkaynak Oranı) belirle.",
            "3. Uç Değer (Terminal Value) Tahmini: Şirketin sonsuza dek büyüme hızını (Gordon Growth) makul ülke büyüme oranına (%2-3) sabitle.",
            "4. Monte Carlo Duyarlılık Matrisi: Büyüme oranı %2 düşer veya iskonto oranı %1 artarsa şirket değerinin ne olacağını ısı haritasında göster."
        ],
        "framework_steps_en": [
            "1. Model Unlevered Free Cash Flow (UFCF): NOPAT + D&A - Capital Expenditures - Change in Net Working Capital.",
            "2. Compute Dynamic WACC: Weight the after-tax cost of debt with the Capital Asset Pricing Model (CAPM) cost of equity.",
            "3. Anchor Terminal Value Rigor: Bound terminal perpetuity growth strictly below the long-term GDP expansion rate (2-3%).",
            "4. Execute Sensitivity Matrix: Run dual-axis tables testing enterprise value across fluctuating WACC and terminal growth bounds."
        ],
        "case_study_tr": "Bir lojistik yazılımı girişimi, Seri A turunda 'Biz geleceğin unicornuyuz, değerlememiz 50 milyon $' diyerek yatırımcı masasına oturdu. Yatırımcılar bu afaki rakamı reddetti ve görüşmeler tıkandı. Girişimin finans danışmanı, şirketin son 3 yıllık kohort verilerini ve geleceğe dönük UFCF projeksiyonlarını AI tabanlı bir DCF ve Monte Carlo motoruna döktü. Simülasyon, şirketin en olası içsel değerinin 32.4 milyon $ olduğunu, %80 güven aralığında 28M $ ile 36M $ arasında kaldığını kanıtladı. Girişim bu bilimsel raporu masaya koydu; VC fonu 32 milyon $ değerleme üzerinden 8 milyon $ yatırımı tereddütsüz imzaladı.",
        "case_study_en": "A logistics tech startup entered Series A negotiations demanding a $50M pre-money valuation based on inflated optimism, hitting an immediate investor wall. The finance lead structured a rigorous valuation framework: Unlevered FCF projections paired with an AI-driven 10,000-run Monte Carlo simulation modeling revenue growth and churn variance. The model established a tight 80% confidence interval of intrinsic enterprise value between $28M and $36M, with a median of $32.4M. Armed with defensible math, the founders closed an $8M round at a $32M valuation without friction.",
        "ai_prompts": [
            {
                "title_tr": "DCF Şirket Değerleme ve Monte Carlo Simülatörü",
                "title_en": "DCF Valuation Engine & Monte Carlo Sensitivity Modeler",
                "prompt_tr": "Sen Goldman Sachs veya Morgan Stanley'de Baş Şirket Değerleme (M&A Valuation) Direktörüsün. Aşağıdaki şirket finansallarını incele: [GELİR, BÜYÜME, FAVÖK MARJI, CAPEX VE BORÇ DURUMU]. 1) Gelecek 5 yıllık Serbest Nakit Akışı (FCF) projeksiyonunu kur, 2) Şirket için uygun WACC iskonto oranını ve Terminal Değer çarpanını belirle, 3) Farklı büyüme ve iskonto senaryolarına göre şirketin değerleme aralığını (Bear, Base, Bull senaryoları) tablo halinde hesapla.",
                "prompt_en": "Act as a Principal M&A Valuation Banker at a top-tier investment bank. For the target enterprise data: [INSERT FINANCIALS & CAPEX]: 1) Structure a 5-year Unlevered Free Cash Flow forecast, 2) Formulate a defensible WACC hurdle rate incorporating appropriate beta and debt spreads, 3) Output a multi-scenario sensitivity table (Bear, Base, Bull) illustrating implied enterprise value."
            }
        ],
        "notebooklm_prompts_tr": "İki yatırım uzmanı: Biri kafadan çarpan uydurup şişirme değerlemelerle yatırımcıları kandırmaya çalışan bir hayal tüccarı, diğeri DCF ve Monte Carlo simülasyonlarıyla bir şirketin kuruşu kuruşuna içsel değerini hesaplayan usta değerleme mimarı. 'Şirket değerleme sanatı: Değerleme bir his midir yoksa nakit akışının bilimi midir?' konusunu eğlenceli ve derin bir sohbetle dinleyin.",
        "notebooklm_prompts_en": "A masterclass dialogue between an aggressive startup founder pitching a speculative 30x multiple, and an elite private equity valuation partner who dismantles the thesis using discounted cash flows and sensitivity ranges. Uncover why true enterprise value always converges on cash generation.",
        "udemy_outline_tr": [
            "00:00 - Değerleme Yalanları: Çarpan Balonları Neden Patlar?",
            "04:45 - Bir Şirketin İçsel Değeri (Intrinsic Value) ve FCF Mantığı",
            "10:15 - Ağırlıklı Ortalama Sermaye Maliyeti (WACC) Nasıl Hesaplanır?",
            "16:20 - Canlı Uygulama: AI ile Bir Şirketin 5 Yıllık DCF Modelini Kurmak",
            "22:45 - Eylem Görevi: Kendi İşletmenin veya Bir Halka Açık Şirketin Değerlemesini Yap"
        ],
        "udemy_outline_en": [
            "00:00 - The Speculative Multiples Trap: Why Valuation Bubbles Burst",
            "04:45 - Intrinsic Enterprise Value: The Mechanics of Unlevered Free Cash Flows",
            "10:15 - Demystifying the WACC Discount Rate and Terminal Horizon",
            "16:20 - Live Lab: Constructing a Dynamic 5-Year DCF Engine via AI",
            "22:45 - Action Assignment: Stress-Testing an Enterprise Valuation Sensitivity Matrix"
        ]
    },
    {
        "id": 23,
        "part_num": 5,
        "part_title_tr": "Bölüm 5: Finansal Yönetim, Değerleme & Sermaye Tahsisi (The Financial Leader & VP Finance)",
        "part_title_en": "Part 5: Corporate Finance, Valuation & Capital Allocation (The Financial Leader & VP Finance)",
        "lesson_num": 23,
        "level_tr": "Seviye 5: Finansal Liderlik / VP Finance",
        "level_en": "Level 5: Financial Leadership / VP Finance",
        "title_tr": "Ders 23: Nakit Akışı Yönetimi ve İşletme Sermayesi: Erken Uyarı Sistemleri ile Likidite Krizlerini Önlemek",
        "title_en": "Lesson 23: Working Capital & Liquidity Defense: Predictive Cash Runway Modeling",
        "summary_tr": "Şirketler kârsızlıktan değil, nakit yetersizliğinden batar. Nakit Dönüşüm Süresi (Cash Conversion Cycle - CCC), bir şirketin envantere yatırdığı 1 liranın kaç gün sonra kasaya geri döndüğünü gösteren en acımasız saat mekanizmasıdır. Alacak tahsilatı (DSO), borç ödeme vadesi (DPO) ve stok devir süresini (DIO) yapay zeka ile optimize ederek negatif işletme sermayesiyle şirketi bedava fonlayın.",
        "summary_en": "Companies rarely die of unprofitability; they perish from sudden liquidity asphyxiation. The Cash Conversion Cycle (CCC) is the unforgiving operational clock tracking how many days it takes for capital invested in raw inventory to return as cash. By optimizing DSO, DPO, and DIO through predictive AI, leaders unlock negative working capital, turning vendors and customers into an interest-free growth credit facility.",
        "eli5_metaphor_tr": "Nakit akışı yönetimi, suyun altında dalış yaparken tüpündeki kalan oksijen göstergesine bakmaya benzer. Denizde ne kadar çok balık (satış) gördüğün önemli değildir; eğer oksijen tüpün (nakdin) yüzeye çıkmaya yetmiyorsa boğulursun. Akıllı işletme sermayesi, tüpteki her nefesi hesaplayıp seni asla havasız bırakmayan dijital dalış bilgisayarıdır.",
        "eli5_metaphor_en": "Cash runway management is deep-sea scuba diving with an oxygen pressure gauge. It doesn't matter how much treasure (contracts) you discover on the ocean floor; if your oxygen tank (working capital) empties 50 feet below the surface, you suffocate. Intelligent working capital management guarantees you always have enough air to breach the surface.",
        "comparison_table": [
            {
                "topic_tr": "Nakit Dönüşüm Süresi (CCC)",
                "topic_en": "Cash Conversion Cycle",
                "old_way_tr": "Nakit döngüsünün 90 günü bulmasını dert etmeyip sürekli banka kredisi aramak.",
                "old_way_en": "Tolerating a 90-day cash conversion cycle and constantly taking high-interest loans.",
                "ai_way_tr": "Negatif Nakit Döngüsü (Apple & Amazon modeli): Parayı peşin alıp tedarikçiye 60 günde ödemek.",
                "ai_way_en": "Negative Working Capital (Amazon/Apple playbook): Collecting cash upfront, paying suppliers later."
            },
            {
                "topic_tr": "Alacak Tahsilatı (DSO)",
                "topic_en": "Receivables Management (DSO)",
                "old_way_tr": "Vadesi geçen faturalar için muhasebecinin haftada bir kez çekingen telefonlar açması.",
                "old_way_en": "Waiting until bills are 45 days overdue before awkward manual phone follow-ups.",
                "ai_way_tr": "Ödeme gecikme olasılığı yüksek müşterileri önceden tespit edip dinamik ödeme teşvikleri sunmak.",
                "ai_way_en": "Predictive invoice telemetry triggering algorithmic early-pay discounts before due dates."
            },
            {
                "topic_tr": "Nakit Pisti (Runway) Tahmini",
                "topic_en": "Cash Runway Forecasting",
                "old_way_tr": "Ay sonunda kasadaki parayı görüp '3 ayımız kalmış' diyerek paniğe kapılmak.",
                "old_way_en": "Realizing runway has shrunk to 8 weeks during an emergency monthly bank reconciliation.",
                "ai_way_tr": "13 Haftalık Yuvarlanan Nakit Akışı (13-Week Rolling Cash Flow) ile günlük likidite simülasyonu.",
                "ai_way_en": "Dynamic 13-Week Rolling Cash Flow forecasting simulating daily cash buffers under volatility."
            }
        ],
        "framework_steps_tr": [
            "1. CCC Formülünü Çöz: CCC = DIO (Stok Günü) + DSO (Alacak Günü) - DPO (Borç Günü). Hedef: Bu sayıyı sıfıra veya negatife indirmek!",
            "2. 13 Haftalık Nakit Radarı (13-Week Cash Forecast): Gelecek 90 günün her haftası için nakit giriş ve çıkışlarını kuruşu kuruşuna modelle.",
            "3. Likidite Erken Uyarı Barometresi: Kasa bakiyesi 2 aylık operasyonel giderin altına indiği anda şirket içi harcama kilitlerini otomatik devreye al.",
            "4. Dinamik Erken Ödeme İskontosu: Paraya acil ihtiyaç duyulan haftalarda, borçlu müşterilere 'Şimdi öde %3 indirim kap' AI teklifi yolla."
        ],
        "framework_steps_en": [
            "1. Calibrate the CCC Equation: CCC = Days Inventory Outstanding (DIO) + Days Sales Outstanding (DSO) - Days Payable Outstanding (DPO).",
            "2. Institute the 13-Week Rolling Cash Forecast: Track weekly cash inflows vs. disbursements with granular line-item discipline.",
            "3. Enforce Minimum Liquidity Covenants: Trigger autonomous expenditure freezes whenever cash reserves breach 60 days of fixed OPEX.",
            "4. Deploy Algorithmic Dynamic Discounting: Automatically offer 2% early-pay incentives to slow-paying corporate clients during tight cash cycles."
        ],
        "case_study_tr": "Bir toptan inşaat malzemeleri satıcısı, yıllık cirosunu 40 milyon TL'ye çıkardı ancak şirket maaş ödeyemez hale geldi. Şirket sahibi 'Çok iş yapıyoruz ama paramız nerede?' diye feryat ediyordu. Yeni finans direktörü şirketin CCC tablosunu çıkardı: Malzemeler depoda 65 gün bekliyor (DIO), müteahhitler parayı ortalama 90 günde ödüyor (DSO), fabrika ise tedarikçiye 30 günde ödüyordu (DPO). Nakit döngüsü tam 125 gündü! Yani şirket 125 gün boyunca cebinden para finanse ediyordu. Direktör AI ile talep tahminini düzelterek stok süresini 25 güne indirdi, tahsilata erken ödeme iskontosu getirerek DSO'yu 40 güne çekti ve tedarikçi vadesini 60 güne uzattı. Nakit döngüsü 125 günden 5 güne indi; şirketin kasasında anında 8.5 milyon TL nakit serbest kaldı!",
        "case_study_en": "A construction materials distributor expanded annual revenue to $12M, yet found themselves unable to meet bi-weekly payroll. The owner was bewildered: 'Sales are booming, where is the money?' The interim CFO audited their Cash Conversion Cycle: Inventory sat for 65 days (DIO), contractor receivables dragged to 90 days (DSO), while suppliers demanded payment in 30 days (DPO). The net cash cycle was a brutal 125 days! Every dollar of revenue locked up capital for over four months. By deploying AI stock forecasting, DSO early-settlement terms, and renegotiating vendor terms to 60 days, CCC compressed from 125 days to 5 days, freeing $2.2M in dormant cash immediately.",
        "ai_prompts": [
            {
                "title_tr": "13 Haftalık Nakit Akışı ve İşletme Sermayesi Mimarı",
                "title_en": "13-Week Rolling Cash Flow & Working Capital Optimizer",
                "prompt_tr": "Sen dünyanın en deneyimli Kriz ve Likidite CFO'susun (Turnaround Specialist). Şirketimizin şu çalışma sermayesi verilerini incele: [STOK BEKLEME GÜNÜ, ALACAK TAHSİLAT SÜRESİ, TEDARİKÇİ ÖDEME VADESİ, HAFTALIK NAKİT GİRİŞ/ÇIKIŞLARI]. 1) Nakit Dönüşüm Süresini (CCC) hesapla ve darboğazı açıkla, 2) 13 haftalık yuvarlanan nakit projeksiyonunu kurarak şirketin kasasının kırmızıya düşeceği 'ölüm haftasını' belirle, 3) Banka kredisi çekmeden kasaya 30 günde acil nakit sokacak 3 operasyonel taktik geliştir.",
                "prompt_en": "Act as an elite Corporate Turnaround CFO specializing in emergency liquidity engineering. For these balance sheet parameters: [INSERT DIO, DSO, DPO, WEEKLY RUNWAY METRICS]: 1) Calculate the Net Cash Conversion Cycle and identify liquidity traps, 2) Construct a 13-week rolling cash flow model pinpointing the exact week cash turns negative, 3) Formulate three non-debt operational interventions to generate non-dilutive working capital within 30 days."
            }
        ],
        "notebooklm_prompts_tr": "İki finans lideri: Biri rekor satış yaparken kasasında para kalmadığı için haciz memurlarıyla uğraşan şaşkın patron, diğeri Nakit Dönüşüm Süresini negatif yaparak şirketi tamamen müşterilerin parasıyla büyüten usta CFO. 'Nakit kraldır: Satış yapmak ile parayı kasaya koymak arasındaki ölümcül uçurum' temasını eğlenceli ve öğretici bir dille tartışın.",
        "notebooklm_prompts_en": "A dramatic, cautionary dialogue between a founder whose company collapsed while posting record sales, and a restructuring veteran who explains how unmanaged working capital turns growth into bankruptcy. Deconstruct the mechanical beauty of the Cash Conversion Cycle.",
        "udemy_outline_tr": [
            "00:00 - Büyüme Tuzağı: Neden Çok Satan Şirketler Kasasız Kalır?",
            "04:50 - Nakit Dönüşüm Süresi (CCC) Formülünün Sırları: DIO, DSO, DPO",
            "10:15 - Amazon ve Apple Modeli: Negatif İşletme Sermayesi ile Bedava Fonlanmak",
            "16:20 - Canlı Uygulama: 13 Haftalık Yuvarlanan Nakit Akışını AI ile Modellemek",
            "22:50 - Eylem Görevi: Kendi Şirketinin Nakit Dönüşüm Süresini Gün Olarak Çıkar"
        ],
        "udemy_outline_en": [
            "00:00 - The Overtrading Mirage: Why Accelerating Sales Drains Liquidity",
            "04:50 - The Mathematics of the Cash Conversion Cycle: Decoding DIO, DSO, and DPO",
            "10:15 - Negative Working Capital: How Tech Giants Turn Suppliers into Growth Lenders",
            "16:20 - Live Lab: Generating a Resilient 13-Week Cash Flow Engine via AI",
            "22:50 - Action Assignment: Quantifying Your Enterprise Cash Conversion Velocity"
        ]
    },
    {
        "id": 24,
        "part_num": 5,
        "part_title_tr": "Bölüm 5: Finansal Yönetim, Değerleme & Sermaye Tahsisi (The Financial Leader & VP Finance)",
        "part_title_en": "Part 5: Corporate Finance, Valuation & Capital Allocation (The Financial Leader & VP Finance)",
        "lesson_num": 24,
        "level_tr": "Seviye 5: Finansal Liderlik / VP Finance",
        "level_en": "Level 5: Financial Leadership / VP Finance",
        "title_tr": "Ders 24: Sermaye Bütçelemesi ve ROI Hesabı: Yapay Zeka Yatırımlarının Getirisini Ölçmek ve Savunmak",
        "title_en": "Lesson 24: Capital Budgeting & AI ROI: Evaluating & Defending Tech Capex vs Opex",
        "summary_tr": "Şirketler yapay zeka projelerine milyonlarca dolar harcıyor ancak Yönetim Kurulu masasına oturulduğunda 'Bu yatırımın finansal getirisi (ROI) nerede?' sorusuna yanıt veremiyor. Net Bugünkü Değer (NPV), İç Verim Oranı (IRR) ve Geri Ödeme (Payback) hesaplarını yapay zeka yatırımlarına uygulayarak; spekülatif teknoloji projelerini somut kâr merkezi argümanlarına dönüştürün.",
        "summary_en": "Enterprises squander millions on speculative AI pilots, only to freeze when the Board asks for audited ROI. Modern finance leaders bridge technical capability with fiscal accountability, applying Net Present Value (NPV), Internal Rate of Return (IRR), and Hurdle Rate metrics to defend technology investments as disciplined capital allocation bets.",
        "eli5_metaphor_tr": "Şirketin yapay zeka yatırımı yapması, tarlasına pahalı bir otomatik sulama traktörü almaya benzer. Traktörün renginin güzelliği veya arkasındaki ekranın büyüklüğü seni zengin etmez; traktörün tarladaki buğday hasadını ne kadar artırdığı ve benzin masrafını kaç ayda amorti ettiği önemlidir. Eğer traktör maliyetini çıkaramıyorsa, o traktör bir yatırım değil, pahalı bir oyuncaktır!",
        "eli5_metaphor_en": "Investing in enterprise AI is like buying a robotic combine harvester for a wheat farm. Its futuristic dashboard and titanium paint job won't make you wealthy; what matters is whether it increases bushels harvested per acre while reducing diesel costs enough to pay for itself in 18 months. If it doesn't clear the hurdle, it's not a capital investment—it's an expensive corporate toy.",
        "comparison_table": [
            {
                "topic_tr": "Yatırım Gerekçelendirme",
                "topic_en": "Business Case Rigor",
                "old_way_tr": "'Geri kalmamak için yapay zeka yapmalıyız' gibi muğlak FOMO argümanları.",
                "old_way_en": "FOMO-driven budgeting: 'We must build an AI tool because competitors have one.'",
                "ai_way_tr": "Net Bugünkü Değer (NPV > 0) ve İç Verim Oranı (IRR > WACC) ile somut finansal savunma.",
                "ai_way_en": "Quantified hurdle modeling: Validating projects where NPV > 0 and IRR exceeds corporate hurdle rates."
            },
            {
                "topic_tr": "Maliyet Yapısı (CapEx vs. OpEx)",
                "topic_en": "Cost Topology (CapEx vs OpEx)",
                "old_way_tr": "Milyon dolarlık sunucu yatırımları yapıp şirketin nakdini sabit varlıklara gömmek.",
                "old_way_en": "Sunken on-premise hardware CapEx that depreciates rapidly on the balance sheet.",
                "ai_way_tr": "Tüketime dayalı esnek bulut ve API OpEx modelleriyle sermaye verimliliğini korumak.",
                "ai_way_en": "Elastic consumption-based OpEx models that dynamically scale directly with business volume."
            },
            {
                "topic_tr": "Verimlilik ve Getiri Ölçümü",
                "topic_en": "Return Attribution",
                "old_way_tr": "'Çalışanlar çok memnun kaldı' gibi sübjektif hislerle projeyi kapatmak.",
                "old_way_en": "Declaring victory based on vague qualitative user-satisfaction surveys.",
                "ai_way_tr": "Tasarruf edilen adam-saat, azalan hata maliyeti ve artan ciro ile net ROI hesabı.",
                "ai_way_en": "Hard monetary attribution: Audited man-hour recapture, scrap reduction, and net revenue lift."
            }
        ],
        "framework_steps_tr": [
            "1. Finansal Metrikleri Belirle: Net Bugünkü Değer (NPV), İç Verim Oranı (IRR) ve İskontolu Geri Ödeme Süresi.",
            "2. Toplam Sahip Olma Maliyetini (TCO) Çıkar: Sadece lisans ücreti değil; API maliyeti, veri temizleme, çalışan eğitimi ve bakım giderlerini dahil et.",
            "3. Sert Tasarruf vs. Yumuşak Tasarruf Ayrımı: Tasarruf edilen zaman gerçekten personel maliyetini düşürüyor veya yeni ciro yaratıyor mu?",
            "4. Aşamalı Fonlama (Stage-Gate Capital Allocation): Paranın tamamını baştan verme; ilk pilotta ROI kanıtlandıkça bütçeyi serbest bırak."
        ],
        "framework_steps_en": [
            "1. Formalize the Capital Appraisal Trio: Net Present Value (NPV), Internal Rate of Return (IRR), and Discounted Payback.",
            "2. Quantify True Total Cost of Ownership (TCO): Ingest token API expenses, data sanitization, security audits, and continuous fine-tuning overhead.",
            "3. Differentiate Hard vs. Soft Savings: Validate whether recaptured man-hours directly translate into headcount reduction or quantifiable incremental revenue.",
            "4. Enforce Stage-Gate Capital Tranches: Fund tech initiatives in venture-style tranches released strictly upon audited milestone completion."
        ],
        "case_study_tr": "Büyük bir telekomünikasyon şirketi, çağrı merkezine 3 milyon dolarlık bir yapay zeka konuşma motoru kurmak istedi. CFO projeyi 'pahalı bir fantezi' diyerek veto etti. Proje lideri pes etmedi; projeyi bir sermaye bütçelemesi modeline döktü: 'Yıllık 1.4 milyon $ çağrı yönlendirme tasarrufu, %18 daha hızlı problem çözümü ve 1.8 yılda kendini amorti eden bir yatırım (NPV = 2.1M $, IRR = %34).' Bu net finansal tablo karşısında CFO projeyi onayladı. Sistem devreye alındıktan 14 ay sonra yatırım maliyetini tamamen çıkardı ve şirkete yılda 1.6 milyon $ net nakit üretmeye başladı.",
        "case_study_en": "A telecommunications giant's customer service division requested $3M to deploy an enterprise conversational AI agent. The CFO summarily rejected the proposal as corporate vanity. The project director rebuilt the proposal as an institutional capital budgeting dossier: Projecting a $1.4M annual Tier-1 support reduction, an 18-month discounted payback, an NPV of $2.1M at a 12% WACC, and an IRR of 34%. Confronted with defensible cash-flow modeling, the CFO signed the authorization. The platform achieved full capital recoupment in 14 months, generating $1.6M in recurring annual cash savings.",
        "ai_prompts": [
            {
                "title_tr": "Sermaye Bütçelemesi ve Teknoloji ROI Savunma Mimarı",
                "title_en": "Capital Budgeting & Technology ROI Defense Dossier",
                "prompt_tr": "Sen Fortune 100 şirketinde Yatırım Komitesi Başkanı ve Baş Finans Direktörüsün (CFO). Masandaki şu teknoloji/yapay zeka yatırım teklifini incele: [YATIRIM MALİYETİ, BEKLENEN TASARRUF VE PROJE DETAYI]. 1) Bu projenin Net Bugünkü Değerini (NPV) ve İç Verim Oranını (IRR) 5 yıllık nakit akışlarıyla modelle, 2) Yönetim Kuruluna sunulacak 'Yatırım Karar Notu'nu (Capital Allocation Memo) hazırla, 3) Projenin başarısız olması durumunda zararı kesecek (Kill Switch) 3 aşamalı denetim kapısı (Stage-Gate) koy.",
                "prompt_en": "Act as an Investment Committee Chair and Enterprise CFO. Evaluate this proposed enterprise AI capital requisition: [INSERT INITIAL CAPEX/OPEX, RUNWAY, PROJECTED SAVINGS]. 1) Construct a 5-year discounted cash flow appraisal computing NPV and IRR against a 10% hurdle rate, 2) Draft an airtight Capital Allocation Memo for the Board, 3) Establish a three-stage Stage-Gate milestone protocol with strict kill-switch triggers if ROI drifts below thresholds."
            }
        ],
        "notebooklm_prompts_tr": "İki yönetici: Biri her yeni teknolojiye körü körüne milyon dolarlar saçıp batıran vizyonsuz teknoloji müdürü, diğeri her yatırımın kuruş kuruş ROI ve NPV hesabını çıkarıp şirketin parasını altın gibi çoğaltan sermaye tahsisi ustası. 'Yapay zeka yatırımlarının gerçek getirisi: Fantezi mi, kâr makinesi mi?' konusunu nefes kesici bir dille tartışın.",
        "notebooklm_prompts_en": "A gripping corporate confrontation between a tech executive pursuing speculative AI vanity projects, and an unsparing CFO demanding audited ROI, NPV, and IRR metrics. Break down how disciplined capital allocation separates market titans from bankrupt experimenters.",
        "udemy_outline_tr": [
            "00:00 - FOMO Odaklı Bütçelemenin Sonu: Yapay Zeka Neden ROI Üretmelidir?",
            "04:50 - Sermaye Bütçelemesinin Üç Silahşörü: NPV, IRR ve İskontolu Payback",
            "10:15 - CapEx vs. OpEx: Bulut Çağında Sermaye Tahsisi Mimarisi",
            "16:20 - Canlı Uygulama: 3 Milyon Dolarlık Bir Projenin Finansal Savunmasını Hazırlamak",
            "22:45 - Eylem Görevi: Kendi Ekibinin Bir Teknoloji Harcaması İçin ROI Dosyası Oluştur"
        ],
        "udemy_outline_en": [
            "00:00 - The Death of FOMO Budgeting: Demanding Quantifiable Tech ROI",
            "04:50 - The Holy Trinity of Capital Appraisal: NPV, IRR, and Payback Velocity",
            "10:15 - CapEx vs. OpEx Topologies in the Generative Infrastructure Era",
            "16:20 - Live Lab: Structuring an Airtight Executive Capital Allocation Memo",
            "22:45 - Action Assignment: Building an Audited Business Case for Your Next Tech Requisition"
        ]
    },
    {
        "id": 25,
        "part_num": 5,
        "part_title_tr": "Bölüm 5: Finansal Yönetim, Değerleme & Sermaye Tahsisi (The Financial Leader & VP Finance)",
        "part_title_en": "Part 5: Corporate Finance, Valuation & Capital Allocation (The Financial Leader & VP Finance)",
        "lesson_num": 25,
        "level_tr": "Seviye 5: Finansal Liderlik / VP Finance",
        "level_en": "Level 5: Financial Leadership / VP Finance",
        "title_tr": "Ders 25: Risk Yönetimi ve Türev Araçlar: Kur, Enflasyon ve Piyasa Şoklarına Karşı AI Koruma Kalkanı",
        "title_en": "Lesson 25: Enterprise Risk Management: AI Hedging Strategies Against Macroeconomic Shocks",
        "summary_tr": "Döviz kurlarındaki bir gecelik sıçrama, emtia fiyatlarındaki patlama veya faiz şokları; yıllardır başarıyla yönetilen bir şirketi haftalar içinde iflasa sürükleyebilir. Türev araçları (Forward, Futures, Opsiyonlar) ve yapay zeka destekli Risk Değeri (Value at Risk - VaR) modellerini kullanarak, şirketin bilançosunu öngörülemez makroekonomik fırtınalara karşı zırh gibi koruyun.",
        "summary_en": "An overnight currency devaluation, commodity supply crunch, or sovereign interest rate shock can eradicate a decade of operational excellence in thirty days. Modern financial leaders deploy derivative instruments (Forwards, Options, Swaps) paired with AI-driven Value at Risk (VaR) telemetry to construct an impenetrable corporate balance sheet shield against macroeconomic turbulence.",
        "eli5_metaphor_tr": "Türev araçlarla risk yönetimi (Hedging), tatile çıkarken yağmur yağma ihtimaline karşı küçük bir şemsiye parası ödemeye benzer. Hava güneşli kalırsa şemsiyeye verdiğin küçük para yanar ama tatilin güzel geçer; eğer şiddetli bir fırtına koparsa, o şemsiye seni zatürre olmaktan ve hastaneye düşmekten kurtarır!",
        "eli5_metaphor_en": "Financial hedging is buying a tailored insurance policy before sailing into uncharted waters. If the skies stay clear, the modest option premium you paid expires worthless and you sail merrily. But when a category-5 macroeconomic typhoon strikes, that protective contract keeps your hull intact while uninsured vessels sink around you.",
        "comparison_table": [
            {
                "topic_tr": "Makroekonomik Risk Duruşu",
                "topic_en": "Risk Posture",
                "old_way_tr": "Kadercilik: 'Döviz yükselirse zam yaparız, yapacak bir şey yok' tembelliği.",
                "old_way_en": "Fatalistic passivity: 'If the exchange rate jumps, we will just raise prices and pray.'",
                "ai_way_tr": "Proaktif Korunma (Hedging): Kur ve faiz riskini türev kontratlarla önceden kilitlemek.",
                "ai_way_en": "Algorithmic Hedging: Locking foreign exchange, interest rates, and commodity inputs via derivatives."
            },
            {
                "topic_tr": "Risk Ölçüm Yöntemi",
                "topic_en": "Risk Telemetry",
                "old_way_tr": "Sadece sezgilere ve televizyondaki yorumcuların tahminlerine göre hareket etmek.",
                "old_way_en": "Relying on television pundits and gut instinct to guess market directions.",
                "ai_way_tr": "Riske Maruz Değer (VaR) ve stres testi senaryolarını günlük simüle etmek.",
                "ai_way_en": "Dynamic Value at Risk (VaR) modeling simulating tail-risk probability distributions daily."
            },
            {
                "topic_tr": "Bilanço Dayanıklılığı",
                "topic_en": "Balance Sheet Resilience",
                "old_way_tr": "Açık pozisyon taşıyıp devalüasyon gecelerinde kabus görmek.",
                "old_way_en": "Carrying unhedged net foreign liability balances, vulnerable to sudden margin calls.",
                "ai_way_tr": "Doğal korunma (Natural Hedge) ve finansal türevleri harmanlayan zırhlı bilanço.",
                "ai_way_en": "Synthetic and natural hedging: Matching foreign currency revenues directly to supplier liabilities."
            }
        ],
        "framework_steps_tr": [
            "1. Net Açık Pozisyonu Haritala: Döviz cinsinden varlıkların ile borçların arasındaki farkı (Döviz Pozisyon Açığı) netleştir.",
            "2. Doğal Korunma (Natural Hedge) Uygula: Mümkünse döviz borcun varsa döviz cinsi ihracat gelirlerini artırarak riski sıfırla.",
            "3. Finansal Korunma (Forward & Opsiyonlar): Kalan açık risk için vadeli forward anlaşması yap veya aşağı yönlü riski sınırlayan Put opsiyonu satın al.",
            "4. Riske Maruz Değer (VaR) Limiti: Şirket yönetim kurulunun onayladığı maksimum günlük kayıp eşiğini belirle; aşılırsa otomatik hedge pozisyonu aç."
        ],
        "framework_steps_en": [
            "1. Map Net Currency & Commodity Exposure: Quantify total foreign denominated liabilities against predictable foreign currency receivables.",
            "2. Optimize Natural Hedging: Re-denominate supplier purchase contracts into customer billing currencies to structurally neutralize volatility.",
            "3. Deploy Synthetic Financial Hedges: Utilize forward exchange contracts to lock operational cash flows and collar options for tail-risk insurance.",
            "4. Enforce Dynamic Value at Risk (VaR) Covenants: Mandate algorithmic hedge triggers whenever projected 99% 30-day downside risk breaches reserves."
        ],
        "case_study_tr": "Türkiye'de faaliyet gösteren büyük bir kimya üreticisi, hammaddelerini euro ile ithal edip iç pazara TL ile vadeli satıyordu. Şirketin 12 milyon euro döviz açığı vardı. Yeni Finans Direktörü (Treasury VP), AI destekli makro senaryo analizinde dövizde ani bir dalgalanma riskini yüksek gördü. Şirket genel müdürünü ikna ederek açığın %75'ini vadeli forward sözleşmeleriyle sabitledi. İki ay sonra kurda beklenmedik bir devalüasyon şoku yaşandı ve kur %35 fırladı. Sektördeki rakipler devasa kur zararları yazıp konkordato ilan ederken; bu üretici forward sözleşmesi sayesinde hammaddeyi kriz öncesi fiyattan aldı, pazar payını ikiye katladı ve yılı rekor kârla kapattı.",
        "case_study_en": "An industrial chemicals manufacturer imported primary raw materials in EUR while selling domestically on 90-day local currency terms, holding an unhedged 12M EUR net exposure. The newly appointed VP of Treasury deployed macro volatility telemetry signaling high tail-risk probability. Overcoming internal resistance, she hedged 75% of the exposure via FX forwards and collar options. Eight weeks later, a sudden sovereign currency devaluation drove an instantaneous 35% FX spike. Competitors faced devastating balance-sheet write-downs and insolvency, while the hedged manufacturer secured raw supplies at pre-crisis rates, absorbed distressed market share, and achieved record net operating margins.",
        "ai_prompts": [
            {
                "title_tr": "Hazine Direktörü ve Kurumsal Risk Kalkanı Mimarı",
                "title_en": "Chief Risk Officer & Enterprise Hedging Strategist",
                "prompt_tr": "Sen dünyanın en büyük yatırım bankalarından birinin Kurumsal Hazine ve Risk Yönetimi Direktörüsün (Head of Corporate Treasury). Şirketimizin şu bilanço ve piyasa risklerini incele: [DÖVİZ BORCU, GELİR DAĞILIMI, EMTAİ GİRDİLERİ VE FAİZ YAPISI]. 1) Bu şirketin Net Döviz ve Emtia Pozisyon Açığını analiz et, 2) Şirketi batmaktan koruyacak en maliyet etkin Korunma (Hedging) stratejisini (Forward, Opsiyon veya Doğal Hedge) kurgula, 3) Dövizin %25 artması veya hammadde fiyatının %30 fırlaması durumunda şirketin nakit akışını koruyacak eylem planını yaz.",
                "prompt_en": "Act as a Managing Director of Corporate Treasury and Enterprise Risk Management. For the following corporate balance sheet inputs: [INSERT FX DEBT, REVENUE SPLIT, RAW COMMODITY INPUTS, INTEREST EXPOSURE]: 1) Quantify net open currency and interest rate mismatch vulnerabilities, 2) Formulate an institutional Hedging Strategy (Forward contracts, costless collars, or synthetic swaps) to insulate operating margins, 3) Model enterprise balance-sheet resilience under a sudden 30% commodity inflation and 25% FX shock scenario."
            }
        ],
        "notebooklm_prompts_tr": "İki finans lideri: Biri kur ve faiz riskine karşı hiçbir önlem almayıp devalüasyon gecesinde şirketi batıran kumarbaz ruhlu patron, diğeri türev araçlar ve yapay zeka risk modelleriyle şirketin bilançosuna çelik bir zırh giydiren usta risk direktörü. 'Risk yönetimi kumar değil, hayatta kalma kalkanıdır' konusunu nefes kesen bir finansal kriz hikayesiyle tartışın.",
        "notebooklm_prompts_en": "A gripping treasury podcast debate: Dissecting how sudden currency crashes destroy unhedged businesses overnight. Contrast the reckless complacency of speculative founders with the rigorous balance-sheet defense engineered by modern Chief Risk Officers using derivative hedges and probabilistic Value at Risk modeling.",
        "udemy_outline_tr": [
            "00:00 - Bir Gecede Şirket Batıran Makro Şoklar: Devalüasyon ve Enflasyon",
            "04:50 - Riske Maruz Değer (Value at Risk - VaR) Nedir ve Nasıl Hesaplanır?",
            "10:15 - Türev Araçlar Cephaneliği: Forward, Futures, Opsiyonlar ve Swapr",
            "16:20 - Canlı Vaka: 12 Milyon Euroluk Döviz Açığını Sıfır Maliyetli Yaka (Collar) ile Korumak",
            "22:50 - Bölüm 5 Kapanış Sınavı: Finansal Yönetim ve Değerleme Sertifikasyon Görevi"
        ],
        "udemy_outline_en": [
            "00:00 - Anatomy of an Overnight Collapse: Currency Crises and Macro Volatility",
            "04:50 - Demystifying Value at Risk (VaR) and Tail-Risk Probability Distributions",
            "10:15 - The Derivative Arsenal: Forwards, Costless Collars, and Synthetic Swaps",
            "16:20 - Live Case Study: Shielding a $12M Foreign Exchange Gap from Devaluation",
            "22:50 - Part 5 Capstone Project: Financial Leadership & Capital Allocation Certification"
        ]
    },

    # -----------------------------------------------------------------
    # PART 6: İNSAN KAYNAKLARI, LİDERLİK & KÜLTÜR (LESSONS 26-30)
    # -----------------------------------------------------------------
    {
        "id": 26,
        "part_num": 6,
        "part_title_tr": "Bölüm 6: İnsan Kaynakları, Liderlik & Kültür (The Chief People Officer & Culture Builder)",
        "part_title_en": "Part 6: People, Culture & Organizational Architecture (The Chief People Officer & Culture Builder)",
        "lesson_num": 26,
        "level_tr": "Seviye 6: Organizasyonel Liderlik / Chief People Officer",
        "level_en": "Level 6: Organizational Leadership / Chief People Officer",
        "title_tr": "Ders 26: AI Çağında Yetenek Kazanımı ve İşe Alım: Bias İçermeyen, Beceri Odaklı Aday Eşleştirme",
        "title_en": "Lesson 26: AI-Powered Talent Acquisition: Skill-Based Recruiting & Bias Mitigation",
        "summary_tr": "Kişisel torpiller, gösterişli üniversite diplomaları ve süslü CV'ler devri kapandı. Modern yetenek yönetimi; adayın hangi okuldan mezun olduğuna değil, somut problem çözme becerisine, öğrenme çevikliğine ve yapay zekayı bir çarpan olarak kullanma yeteneğine odaklanan tarafsız, beceri odaklı (Skill-Based) algoritmik bir eşleştirme sistemidir.",
        "summary_en": "Pedigree-based hiring, Ivy League credentials, and embellished CVs are obsolete heuristics. Next-generation talent architecture pivots from static pedigrees to verified cognitive capability, learning agility, and AI symbiosis—deploying debiased, skill-based algorithmic screening that surfaces top 1% non-traditional performers while neutralizing historical hiring biases.",
        "eli5_metaphor_tr": "Eski usul işe alım, bir basketbol takımına oyuncu seçerken boyuna veya giydiği pahalı spor ayakkabıya bakmaya benzer; adam hiç şut atamasa bile ayakkabısı güzel diye takıma alırsın. Becerı odaklı işe alım ise adayı hemen sahaya çıkarıp 100 tane üçlük attırmaktır: Kaç tanesini soktuysa takımda o yer alır!",
        "eli5_metaphor_en": "Legacy recruiting is selecting a basketball point guard based on the prestige of his sneakers and the private school he attended, rather than seeing him shoot. Skill-based recruitment puts the candidate on the court for 20 minutes to shoot three-pointers against pressure: The scoreboard does not care about pedigree, only verified execution.",
        "comparison_table": [
            {
                "topic_tr": "Eleme Kriteri",
                "topic_en": "Screening Paradigm",
                "old_way_tr": "Üniversite adı, şirket unvanları ve süslü anahtar kelimelere göre CV taramak.",
                "old_way_en": "Keyword-matching CVs prioritizing prestige universities and Fortune 500 logos.",
                "ai_way_tr": "Gerçek dünya problem çözme simülasyonları ve canlı beceri grafiği (Skill Graph) analizi.",
                "ai_way_en": "Algorithmic Skill Graph mapping evaluated through real-world work sample simulations."
            },
            {
                "topic_tr": "Bilişsel Önyargı (Bias)",
                "topic_en": "Cognitive Bias Mitigation",
                "old_way_tr": "Mülakatçının 'Ben bu adayın enerjisini sevdim' şeklindeki subjektif hisleri.",
                "old_way_en": "Subjective gut-instinct: 'I just liked his vibe during the coffee chat.'",
                "ai_way_tr": "Kör değerlendirme (Blind assessment): İsim, cinsiyet ve yaş gizlenerek sadece performansın puanlanması.",
                "ai_way_en": "Debiased blind evaluations: Stripping demographic markers to evaluate pure merit."
            },
            {
                "topic_tr": "Aday Deneyimi & Hız",
                "topic_en": "Hiring Velocity",
                "old_way_tr": "Bir pozisyonu doldurmak için 45 gün boyunca 6 tur yorucu mülakat yapmak.",
                "old_way_en": "45-day hiring cycles dragging candidates through six repetitive interview loops.",
                "ai_way_tr": "AI ön eleme ve akıllı eşleştirme ile 'Teklif Verme Süresini' (Time-to-Offer) 7 güne indirmek.",
                "ai_way_en": "Compressing Time-to-Offer to 7 days via asynchronous AI skill benchmarks and targeted final interviews."
            }
        ],
        "framework_steps_tr": [
            "1. Görev Profilini Becerilere Ayrıştır: Pozisyonu genel unvanlarla değil, yapılması gereken 5 somut iş çıktısı ve beceriyle tanımla.",
            "2. Gerçekçi İş Numunesi (Work Sample Test): Adaya teorik soru sorma; işe girdiğinde ilk hafta çözeceği gerçek bir kriz senaryosunu ver.",
            "3. Yapay Zeka Çarpanını Ölç: Adayın yapay zekayı nasıl kullandığını test et: 'Bu problemi AI ile 3 kat daha hızlı nasıl çözersin?'",
            "4. Yapılandırılmış Puanlama Rubriği: Her mülakatçıya nesnel bir puan tablosu ver; 'hislerle' karar verilmesini kesinlikle yasakla."
        ],
        "framework_steps_en": [
            "1. Deconstruct JDs into Skill Atoms: Replace generic job descriptions with five verified operational capabilities and outcomes.",
            "2. Deploy Rigorous Work Sample Tests: Evaluate performance on an authentic 90-minute operational simulation rather than hypothetical banter.",
            "3. Assess Cognitive AI Leverage: Evaluate candidate fluency in orchestrating AI agents to solve edge-case challenges under time constraints.",
            "4. Enforce Calibrated Rubrics: Anchor candidate scoring to behavioral rubrics with explicit criteria to eliminate halo and affinity effects."
        ],
        "case_study_tr": "Büyük bir e-ticaret şirketi, yazılım ve veri analisti alımlarında prestijli üniversite mezunlarını tercih ediyor ancak işe alınanların %35'i ilk 6 ayda performans yetersizliğinden ayrılıyordu. Yeni İK Direktörü (CPO), CV taramayı tamamen kaldırdı. Adaylara isimleri ve okulları gizlenmiş şekilde 'Canlı Veri Kriz Simülasyonu' verildi. Değerlendirmede birinci çıkan kişi, üniversite mezunu bile olmayan 21 yaşında kendi kendini yetiştirmiş bir gençti. Şirket onu baş analist olarak işe aldı. 1 yıl sonra o genç, şirketin en yüksek performans puanı alan çalışanı oldu ve şirketin işe alım başarı oranı %92'ye yükseldi.",
        "case_study_en": "A premier enterprise tech marketplace suffered a disastrous 35% first-year turnover rate among engineering hires recruited exclusively from top-tier universities. The newly hired Chief People Officer abolished resume screening entirely. Candidates were administered an anonymized, blind 'Live Production Outage Simulation' assessing algorithmic debugging and AI prompt leverage. The highest scoring candidate across 400 applicants was a 21-year-old self-taught community college dropout. Hired immediately, he became the division's top-ranked performer within nine months, driving company-wide hiring retention to 92%.",
        "ai_prompts": [
            {
                "title_tr": "Becerı Odaklı İşe Alım ve Kör Mülakat Simülatörü",
                "title_en": "Skill-Based Hiring Architect & Blind Assessment Engine",
                "prompt_tr": "Sen dünyanın en yenilikçi Baş İnsan Kaynakları Yöneticisisin (Chief People Officer - Google ve Netflix kalibresinde). Şirketimize alacağımız şu pozisyonu incele: [POZİSYON ADI VE SORUMLULUKLARI]. 1) Bu rol için diplomalardan bağımsız 4 temel 'İş Numunesi Testi' (Work Sample Challenge) tasarla, 2) Mülakatçıların önyargılarını sıfırlayacak 5 puanlık nesnel bir Değerlendirme Rubriği (Scoring Rubric) oluştur, 3) Adayın yapay zekayı bir süper güç olarak kullanıp kullanmadığını ölçecek 2 kışkırtıcı pratik görev hazırla.",
                "prompt_en": "Act as a visionary Chief People Officer applying Netflix and Stripe talent methodologies. For this role requisition: [INSERT ROLE TITLE & CORE OUTCOMES]: 1) Engineer an anonymized, 60-minute Work Sample Simulation that tests actual day-one operational capability, 2) Design an objective 5-tier behavioral scoring rubric that eliminates affinity bias, 3) Formulate two high-leverage challenges specifically testing candidate proficiency in pairing with AI agents."
            }
        ],
        "notebooklm_prompts_tr": "İki İK yöneticisi: Biri diplomaya, kravata ve adayın nereden mezun olduğuna takıntılı eski kafalı personel müdürü, diğeri üniversiteyi değil saf problem çözme yeteneğini ve AI becerisini ödüllendiren vizyoner yetenek mimarı. 'CV'lerin ölümü ve yetenek avcılığında liyakat devrimi' konusunu esprili ve çarpıcı örneklerle ele alın.",
        "notebooklm_prompts_en": "A spirited debate dissecting the collapse of traditional resume screening: Contrasting the pedigree-obsessed corporate recruiter who hires confident mediocrities from elite schools, with an AI talent architect who uses blind skill simulations to discover extraordinary, unconventional operators.",
        "udemy_outline_tr": [
            "00:00 - CV Yalanları ve Diploma Tuzağı: Neden İşe Alımların %50'si Hatalıdır?",
            "04:50 - Beceri Odaklı (Skill-Based) İşe Alım Modeline Geçiş",
            "10:15 - Kör Değerlendirme (Blind Assessment) ile Bilişsel Önyargıları Yok Etmek",
            "16:20 - Canlı Uygulama: AI ile Bir Pozisyon İçin Gerçekçi İş Numunesi Testi Tasarlamak",
            "22:50 - Eylem Görevi: Kendi Takımın İçin Diploma Aramayan Beceri Rubriği Oluştur"
        ],
        "udemy_outline_en": [
            "00:00 - The Resume Farce: Why Half of Traditional Corporate Hires Fail",
            "04:50 - The Architectural Transition to Skill-Based Talent Acquisition",
            "10:15 - Blind Simulation Assessments: Neutralizing Gender, Age, and Pedigree Bias",
            "16:20 - Live Lab: Building an Objective Work Sample Evaluation Engine via AI",
            "22:50 - Action Assignment: Designing a Pedigree-Agnostic Talent Rubric for Your Team"
        ]
    },
    {
        "id": 27,
        "part_num": 6,
        "part_title_tr": "Bölüm 6: İnsan Kaynakları, Liderlik & Kültür (The Chief People Officer & Culture Builder)",
        "part_title_en": "Part 6: People, Culture & Organizational Architecture (The Chief People Officer & Culture Builder)",
        "lesson_num": 27,
        "level_tr": "Seviye 6: Organizasyonel Liderlik / Chief People Officer",
        "level_en": "Level 6: Organizational Leadership / Chief People Officer",
        "title_tr": "Ders 27: Hibrit ve Dağınık Takım Yönetimi: Asenkron İletişim, Psikolojik Güvenlik ve Şeffaflık",
        "title_en": "Lesson 27: Managing Distributed & Hybrid Teams: Asynchronous Culture & Psychological Safety",
        "summary_tr": "Çalışanları 8 saat ofisteki masalara kilitleyip ekranlarını gözetlemek liderlik değil, gardiyanlıktır. Dünyanın en başarılı modern organizasyonları; Zoom yorgunluğunu yok eden asenkron yazılı kültür, fikirlerin korkusuzca paylaşıldığı psikolojik güvenlik (Psychological Safety) ve yapay zeka ile otomatikleştirilmiş şeffaf bilgi akışı üzerine inşa edilir.",
        "summary_en": "Mandating seat-time in cubicles and tracking keystrokes is not leadership; it is digital prison management. The world's highest-velocity organizations reject meeting fatigue in favor of rigorous asynchronous documentation, radical transparency, and Amy Edmondson's psychological safety—empowered by AI meeting synthesizers that turn team discussions into shared organizational intelligence.",
        "eli5_metaphor_tr": "Eski usul ofis yönetimi, bir sınıfın başında durup 'Kimse kıpırdamasın, herkes bana baksın!' diye bağıran bir öğretmene benzer. Modern asenkron takım yönetimi ise bir açık kaynak yazılım topluluğu veya Wikipedia gibidir: Dünyanın her yerindeki insanlar kendi en verimli oldukları saatte uyanır, ortak dijital tahtaya en iyi fikirlerini yazar ve sistem saat gibi tıkır tıkır işler.",
        "eli5_metaphor_en": "Legacy office management is an insecure teacher shouting in a classroom: 'Quiet! Keep your eyes on me for 8 hours!' Modern asynchronous leadership is like orchestrating an open-source movement or Wikipedia: World-class specialists across four continents contribute at their peak biological hours to a shared, transparent knowledge graph.",
        "comparison_table": [
            {
                "topic_tr": "İletişim Kültürü",
                "topic_en": "Communication Cadence",
                "old_way_tr": "Senkron Bağımlılığı: Her küçük soru için tüm takımı 45 dakikalık Zoom toplantısına kilitlemek.",
                "old_way_en": "Synchronous reflex: Forcing 8 people onto a 45-minute Zoom call for a 2-minute decision.",
                "ai_way_tr": "Asenkron Yazı Kültürü: Net yazılı dokümanlar (Notion/Slack) ve AI toplantı özetleri.",
                "ai_way_en": "Asynchronous-first: High-signal memos, clear decision frameworks, and automated AI transcripts."
            },
            {
                "topic_tr": "Güven ve Kontrol",
                "topic_en": "Trust & Accountability",
                "old_way_tr": "Gözetim Takıntısı: 'Kameran açık mı, Slack'te yeşil yanıyor musun?' paranoyası.",
                "old_way_en": "Surveillance paranoia: Tracking mouse movements, webcam status, and login hours.",
                "ai_way_tr": "Çıktı Odaklılık (Outcome-Based): Nerede ve ne zaman çalıştığın değil, ne ürettiğin önemlidir.",
                "ai_way_en": "Outcome-based trust: Total autonomy over schedules paired with strict accountability for outputs."
            },
            {
                "topic_tr": "Hata ve Fikir Güvenliği",
                "topic_en": "Psychological Safety",
                "old_way_tr": "Hata yapanı azarlayıp sindiren, insanların konuşmaktan korktuğu toksik hiyerarşi.",
                "old_way_en": "Blame-and-shame hierarchy where pointing out bad ideas is career suicide.",
                "ai_way_tr": "Psikolojik Güvenlik: Hataların şeffafça tartışıldığı 'Suçlamasız Otopsi' (Blameless Post-Mortem).",
                "ai_way_en": "Blameless Post-Mortems: Treating mistakes as systems failures to be dissected constructively."
            }
        ],
        "framework_steps_tr": [
            "1. 'Toplantı Olmayan Günler' (No-Meeting Days): Haftanın en az 2 gününü tamamen derin odaklanma (Deep Work) zamanı ilan et.",
            "2. Amazon Usulü 6 Sayfalık Not (Narrative Memo): Toplantılarda slayt okumayı yasakla; toplantının ilk 15 dakikasında hazırlanan yazılı brifingi sessizce okut.",
            "3. Suçlamasız Kriz Analizi (Blameless Post-Mortem): Bir hata olduğunda 'KİM yaptı?' diye değil, 'SİSTEM neden izin verdi?' diye sor.",
            "4. Asenkron Durum Güncellemeleri: Her sabah yapılan yorucu stand-up toplantılarını Slack/Teams üzerinden AI özetli metinlere dönüştür."
        ],
        "framework_steps_en": [
            "1. Institutionalize No-Meeting Focus Blocks: Protect at least two full business days weekly for uninterrupted deep cognitive output.",
            "2. The Narrative Memo Protocol: Ban slide-reading meetings; dedicate the first 15 minutes to silent reading of a structured AI-refined brief.",
            "3. Institute Blameless Post-Mortems: Shift language from 'Who screwed up?' to 'What gap in our automated guardrails permitted this failure?'",
            "4. Asynchronous Standups: Replace 30-minute status check-ins with automated Slack check-ins synthesized by AI bots into an executive dashboard."
        ],
        "case_study_tr": "50 yazılımcı ve ürün uzmanından oluşan küresel bir yazılım şirketi, haftada ortalama 26 saat toplantı yapıyordu. Çalışan tükenmişliği (burnout) tavan yapmış, teslimatlar sürekli gecikiyordu. Yeni lider ekibi radikal bir 'Asenkron Devrim' başlattı: Tüm durum toplantıları yasaklandı, yerine AI toplantı botu ve yazılı şablonlar getirildi. Kararlar 1 sayfalık dokümanlarla tartışıldı. Toplantı süresi haftada 4 saate indi. Çalışan memnuniyeti %80 artarken, şirketin sprint tamamlama hızı (velocity) tam %140 fırladı.",
        "case_study_en": "A 50-person distributed product engineering firm was suffocating under 26 hours of mandatory weekly video calls. Morale plummeted, voluntary departures hit 30%, and product releases stagnated. The incoming leadership team executed an immediate Asynchronous Reset: Abolished recurring status meetings, mandated asynchronous written memos, and deployed AI synthesis bots to catalog decision logs. Total meeting load collapsed from 26 hours to 3.5 hours weekly. Engineer engagement jumped by 80%, while quarterly feature velocity accelerated by 140%.",
        "ai_prompts": [
            {
                "title_tr": "Asenkron Kültür ve Suçlamasız Otopsi (Blameless Post-Mortem) Mimarı",
                "title_en": "Asynchronous Culture & Blameless Post-Mortem Engine",
                "prompt_tr": "Sen Amy Edmondson'ın Psikolojik Güvenlik ve Amazon'un Yazılı Kültür metodolojisinde uzmanlaşmış bir Organizasyonel Tasarımcısın. Şirketimizde yaşanan şu operasyonel krizi/hatayı ele al: [KRİZ VE HATA DETAYLARI]. 1) Hiçbir çalışanı suçlamadan, tamamen süreç ve sistem hatalarına odaklanan bir 'Suçlamasız Otopsi Raporu' (Blameless Post-Mortem) hazırla, 2) Ekipte psikolojik güvenliği artıracak bir geri bildirim dili tasarla, 3) 1 saatlik Zoom toplantısını ortadan kaldıracak tek sayfalık asenkron karar dokümanı yaz.",
                "prompt_en": "Act as an elite Organizational Culture Architect trained in Amy Edmondson's Psychological Safety and GitLab's remote protocols. For this operational catastrophe: [INSERT FAILURE LOGS]: 1) Structure a rigorous Blameless Post-Mortem memo isolating systemic architectural vulnerabilities without finger-pointing, 2) Draft an empathetic leadership framing script that models vulnerability and learning, 3) Convert the issue into a 1-page asynchronous decision memo that eliminates the need for an emergency video call."
            }
        ],
        "notebooklm_prompts_tr": "İki şirket lideri: Biri çalışanların evdeki kameralarını gözetleyip günde 8 saat Zoom toplantısı dayatan kontrol manyağı eski nesil patron, diğeri asenkron yazılı kültür ve psikolojik güvenlikle dünyanın dört bir yanından inanılmaz bir verim çıkaran modern lider. 'Toplantı cehenneminden kurtuluş: Asenkron çalışmanın ve güvenin gücü' konusunu mizahi ve ilham verici bir diyalogla dinleyin.",
        "notebooklm_prompts_en": "A hilarious yet profoundly instructive debate on workplace sanity: Contrasting an insecure micromanager who equates productivity with glowing green Slack bubbles, with an asynchronous remote leader who delivers 3x more output by killing 90% of meetings and cultivating deep psychological safety.",
        "udemy_outline_tr": [
            "00:00 - Zoom Yorgunluğu ve Dijital Gardiyanlığın İflası",
            "04:50 - Amy Edmondson'ın Psikolojik Güvenlik (Psychological Safety) Modeli",
            "10:15 - Asenkron Çalışmanın 3 Altın Kuralı: Yazı, Şeffaflık, Güven",
            "16:20 - Canlı Uygulama: Hataları Güce Dönüştüren Suçlamasız Otopsi (Blameless Post-Mortem)",
            "22:50 - Eylem Görevi: Gelecek Hafta İçin Takımında 'Toplantısız Odak Günü' İlan Et"
        ],
        "udemy_outline_en": [
            "00:00 - The Pathology of Video Fatigue: Why Digital Surveillance Fails",
            "04:50 - Engineering Psychological Safety: Amy Edmondson's Blueprint",
            "10:15 - The Core Pillars of Asynchronous Cadence: Written Memos and Transparency",
            "16:20 - Live Lab: Structuring an Exhaustive Blameless Post-Mortem via AI",
            "22:50 - Action Assignment: Establishing a Protected No-Meeting Deep Work Day"
        ]
    },
    {
        "id": 28,
        "part_num": 6,
        "part_title_tr": "Bölüm 6: İnsan Kaynakları, Liderlik & Kültür (The Chief People Officer & Culture Builder)",
        "part_title_en": "Part 6: People, Culture & Organizational Architecture (The Chief People Officer & Culture Builder)",
        "lesson_num": 28,
        "level_tr": "Seviye 6: Organizasyonel Liderlik / Chief People Officer",
        "level_en": "Level 6: Organizational Leadership / Chief People Officer",
        "title_tr": "Ders 28: Performans Yönetimi ve OKR Mimarisi: Yılda Bir Değerlendirmeden Sürekli AI Geribildirimine",
        "title_en": "Lesson 28: Modern Performance Architecture: Continuous AI Feedback & Dynamic OKR Alignment",
        "summary_tr": "Yılda bir kez yapılan ve herkesin sahte gülücüklerle birbirine not verdiği o hantal 'Yıllık Performans Değerlendirmeleri' resmi bir komedidir. John Doerr'ın Hedefler ve Temel Sonuçlar (OKR) çerçevesini yapay zeka ile dinamikleştirerek; şirket hedeflerini haftalık yaşayan organizmalara dönüştürün ve çalışanlara anlık, gelişim odaklı geribildirim sağlayın.",
        "summary_en": "The annual corporate performance appraisal—where managers assign arbitrary 1-to-5 numbers based on recency bias—is a demotivating farce. By modernizing John Doerr's Objectives and Key Results (OKRs) with continuous AI feedback loops, organizations align strategic priorities in real-time, replacing annual trauma with weekly micro-coaching.",
        "eli5_metaphor_tr": "Yılda bir performans değerlendirmesi yapmak, bir futbol maçında teknik direktörün 90 dakika boyunca kenarda sessizce oturup maç bittikten ve takım 5-0 yenildikten sonra soyunma odasına girip futbolculara '3 ay önceki pasta niye koşmadın?' diye bağırmasına benzer. Dinamik OKR ise sahanın kenarında her pozisyonda taktik fısıldayan akıllı bir koçtur.",
        "eli5_metaphor_en": "Annual performance reviews are like a soccer coach sitting silently with his arms crossed for 90 minutes, watching his team lose 5-0, and then storming the locker room to scream: 'Why did you miss that pass in the 12th minute?' Dynamic OKRs are real-time tactical adjustments whispered into the player's earpiece after every single play.",
        "comparison_table": [
            {
                "topic_tr": "Değerlendirme Sıklığı",
                "topic_en": "Evaluation Frequency",
                "old_way_tr": "Yılda bir kez yapılan, herkesin gerildiği ve son 2 haftanın hatırlandığı formalite seansları.",
                "old_way_en": "Annual retrospective rituals dominated by recency bias and political anxiety.",
                "ai_way_tr": "Haftalık ve anlık mikro-geribildirim döngüleri (Continuous AI Coaching).",
                "ai_way_en": "Continuous weekly micro-feedback synthesizing work telemetry and peer recognition."
            },
            {
                "topic_tr": "Hedef Belirleme Modeli",
                "topic_en": "Goal Architecture",
                "old_way_tr": "Yukarıdan aşağıya dikte edilen, 6 ay sonra unutulan ve esnemeyen statik hedefler (MBO).",
                "old_way_en": "Top-down static targets buried in HR portals and ignored until December.",
                "ai_way_tr": "Dinamik, şeffaf ve ölçülebilir Çift Yönlü OKR'lar (Objectives & Key Results).",
                "ai_way_en": "Bi-directional OKRs: Ambitious Objectives anchored to quantifiable, auditable Key Results."
            },
            {
                "topic_tr": "Liderin Rolü",
                "topic_en": "Managerial Role",
                "old_way_tr": "Not veren, ceza kesen ve yargılayan bir 'müfettiş' gibi davranmak.",
                "old_way_en": "Acting as a punitive judge handing down arbitrary salary grades.",
                "ai_way_tr": "Çalışanın önündeki blokajları kaldıran ve gelişimine rehberlik eden bir 'koç'.",
                "ai_way_en": "An empowering multiplier coach whose primary role is clearing path friction."
            }
        ],
        "framework_steps_tr": [
            "1. Hedef (Objective) ile Temel Sonucu (Key Result) Ayır: Hedef ilham verici ve nitel olmalı ('Sektörün en güvenilir mobil bankası olmak'); Key Result ise sert bir rakam içermeli ('Uptime oranını %99.98'e çıkarmak').",
            "2. Gerilimli Hedefler (Stretch Goals): OKR'larda %100 başarı hedefi koyma; %70 başarı oranı hedefin yeterince cesur olduğunu gösterir.",
            "3. Haftalık Check-In Rutini: Cuma günleri 15 dakikalık ritüel: 'Bu hafta OKR'ımıza ne kadar yaklaştık, önümüzdeki blokaj ne?'",
            "4. 360 Derece Sürekli Geri Bildirim: Performansı tek bir yöneticinin keyfine bırakma; yapay zeka ile projelerdeki iş birliği kalitesini analiz et."
        ],
        "framework_steps_en": [
            "1. Architect Qualitative Objectives & Quantitative KRs: Objectives inspire ('Dominate cloud security'); Key Results measure numerically ('Hit 0 breaches and $5M ARR').",
            "2. Calibrate Stretch Thresholds: If a team hits 100% of their OKRs every quarter, the goals were cowardice; 70-80% completion reflects optimal stretch.",
            "3. The Friday OKR Pulse: A 15-minute weekly reflection reviewing metric velocity and unblocking cross-functional dependencies.",
            "4. Decouple Coaching from Compensation: Separate ongoing capability feedback from formal compensation resets to preserve psychological safety."
        ],
        "case_study_tr": "Geleneksel bir perakende şirketinde çalışanların yıllık değerlendirmeleri 2 ay sürüyordu; İK departmanı binlerce form topluyor ama şirket hedefleri %40 oranında şaşıyordu. Yeni liderlik, John Doerr OKR modelini ve AI destekli bir iç geri bildirim asistanını devreye aldı. Şirketin ana hedefi 'E-ticarette sipariş teslimat süresini 48 saatten 4 saate indirmek' olarak netleştirildi. Tüm departmanlar kendi Key Result'larını bu hedefe bağladı. Çalışanlar her Cuma 2 dakikada durum girdi; sistem aksayan noktaları otomatik işaretledi. 6 ay içinde teslimat süresi 3.5 saate indi ve ciro %65 arttı.",
        "case_study_en": "A 1,000-employee omnichannel retailer wasted 60 days every autumn completing 10-page appraisal forms, while missing corporate revenue targets by 40%. The Chief People Officer replaced the legacy process with John Doerr OKRs driven by an automated feedback bot. The company's north star was crystallized: 'Compress same-day delivery from 48 hours to 4 hours.' Every team engineered three contributing Key Results. Teams submitted a 2-minute weekly check-in via AI prompts. Operational friction dropped instantly. Delivery speed hit 3.5 hours within two quarters, driving a 65% digital sales surge.",
        "ai_prompts": [
            {
                "title_tr": "John Doerr OKR Mimarı ve Dinamik Koçluk Motoru",
                "title_en": "John Doerr OKR Architect & Continuous Coaching Engine",
                "prompt_tr": "Sen John Doerr'ın 'Measure What Matters' metodolojisinde uzmanlaşmış bir Stratejik OKR Koçusun. Şirketimizin/departmanımızın şu vizyonunu ele al: [ŞİRKET VİZYONU VEYA PROJE]. 1) Bu vizyon için 1 adet ilham verici Hedef (Objective) ve 3 adet ölçülebilir, sert rakam içeren Temel Sonuç (Key Result) yaz, 2) Bu OKR'ların başarı puanını (0.0 - 1.0) ölçecek puanlama baremini belirle, 3) Yöneticilerin çalışanlarına haftalık 1-on-1 görüşmelerde soracağı 3 güçlü koçluk sorusu hazırla.",
                "prompt_en": "Act as an executive OKR Architect trained by John Doerr (Measure What Matters framework). For this strategic corporate priority: [INSERT INITIATIVE]: 1) Engineer one inspiring, qualitative Objective paired with three numerically auditable Key Results, 2) Establish explicit grading boundaries (0.0 to 1.0 scoring scale), 3) Formulate three high-leverage coaching questions for weekly manager check-ins that surface hidden blockers."
            }
        ],
        "notebooklm_prompts_tr": "İki yönetici: Biri yıl sonu gelince personeline 1'den 5'e kadar not verip herkesi küstüren eski usul İK müdürü, diğeri dinamik OKR'lar ve sürekli AI koçluğuyla takımını her hafta şampiyonlar ligi finaline hazırlar gibi motive eden modern lider. 'Yıllık performans değerlendirmelerinin ölümü ve yaşayan OKR kültürü' konusunu ilham verici bir sohbetle dinleyin.",
        "notebooklm_prompts_en": "A dynamic podcast discussion breaking down the failure of annual performance grading: Contrasting the hated annual review with real-time OKR alignment and continuous AI micro-coaching that inspires teams to achieve 10x ambitious outcomes.",
        "udemy_outline_tr": [
            "00:00 - Yıllık Değerlendirme Komedisi: Neden Kimse Bu Formlara İnanmaz?",
            "04:50 - John Doerr ve 'Önemli Olanı Ölç' (Measure What Matters) Felsefesi",
            "10:15 - Hedef (Objective) vs. Temel Sonuç (Key Result): Altın Kurallar",
            "16:20 - Canlı Uygulama: AI ile Şirket Vizyonunu Departman OKR'larına Bölmek",
            "22:50 - Eylem Görevi: Kendi Rolün İçin Gelecek Çeyreğin 3 Temel Sonucunu Yaz"
        ],
        "udemy_outline_en": [
            "00:00 - The Farce of the Annual Review: Why Employees Dread Year-End Appraisals",
            "04:50 - John Doerr's Measure What Matters: The Philosophical Core of OKRs",
            "10:15 - Distinguishing Qualitative Objectives from Quantitative Key Results",
            "16:20 - Live Lab: Cascading Enterprise Strategy into Team-Level OKR Trees via AI",
            "22:50 - Action Assignment: Writing Three High-Conviction Key Results for Your Quarter"
        ]
    },
    {
        "id": 29,
        "part_num": 6,
        "part_title_tr": "Bölüm 6: İnsan Kaynakları, Liderlik & Kültür (The Chief People Officer & Culture Builder)",
        "part_title_en": "Part 6: People, Culture & Organizational Architecture (The Chief People Officer & Culture Builder)",
        "lesson_num": 29,
        "level_tr": "Seviye 6: Organizasyonel Liderlik / Chief People Officer",
        "level_en": "Level 6: Organizational Leadership / Chief People Officer",
        "title_tr": "Ders 29: Kurum İçi Öğrenme ve Tersine Mentorluk: Çalışanları AI Destekli Süper Güçlerle Donatmak",
        "title_en": "Lesson 29: Continuous Organizational Learning: Upskilling Teams into AI Centaurs",
        "summary_tr": "Yapay zeka işleri insanların elinden almayacak; ancak yapay zekayı bir uzvu gibi kullanan insanlar (Centaurs ve Cyborgs), kullanmayanların işini elinden alacak. Şirket içi eğitimleri sıkıcı video portallarından kurtarın; genç yeteneklerin kıdemli yöneticileri eğittiği Tersine Mentorluk (Reverse Mentoring) ve AI çalışma kulüpleri ile tüm organizasyonu bilişsel bir süper güce dönüştürün.",
        "summary_en": "AI will not replace executives; executives who master human-machine symbiosis will replace those who do not. The modern enterprise culture is an AI Centaur academy—where half the cognitive load is borne by human intuition and half by machine intelligence. By instituting Reverse Mentoring and generative sandbox dojos, organizations turn every employee into a 10x operator.",
        "eli5_metaphor_tr": "Yapay zekayı öğrenmek, satrançtaki 'Kentavr' (Yarı insan, yarı at) oyuncularına benzer. Tek başına en iyi insan satranç ustası bilgisayara yenilir, tek başına bilgisayar da bazen sezgiden yoksundur. Ama vasat bir insan satranç oyuncusu yanına iyi bir yapay zeka motoru alırsa, dünyanın en büyük büyükustasını bile tahtadan siler. Şirketini işte bu Kentavr ordusuna dönüştürmelisin!",
        "eli5_metaphor_en": "Becoming an AI Centaur is like chess master Garry Kasparov's advanced chess: A lone human grandmaster loses to supercomputers, and a computer lacks creative contextual audacity. But an average player seamlessly paired with an AI engine beats the world's most powerful supercomputer. Your job as a leader is building a company of Centaurs.",
        "comparison_table": [
            {
                "topic_tr": "Eğitim ve Gelişim Modeli",
                "topic_en": "Learning Philosophy",
                "old_way_tr": "Yılda bir kez zorunlu tutulan, arkada sessizde oynatılan sıkıcı e-öğrenme videoları.",
                "old_way_en": "Boring compliance e-learning modules clicked through on mute once a year.",
                "ai_way_tr": "İş üstünde deneysel öğrenme: Haftalık AI hackathonları ve gerçek vaka çözümleri.",
                "ai_way_en": "Weekly sandbox hackathons and real-time operational workflow re-engineering.",
                "ai_way_tr": "Haftalık AI hackathonları, deneysel sandbox laboratuvarları ve gerçek vaka çözümleri."
            },
            {
                "topic_tr": "Bilgi Akış Yönü",
                "topic_en": "Knowledge Transmission",
                "old_way_tr": "Sadece yaşlı ve kıdemli yöneticilerin gençlere akıl verdiği tek yönlü hiyerarşi.",
                "old_way_en": "Unidirectional hierarchy where senior executives lecture junior staff.",
                "ai_way_tr": "Tersine Mentorluk (Reverse Mentoring): 22 yaşındaki stajyerin Yönetim Kuruluna prompt eğitimi vermesi.",
                "ai_way_en": "Reverse Mentoring: 22-year-old AI natives coaching the Executive Committee on agent workflows."
            },
            {
                "topic_tr": "Çalışan Profili",
                "topic_en": "Workforce Capability",
                "old_way_tr": "Sadece tek bir alanda uzmanlaşmış ve yeni teknolojilere direnen dar uzmanlar.",
                "old_way_en": "Siloed specialists who guard their narrow domain and resist automation.",
                "ai_way_tr": "AI Centaur: Kendi uzmanlığını yapay zeka çarpanıyla birleştirerek 10x değer üreten melez profesyoneller.",
                "ai_way_en": "The AI Centaur: T-shaped generalist-specialists orchestrating tools to multiply cognitive throughput."
            }
        ],
        "framework_steps_tr": [
            "1. Kurum İçi AI Sandbox Kur: Çalışanların şirket verisini tehlikeye atmadan özgürce deney yapabileceği güvenli bir kurumsal AI ortamı sağla.",
            "2. Tersine Mentorluk Eşleşmesi: Her C-Suite yöneticisine haftada 1 saat AI araçlarını uygulamalı gösteren genç bir mentor ata.",
            "3. En İyi Prompt Yarışmaları (Prompt Dojos): Departmanlar arasında en yaratıcı zaman kazandıran iş akışını ödüllendir ve kütüphaneye ekle.",
            "4. Bilişsel Çarpan Metriği: Her çalışanın çeyreklik hedeflerine 'Kendi işinde en az 1 süreci yapay zeka ile %50 hızlandırma' şartı koy."
        ],
        "framework_steps_en": [
            "1. Deploy an Enterprise AI Sandbox: Provide secure, privacy-compliant LLM environments where teams experiment without data leak risks.",
            "2. Launch Reverse Mentoring Pairings: Pair every VP with an early-career AI native for bi-weekly 45-minute hands-on tool sparring sessions.",
            "3. Institutionalize Prompt Dojos: Run monthly cross-departmental showcases awarding teams that automate high-friction operational tasks.",
            "4. The Cognitive Multiplier Metric: Include in quarterly goals an explicit requirement to 2x the velocity of at least one core workflow via AI."
        ],
        "case_study_tr": "120 yıllık köklü bir sigorta şirketinde 50 yaş üzeri kıdemli aktüerler ve yöneticiler yapay zekaya mesafeli duruyor, 'Bizim tecrübemizin yerini hiçbir makine tutamaz' diyordu. Şirketin yeni İK lideri 'Tersine Mentorluk' programı başlattı. Yeni mezun 15 genç analist, şirket direktörleriyle birebir eşleştirildi. Gençler yöneticilere karmaşık poliçe analizlerini ve regülasyon özetlerini AI ile nasıl 10 dakikada çıkardıklarını bizzat kendi bilgisayarlarında gösterdi. 3 ay sonra en şüpheci direktör bile günlük brifinglerini AI ile almaya başladı; şirketin yeni ürün çıkarma süresi 9 aydan 6 haftaya indi.",
        "case_study_en": "A 100-year-old insurance conglomerate faced deep cultural inertia among veteran actuaries who dismissed generative technology as a gimmick. The Chief People Officer instituted a mandatory Reverse Mentoring program, pairing 20 young technical associates with Executive Vice Presidents. During weekly 1-on-1 labs, the associates guided the executives through real-world risk modeling using custom LLMs. Witnessing their own workload compressed from 8 hours to 15 minutes, executive resistance dissolved. Within two quarters, cross-functional AI adoption reached 85%, compressing new policy launch cycles from 9 months to 6 weeks.",
        "ai_prompts": [
            {
                "title_tr": "Kurum İçi AI Dönüşüm ve Tersine Mentorluk Mimarı",
                "title_en": "Enterprise AI Upskilling & Reverse Mentoring Program Architect",
                "prompt_tr": "Sen dünyanın en büyük teknoloji şirketlerinde Kurumsal Öğrenme ve Gelişim Direktörüsün (Head of L&D). Şirketimizdeki çalışanların teknolojiye direnç gösterdiği şu departmanı ele al: [DEPARTMAN VE ÇALIŞAN PROFİLİ]. 1) Bu ekibi 60 gün içinde 'AI Centaur' seviyesine çıkaracak 4 haftalık uygulamalı bir eğitim atölyesi müfredatı hazırla, 2) Kıdemli yöneticilerle genç yetenekleri eşleştiren bir Tersine Mentorluk rehberi yaz, 3) Çalışanların gizli şirket sırlarını modele kaptırmasını önleyecek temel Güvenlik İlkelerini (AI Safety SOP) belirle.",
                "prompt_en": "Act as a Chief Learning Officer designing an enterprise capability transformation. For this change-resistant department: [INSERT DEPARTMENT PROFILE]: 1) Structure a 4-week experiential 'AI Centaur' masterclass curriculum anchored to real operational workflows, 2) Draft an actionable charter for a Reverse Mentoring pairing program between junior AI natives and senior VPs, 3) Formulate clear data governance guardrails preventing confidential IP leaks into public models."
            }
        ],
        "notebooklm_prompts_tr": "İki şirket yöneticisi: Biri yeni teknolojilerden korkup çalışanlarının yapay zeka kullanmasını yasaklayan paranoid eski kafalı patron, diğeri 'Tersine Mentorluk' ile 22 yaşındaki stajyerlerden prompt dersi alan ve şirketini bilişsel bir süper güce dönüştüren bilge CEO. 'Yapay zekanın iş dünyasında yarattığı Kentavr devrimi ve kurum içi öğrenme' üzerine nefes kesici bir sohbet yapın.",
        "notebooklm_prompts_en": "A lively, visionary podcast discussing the Centaur workforce: Why banning AI in the office is corporate suicide, and how progressive enterprises use Reverse Mentoring to turn traditional executive teams into agile, machine-augmented operators.",
        "udemy_outline_tr": [
            "00:00 - Korkunun Sonu: AI İnsanların Yerini Değil, Alışkanlıkların Yerini Alır",
            "04:50 - Kentavr (Centaur) ve Kiborg (Cyborg) Çalışma Modelleri",
            "10:15 - Tersine Mentorluk: Stajyerlerin Yönetim Kurulunu Eğitme Sanatı",
            "16:20 - Canlı Uygulama: Şirket İçi Prompt Dojo ve Hackathon Tasarımı",
            "22:50 - Eylem Görevi: Bu Hafta Ekibinden Birine Yeni Bir AI Aracını Öğret"
        ],
        "udemy_outline_en": [
            "00:00 - Beyond the Fear: AI Does Not Replace Humans, It Replaces Obsolete Habits",
            "04:50 - The Theory of Cognitive Symbiosis: Centaurs vs. Cyborg Operators",
            "10:15 - Reverse Mentoring: Empowering Digital Natives to Coach the C-Suite",
            "16:20 - Live Lab: Designing a High-Energy Corporate Prompt Dojo",
            "22:50 - Action Assignment: Upskilling a Colleague on an AI Workflow This Week"
        ]
    },
    {
        "id": 30,
        "part_num": 6,
        "part_title_tr": "Bölüm 6: İnsan Kaynakları, Liderlik & Kültür (The Chief People Officer & Culture Builder)",
        "part_title_en": "Part 6: People, Culture & Organizational Architecture (The Chief People Officer & Culture Builder)",
        "lesson_num": 30,
        "level_tr": "Seviye 6: Organizasyonel Liderlik / Chief People Officer",
        "level_en": "Level 6: Organizational Leadership / Chief People Officer",
        "title_tr": "Ders 30: Değişim Yönetimi ve Kültürel Direnç: Yapay Zeka Korkusunu İnovasyon Heyecanına Dönüştürmek",
        "title_en": "Lesson 30: Leading Change Management: Overcoming AI Anxiety & Igniting a Culture of Innovation",
        "summary_tr": "Değişime direnmek insanın en temel biyolojik savunma mekanizmasıdır. 'Yapay zeka işimizi elimizden alacak' korkusuyla sistemleri sabote eden ekipleri zorla dönüştüremezsiniz. John Kotter'ın 8 Adımlı Değişim Modeli'ni empati ve psikolojik yeniden çerçeveleme ile birleştirerek; çalışanların korkularını dinleyin, erken zaferler (Quick Wins) yaratın ve yapay zekayı bir tehdit değil, sıkıcı işlerden kurtuluş bileti yapın.",
        "summary_en": "Resistance to change is not employee malice; it is primal evolutionary fear of irrelevance. You cannot mandate cultural transformation through executive decree. By operationalizing John Kotter's 8-Step Change Framework infused with deep psychological empathy, leaders transform systemic AI anxiety into shared mission enthusiasm—celebrating early wins that liberate human talent from administrative drudgery.",
        "eli5_metaphor_tr": "Bir insana 'Yarın senin arabanı alıp yerine elektrikli uçan bir kaykay vereceğiz' dersen korkar ve kaykayı tekmeleyip kırar. Ama 'Seni her sabah 2 saat trafikte bekleten o çileyi yok ediyoruz, bak bu düğmeye basınca hiç yorulmadan gökyüzünden süzülüp işine gidiyorsun ve ailenle 2 saat fazla vakit geçiriyorsun' dersen koşa koşa biner. Değişim yönetimi kaykayı değil, özgürlüğü satmaktır!",
        "eli5_metaphor_en": "If you walk into a medieval village and announce: 'We are confiscating your horses and giving you steam engines,' the villagers will burn the engines to the ground in terror. But if you demonstrate that the steam pump clears toxic water from their coal mine in 10 minutes so their children don't get sick, they will embrace the machine. Change management sells human liberation, not cold mechanics.",
        "comparison_table": [
            {
                "topic_tr": "Dönüşüm Yaklaşımı",
                "topic_en": "Transformation Stance",
                "old_way_tr": "Tepeden inme emirler: 'Pazartesiden itibaren herkes şu aracı kullanacak, yoksa sonuçlarına katlanır!'",
                "old_way_en": "Autocratic mandates: 'Everyone must use this software by Monday or face consequences.'",
                "ai_way_tr": "Empati ve İkna: Korkuları dinleyen, eğitici ve erken zaferlerle heveslendiren liderlik.",
                "ai_way_en": "Empathetic leadership: Listening to visceral fears, framing wins, and building coalition champions."
            },
            {
                "topic_tr": "Hata ve Deneme Alanı",
                "topic_en": "Experimental Leeway",
                "old_way_tr": "Yeni sistemde hata yapan çalışanı cezalandırıp eski alışkanlıklara geri kaçırtmak.",
                "old_way_en": "Penalizing operational hiccups during rollout, driving workers back to legacy spreadsheets.",
                "ai_way_tr": "Güvenli Hata Bölgesi: İlk 90 günde öğrenme hatalarını kutlayan açık kültür.",
                "ai_way_en": "Psychological safety buffers: Celebrating early implementation learnings during the first 90 days."
            },
            {
                "topic_tr": "Kazanımların Paylaşımı",
                "topic_en": "Surplus Sharing",
                "old_way_tr": "Otomasyonla artan verimliliği sadece personel çıkarmak (işten çıkarma) için kullanmak.",
                "old_way_en": "Using automation gains solely to slash headcount, proving the employees' worst fears right.",
                "ai_way_tr": "Verimlilik artışını çalışanlara daha az mesai, daha yaratıcı projeler ve ikramiye olarak yansıtmak.",
                "ai_way_en": "Re-investing productivity gains into higher strategic responsibilities, shorter hours, and bonuses."
            }
        ],
        "framework_steps_tr": [
            "1. Aciliyet Hissi Yarat (Sense of Urgency): Yapay zekaya geçmezsek şirketin ve hepimizin gelecekte nasıl geri kalacağını şeffafça anlat.",
            "2. Güçlü Bir Koalisyon Kur (Guiding Coalition): Sadece yöneticileri değil; şirket içinde sevilen, enerjik çalışanları 'Değişim Elçisi' yap.",
            "3. Erken Zaferler Üret (Quick Wins): İlk 30 günde çalışanların en nefret ettiği haftalık 5 saatlik angarya bir raporu AI ile 2 dakikaya indir.",
            "4. Yeni Normu Kültüre Çimentola: Başarı hikayelerini şirket toplantılarında kutla; yapay zeka ile işini kolaylaştıran çalışanları ödüllendir."
        ],
        "framework_steps_en": [
            "1. Establish Constructive Urgency: Clearly articulate the existential competitive risk of inertia without inducing paralysis.",
            "2. Form the Guiding Coalition: Recruit respected peer influencers across all seniority levels as frontline transformation champions.",
            "3. Engineer Immediate Short-Term Wins: Automate the single most universally hated clerical task within 30 days to build belief.",
            "4. Anchor Changes in Corporate DNA: Celebrate transformed workflows in all-hands meetings, publicly rewarding proactive automation architects."
        ],
        "case_study_tr": "1.500 çalışanlı bir bankada operasyon merkezine AI destekli belge tarama sistemi kurulacağı duyurulduğunda, çalışan sendikası ve personeller 'işsiz kalacağız' korkusuyla sistemi boykot etti; veri girişleri kasten geciktirildi. Durumu devralan Değişim Lideri, projeyi durdurdu ve tüm çalışanlarla empati toplantıları yaptı: 'Tek bir kişinin bile işine son verilmeyecek. Amacımız her gün akşama kadar fatura girmekten parmakları ağrıyan sizleri, müşterilere kredi danışmanlığı veren yüksek primli pozisyonlara taşımaktır.' İlk pilotta en çok şikayet eden 10 çalışan yeni sisteme geçirildi; mesaiye kalmadan prim kazandıkları görülünce tüm departman gönüllü olarak eğitime koştu.",
        "case_study_en": "A 1,500-employee banking operations center announced an automated document underwriting deployment, triggering widespread covert sabotage: Processing times spiked as terrified workers feared mass redundancies. The incoming Chief Change Officer intervened: Declared a written guarantee of zero layoffs and hosted town halls reframing the technology. 'Our mission is to emancipate you from mind-numbing data entry so you can step into high-commission relationship underwriting.' Ten vocal skeptics were placed on the pilot team. When their overtime evaporated while their bonuses increased by 30%, remaining departments clamored for immediate rollout.",
        "ai_prompts": [
            {
                "title_tr": "John Kotter Değişim Yönetimi ve Kültürel Direnç Kırıcı",
                "title_en": "John Kotter Change Architect & Resistance De-escalation Playbook",
                "prompt_tr": "Sen dünyanın en deneyimli Kurumsal Değişim Yönetimi ve Dönüşüm Liderisin (John Kotter metodolojisi). Şirketimizde hayata geçirmek istediğimiz şu yapay zeka projesine karşı ciddi bir çalışan direnci var: [DİRENÇ GÖSTERİLEN PROJE VE KORKULAR]. 1) Kotter'ın 8 Adımlı Değişim Modeli'ne dayanan 90 günlük bir Değişim Eylem Planı hazırla, 2) Çalışanların 'İşsiz kalacağız' korkusunu dindirecek, son derece samimi ve ikna edici bir Genel Müdür / Lider Konuşması (Townhall Speech) yaz, 3) İlk 30 günde çalışanların güvenini kazanacak 2 somut 'Erken Zafer' (Quick Win) belirle.",
                "prompt_en": "Act as an elite Corporate Transformation Architect trained in John Kotter's 8-Step Change Framework. Our enterprise faces acute internal resistance against this AI automation rollout: [INSERT PROJECT & EMPLOYEE FEARS]. 1) Construct a multi-phase 90-day Change Playbook dismantling resistance, 2) Script an authentic, deeply empathetic All-Hands Townhall Address delivered by the CEO that neutralizes job-loss panic, 3) Design two immediate 30-day Quick Wins that tangibly eliminate clerical drudgery for frontline operators."
            }
        ],
        "notebooklm_prompts_tr": "İki şirket lideri: Biri çalışanlarına zorla yeni yazılımlar dayatıp şirkette grev ve sabotaj başlatan otoriter eski patron, diğeri John Kotter metodolojisi ve derin insan empatisiyle çalışanların korkularını inovasyon coşkusuna dönüştüren bilge değişim mimarı. 'Değişimin psikolojisi: Korku nasıl aşılır ve insanlar yeni bir vizyona nasıl aşık edilir?' konusunu büyüleyici bir sohbetle dinleyin.",
        "notebooklm_prompts_en": "An extraordinary podcast exploring the psychology of enterprise transformation: Why humans resist technological change out of instinct, and how compassionate, strategic leaders turn corporate fear into a united, unstoppable innovation movement.",
        "udemy_outline_tr": [
            "00:00 - Neden Dönüşüm Projelerinin %70'i Kültürel Direnç Yüzünden Çöker?",
            "04:50 - İnsan Psikolojisi ve Değişim Korkusunun Evrimsel Kökenleri",
            "10:15 - John Kotter'ın 8 Adımlı Değişim Modeli ile Dönüşüm Yolculuğu",
            "16:20 - Canlı Uygulama: Şirket İçi Direnci Kıran Townhall Konuşması ve Erken Zaferler",
            "22:50 - Bölüm 6 Kapanış Sınavı: İnsan Kaynakları ve Liderlik Sertifikasyon Görevi"
        ],
        "udemy_outline_en": [
            "00:00 - The Graveyard of Transformation: Why 70% of Initiatives Die of Cultural Rejection",
            "04:50 - Evolutionary Neuroscience of Change Anxiety and Loss Aversion",
            "10:15 - Operationalizing John Kotter's 8-Step Framework in the AI Era",
            "16:20 - Live Lab: Scripting a De-escalating CEO Townhall & Quick-Win Milestone",
            "22:50 - Part 6 Capstone Project: People, Culture & Leadership Certification Challenge"
        ]
    }
]
