# -*- coding: utf-8 -*-
"""
AI-Driven MBA - Modules 03 & 04 (Lessons 11 - 20)
Part 3: Büyüme, Pazarlama & Müşteri Deneyimi (Growth, Marketing & Hyper-Personalization)
Part 4: Operasyonlar, Tedarik Zinciri & Yalın Süreçler (Operations, Supply Chain & Automation)
"""

LESSONS_11_20 = [
    # -------------------------------------------------------------
    # PART 3: BÜYÜME, PAZARLAMA & MÜŞTERİ DENEYİMİ (LESSONS 11-15)
    # -------------------------------------------------------------
    {
        "id": 11,
        "part_num": 3,
        "part_title_tr": "Bölüm 3: Büyüme, Pazarlama & Müşteri Deneyimi (The Growth & Marketing Director)",
        "part_title_en": "Part 3: Growth, Marketing & Hyper-Personalization (The Growth & Marketing Director)",
        "lesson_num": 11,
        "level_tr": "Seviye 3: Büyüme & Pazarlama / Growth Director",
        "level_en": "Level 3: Growth & Marketing / Growth Director",
        "title_tr": "Ders 11: AI Destekli Pazarlama Karması (4P'den 4E'ye): Kişiselleştirilmiş İçerik ve Otomasyon Motorları",
        "title_en": "Lesson 11: The Modern Marketing Engine: Moving from 4Ps to 4Es with Generative Marketing",
        "summary_tr": "1960'ların tek tip 'Product, Price, Place, Promotion' (4P) modeli, yapay zeka çağında yerini 'Experience, Exchange, Everyplace, Evangelism' (4E) mimarisine bıraktı. Milyonlarca müşteriye aynı reklamı göstermek yerine, her bireyin anlık ruh haline ve satın alma niyetine göre generatif içerik motorları kurun.",
        "summary_en": "The static 1960s 4Ps (Product, Price, Place, Promotion) have been superseded by the dynamic 4Es: Experience, Exchange, Everyplace, and Evangelism. Rather than broadcasting monolithic campaigns to passive audiences, modern growth directors deploy autonomous generative engines that synthesize personalized creative, copy, and timing for micro-segments of one.",
        "eli5_metaphor_tr": "Eski pazarlama, şehrin meydanına devasa bir megafon koyup avazı çıktığı kadar 'Bizim sabunumuz en iyisi!' diye bağırmaktır; binlerce kişi geçer, çoğu duymaz bile. Modern AI pazarlaması ise her geçen insanın yanına nazik bir rehber koyup, tam da onun cilt tipine ve sabahki ruh haline uygun ferahlatıcı sabunu özel bir tonda fısıldamaktır.",
        "eli5_metaphor_en": "Legacy marketing is parking a deafening megaphone in a town square screaming: 'Buy our toothpaste!' Generative AI marketing is a fleet of invisible, empathetic concierges who whisper the exact bespoke value proposition tailored to each commuter's immediate dental concern and aesthetic preference.",
        "comparison_table": [
            {
                "topic_tr": "Pazarlama Karması Felsefesi",
                "topic_en": "Marketing Paradigm",
                "old_way_tr": "Klasik 4P: Ürünü üret, fiyat koy, dükkana koy, TV'de tanıt.",
                "old_way_en": "Legacy 4Ps: Product, Price, Place, Promotion—broadcasted monolithically.",
                "ai_way_tr": "Modern 4E: Deneyim yaşat, değer takası yap, her yerde ol, elçi yarat.",
                "ai_way_en": "Modern 4Es: Experience, Exchange, Everyplace, Evangelism—hyper-personalized.",
                "ai_way_tr": "Modern 4E: Deneyim yaşat (Experience), Değer takası (Exchange), Her yerde ol (Everyplace), Sadık elçiler yarat (Evangelism)."
            },
            {
                "topic_tr": "Reklam Kreatifi & Metin Üretimi",
                "topic_en": "Creative Generation",
                "old_way_tr": "Reklam ajansına 3 ayda 2 adet TV filmi ve 3 afiş tasarlatıp dua etmek.",
                "old_way_en": "Hiring an agency for 3 months to deliver two TV commercials and three banner variants.",
                "ai_way_tr": "Yapay zeka ile günde 500 farklı görsel ve metin varyasyonu üretip anlık A/B testine sokmak.",
                "ai_way_en": "Algorithmic generation of 500 bespoke creative/copy variations tested dynamically across platforms."
            },
            {
                "topic_tr": "Segmentasyon Mantığı",
                "topic_en": "Segmentation Resolution",
                "old_way_tr": "'25-45 yaş arası şehirli kadınlar' gibi sığ ve kaba demografiler.",
                "old_way_en": "Crude demographic buckets like 'Urban males aged 25-40 with disposable income.'",
                "ai_way_tr": "Davranışsal mikro-segmentler: 'Son 48 saatte sepette ürün unutan ve kahve arayanlar'.",
                "ai_way_en": "Micro-intent cohorts: 'Users who abandoned carts twice at night and browse productivity blogs.'"
            }
        ],
        "framework_steps_tr": [
            "1. 4E Dönüşüm Matrisi: Şirketinin değer teklifini Ürün'den Deneyim'e, Promosyon'dan Savunuculuğa (Evangelism) tercüme et.",
            "2. Generatif Kreatif Fabrikası Kur: Temel marka renklerini ve tonunu Midjourney/Flux ve Claude modellerine 'System Prompt' olarak tanımla.",
            "3. Duygu ve Niyet Eşleştirmesi: Kullanıcının arama niyetine (Aciliyet, Merak, Fiyat Hassasiyeti) göre farklı landing page varyantları üret.",
            "4. Otonom Bütçe Tahsisi: ROAS (Reklam Harcaması Getirisi) düşen kanallardan bütçeyi otomatik çekip kazanan varyanta aktaran kurallar belirle."
        ],
        "framework_steps_en": [
            "1. Transpose into the 4Es: Reframe offerings from static Products into immersive Experiences and Promotions into organic Evangelism.",
            "2. Deploy the Generative Creative Matrix: Anchor brand design guidelines and tonal tokens into prompt templates to generate variations at zero marginal cost.",
            "3. Real-Time Dynamic Landing Pages: Map visitor acquisition source and intent directly to custom modular hero sections and social proofs.",
            "4. Closed-Loop Performance Allocation: Automate capital re-allocation toward creative assets delivering the highest net ROAS."
        ],
        "case_study_tr": "Bir online sigorta platformu, 'Kasko Yaptırın' başlıklı standart Facebook reklamlarıyla tıklama başı 45 TL ödüyor ve %1.2 dönüşüm alıyordu. Yeni Büyüme Direktörü, AI ile kitleyi 12 farklı yaşam evresine böldü: 'Yeni bebeği olan anneler', 'Yeni spor araba alan gençler', 'Emekliliğinde karavan alanlar'. Her kitleye özel 40 farklı görsel ve hikaye üretti. 'Bebeğinizi taşırken içiniz rahat olsun' varyantı tıklama maliyetini 8 TL'ye düşürdü ve kasko satışlarını %340 artırdı.",
        "case_study_en": "An online auto insurance provider was bleeding ad spend with generic 'Get Covered Today' banners yielding a depressing 1.2% conversion rate at $3.20 CPC. The incoming Growth Director leveraged generative workflows to segment campaigns into 12 micro-cohorts (e.g., 'First-time parents buying SUVs', 'Vintage roadster hobbyists'). Deploying bespoke emotional creatives cut customer acquisition costs by 68% and tripled closed policy volume in 60 days.",
        "ai_prompts": [
            {
                "title_tr": "Modern Pazarlama Karması (4E) ve Hiper-Kişiselleştirme Motoru",
                "title_en": "The 4E Modern Marketing Matrix & Dynamic Creative Engine",
                "prompt_tr": "Sen dünyanın en yenilikçi Baş Pazarlama Yöneticisisin (CMO). Şu ürünü ele al: [ÜRÜN BİLGİSİ]. 1) Klasik 4P yaklaşımını modern 4E (Experience, Exchange, Everyplace, Evangelism) çerçevesine dönüştür, 2) Bu ürün için 3 farklı radikal tüketici mikro-segmenti tanımla, 3) Her segment için yüksek dönüşüm getirecek Instagram/LinkedIn reklam metni, görsel promptu ve kanca (hook) cümlesi yaz.",
                "prompt_en": "Act as an avant-garde Chief Marketing Officer. For this product: [INSERT PRODUCT DETAILS]: 1) Transpose legacy 4P thinking into the modern 4E framework (Experience, Exchange, Everyplace, Evangelism), 2) Define three non-obvious micro-intent buyer cohorts, 3) Formulate high-converting ad copy hooks, psychological triggers, and Midjourney image prompts for each cohort."
            }
        ],
        "notebooklm_prompts_tr": "İki pazarlamacı: Biri hâlâ televizyona devasa bütçeler gömüp neyin işe yaradığını bilmeyen 'Mad Men' tarzı eski nesil reklamcı, diğeri ise yapay zekayla saniyeler içinde 500 kişiselleştirilmiş kampanya türeten hiper-büyüme direktörü. 'Kişiselleştirilmiş pazarlamanın gücü ve 4P'nin ölümü' konusunu mizahi ve bol örnekli bir diyalogla tartışın.",
        "notebooklm_prompts_en": "A comedic clash between a vintage 'Mad Men' style creative director who relies on gut feeling and three-martini lunches, and an AI-driven performance marketing architect who optimizes thousands of dynamic creative variants before breakfast. Break down the true shift from 4P broadcast to 4E hyper-personalization.",
        "udemy_outline_tr": [
            "00:00 - Kotler'ın 4P'sine Saygı Duruşu ve 4E Devriminin Doğuşu",
            "04:40 - Müşteri Segmentasyonunun Sonu: Tek Kişilik Mikro-Kitleler",
            "10:15 - AI Destekli Generatif Reklam Fabrikası Kurulumu",
            "16:20 - Canlı Uygulama: 15 Dakikada 10 Farklı Kitle İçin Kampanya Seti Oluşturmak",
            "22:30 - Eylem Görevi: Şirketinin Bir Ürününü 4E Modeliyle Yeniden Pazara Sun"
        ],
        "udemy_outline_en": [
            "00:00 - Deconstructing Philip Kotler: The Historical Pivot to the 4Es",
            "04:40 - The End of Broad Demographics: Engineering Micro-Intent Cohorts",
            "10:15 - Orchestrating an Autonomous Generative Creative Engine",
            "16:20 - Live Lab: Generating 10 Bespoke Multi-Channel Campaigns in 15 Minutes",
            "22:30 - Action Assignment: Rebuilding Your Acquisition Funnel via the 4E Framework"
        ]
    },
    {
        "id": 12,
        "part_num": 3,
        "part_title_tr": "Bölüm 3: Büyüme, Pazarlama & Müşteri Deneyimi (The Growth & Marketing Director)",
        "part_title_en": "Part 3: Growth, Marketing & Hyper-Personalization (The Growth & Marketing Director)",
        "lesson_num": 12,
        "level_tr": "Seviye 3: Büyüme & Pazarlama / Growth Director",
        "level_en": "Level 3: Growth & Marketing / Growth Director",
        "title_tr": "Ders 12: Büyüme Korsanlığı (Growth Hacking) & Viral Döngüler: A/B Testlerinden Otonom Optimizasyona",
        "title_en": "Lesson 12: Modern Growth Hacking: From Manual A/B Tests to Autonomous Multi-Armed Bandits",
        "summary_tr": "Statik A/B testlerinde iki buton rengini yarıştırıp 3 hafta beklemek büyüme korsanlığı değildir. Modern büyüme mimarisi; kendi kendine optimize olan 'Multi-Armed Bandit' algoritmaları, ürün içi teşvik döngüleri (viral loops) ve yapay zeka ile kullanıcıyı anında marka elçisine dönüştüren tavsiye sistemleridir.",
        "summary_en": "Waiting 3 weeks for an inconclusive 50/50 A/B button test is growth amateurism. High-velocity growth engineering leverages reinforcement learning Multi-Armed Bandit algorithms, algorithmic referral engines, and self-reinforcing viral loops that compound compounding network effects autonomously.",
        "eli5_metaphor_tr": "Eski usul A/B testi, bir kumarhanede iki kollu makinenin önüne geçip 1.000 kez kol çekerek hangisinin daha çok kazandırdığını deftere not etmektir. Otonom yapay zeka ise hangi makinenin daha çok para verdiğini ilk 50 çekişte anlayıp, cebindeki paranın %90'ını hemen o kazanan makineye yatıran akıllı bir robottur.",
        "eli5_metaphor_en": "Traditional A/B testing is pulling two slot machines 1,000 times each while blindly tracking losses on a notepad. A Multi-Armed Bandit algorithm is an intelligent card-counter: Within 50 pulls it detects which machine pays out 3x more and dynamically routes 95% of your chips to the winner while continuing to explore.",
        "comparison_table": [
            {
                "topic_tr": "Test Metodolojisi",
                "topic_en": "Testing Methodology",
                "old_way_tr": "Klasik A/B Testi: Trafiği %50/%50 bölüp haftalarca istatistiksel anlamlılık beklemek.",
                "old_way_en": "Static 50/50 A/B split: Burning ad spend on losing variants for weeks.",
                "ai_way_tr": "Multi-Armed Bandit & Bayesian AI: Kazanan varyanta trafiği anında dinamik kaydırmak.",
                "ai_way_en": "Multi-Armed Bandit reinforcement models that route traffic dynamically to outperforming assets."
            },
            {
                "topic_tr": "Viral Katsayı (K-Faktörü)",
                "topic_en": "Viral Coefficient (K-Factor)",
                "old_way_tr": "Sayfanın en altına 'Arkadaşına öner' linki koyup tıklanmasını umut etmek.",
                "old_way_en": "Slapping a generic 'Share with friends' footer link and hoping for virality.",
                "ai_way_tr": "Çift taraflı değer kurgusu (Dropbox tarzı) ve yapay zeka ile doğru anda tetiklenen mikro ödüller.",
                "ai_way_en": "Engineered two-sided viral loops triggered at peak dopamine moments with calibrated incentives."
            },
            {
                "topic_tr": "Huni Optimizasyonu Hızı",
                "topic_en": "Funnel Optimization Cadence",
                "old_way_tr": "Ayda 1 veya 2 büyüme deneyi yapabilen yavaş toplantı kültürü.",
                "old_way_en": "Running 1 or 2 sluggish experiments per month bogged down by committee politics.",
                "ai_way_tr": "Haftada 20 otonom mikro-hipotez deneyip sonuçları hızla ölçekleyen büyüme motoru.",
                "ai_way_en": "A continuous algorithmic growth cadence executing 20+ concurrent hypotheses every sprint."
            }
        ],
        "framework_steps_tr": [
            "1. Viral Döngü Mimarisini Kur: K-Faktörü formülünü hesapla (K = Davet Sayısı x Dönüşüm Oranı). K > 1 ise ürün kendi kendine büyür!",
            "2. Dopamin Zirvesini Yakala: Müşteriye davet teklifini rastgele değil, üründe ilk büyük başarısını kutladığı 'Aha Moment' anında fırlat.",
            "3. Otonom Bandit Algoritması Devreye Al: Başlık, fiyat etiketi ve CTA butonlarını statik bırakma; yapay zekanın trafiği en iyi varyanta akıtmasını sağla.",
            "4. ICE Puanlama Matrisi ile Önceliklendir: Etki (Impact), Güven (Confidence), Kolaylık (Ease) skorunu AI ile tartarak en hızlı kazanımları seç."
        ],
        "framework_steps_en": [
            "1. Architect the Core Viral Loop: Model the K-factor equation (K = Invites Sent * Conversion Rate). If K > 1, growth is self-sustaining.",
            "2. Anchor on Dopamine Highs: Trigger user referral prompts exclusively at the verified 'Aha Moment' when emotional satisfaction peaks.",
            "3. Deploy Multi-Armed Bandit Telemetry: Dynamically route landing page variations based on live Bayesian conversion probabilities.",
            "4. Operationalize the ICE Matrix: Rank backlog growth experiments across Impact, Confidence, and Ease using generative decision scoring."
        ],
        "case_study_tr": "B2B fatura mutabakat yazılımı üreten bir girişim, LinkedIn reklamlarına ayda 30.000 $ harcıyor ama müşteri başına 450 $ ödüyordu. Büyüme lideri, viralliği ürünün merkezine koydu: Bir şirket tedarikçisine faturayı gönderdiğinde, tedarikçiye 'Bu faturayı tek tıkla onaylamak ve kendi faturalarınızı da ücretsiz takip etmek için tıklayın' daveti gitti. Bu akıllı B2B viral döngüsü sayesinde her 1 müşteri sisteme ortalama 3.4 yeni şirket getirdi (K-Faktörü = 3.4). Reklam bütçesi sıfırlandı, şirket 8 ayda 12.000 aktif KOBİ'ye ulaştı.",
        "case_study_en": "A B2B invoice reconciliation platform was burning $30,000/month on LinkedIn ads with an unsustainable $450 CAC. The growth engineer embedded a bilateral network loop: When a client dispatched an invoice, the counterparty vendor received a 1-click reconciliation link alongside a prompt: 'Settle in 1-click and reconcile your own vendor bills for free.' This engineered B2B loop generated a viral K-factor of 3.4. Paid marketing was zeroed out as the platform organically onboarded 12,000 enterprises in 8 months.",
        "ai_prompts": [
            {
                "title_tr": "Büyüme Korsanı: Viral Döngü ve K-Faktörü Tasarımcısı",
                "title_en": "Growth Hacker: Viral Loop Architecture & ICE Experiment Engine",
                "prompt_tr": "Sen Sean Ellis ve Andrew Chen kalibresinde bir Büyüme Korsanlığı (Growth Hacking) Uzmanısın. Şu iş modelini analiz et: [İŞ MODELİ VE HEDEF KİTLE]. 1) Ürünün içine organik olarak gömülebilecek, K-Faktörünü 1'in üzerine çıkaracak 2 adet viral döngü (viral loop) tasarla, 2) Kullanıcının en mutlu olduğu 'Aha Moment' anını ve bu anda sunulacak karşı konulamaz teklifi yaz, 3) Gelecek hafta test edebileceğimiz, ICE puanı en yüksek 3 büyüme deneyini tablo halinde listele.",
                "prompt_en": "Act as an elite Growth Engineering Partner (Andrew Chen / Sean Ellis caliber). For this venture: [INSERT BUSINESS MODEL & AUDIENCE]: 1) Engineer two embedded product-led viral loops capable of driving a K-factor > 1.0, 2) Pinpoint the psychological 'Aha Moment' and design the exact transactional hook, 3) Formulate the top three high-velocity experiments ranked by ICE score (Impact, Confidence, Ease)."
            }
        ],
        "notebooklm_prompts_tr": "İki büyüme uzmanı: Biri haftalarca süren anlamsız A/B testlerinde buton rengi tartışan geleneksel analist, diğeri ürünün içine viral nükleer döngüler kurup şirketi organik olarak patlatan büyüme korsanı. 'A/B testlerinin ölümü, Multi-Armed Bandit algoritmaları ve viral katsayının sırları' üzerine ufuk açıcı bir tartışma yapın.",
        "notebooklm_prompts_en": "A provocative, masterclass-level podcast between two growth leaders: Deconstructing why 80% of corporate A/B testing is vanity theater, and illustrating how Multi-Armed Bandit models and viral loops turn everyday software products into self-propagating enterprise flywheels.",
        "udemy_outline_tr": [
            "00:00 - Büyüme Korsanlığı Nedir, Ne Değildir? Buton Rengi Mitleri",
            "04:30 - K-Faktörünün Matematiği: Ürünü Kendi Kendine Satan Güç",
            "10:00 - A/B Testlerinden Multi-Armed Bandit Algoritmalarına Geçiş",
            "15:45 - Canlı Vaka: B2B Bir Süreci Viral Bir Büyüme Makinesine Dönüştürmek",
            "21:50 - Eylem Görevi: Kendi Ürünün İçin ICE Öncelikli Büyüme Deneyi Hazırla"
        ],
        "udemy_outline_en": [
            "00:00 - Growth Hacking Demystified: Shattering the Button-Color Myth",
            "04:30 - The Mechanics of the K-Factor: Building Self-Propagating Software",
            "10:00 - Reinforcement Learning in Marketing: Multi-Armed Bandits Explained",
            "15:45 - Live Case Study: Engineering a 3.4 K-Factor Loop in Enterprise Tech",
            "21:50 - Action Assignment: Designing Your 7-Day ICE Experiment Backlog"
        ]
    },
    {
        "id": 13,
        "part_num": 3,
        "part_title_tr": "Bölüm 3: Büyüme, Pazarlama & Müşteri Deneyimi (The Growth & Marketing Director)",
        "part_title_en": "Part 3: Growth, Marketing & Hyper-Personalization (The Growth & Marketing Director)",
        "lesson_num": 13,
        "level_tr": "Seviye 3: Büyüme & Pazarlama / Growth Director",
        "level_en": "Level 3: Growth & Marketing / Growth Director",
        "title_tr": "Ders 13: Müşteri Yaşam Boyu Değeri (LTV) ve CAC Optimizasyonu: Yapay Zeka ile Müşteri Edinme Stratejisi",
        "title_en": "Lesson 13: Unit Economics Mastery: LTV/CAC Optimization with Predictive AI",
        "summary_tr": "Birim ekonomi (Unit Economics), şirketlerin ölüm kalım çizgisidir. LTV/CAC oranı 3'ün altında olan her şirket iflasa doğru koşar. Yapay zeka destekli tahminleyici LTV modellemesi ve mikro-kanal CAC atıf (attribution) sistemleri ile en kârlı müşteri dilimlerini hedefleyip sermaye verimliliğini zirveye taşıyın.",
        "summary_en": "Unit economics are the immutable physics of enterprise survival. Any company running an LTV/CAC ratio below 3.0 is subsidized vaporware marching toward insolvency. By deploying predictive AI lifetime value models and multi-touch algorithmic attribution, growth leaders ruthlessly purge toxic customer cohorts and compound capital efficiency.",
        "eli5_metaphor_tr": "Bir elma bahçesi işlettiğini düşün. Bir elmayı dalından koparmak için harcadığın para (CAC) 10 TL ise, o elmayı pazarda ancak 8 TL'ye (LTV) satabiliyorsan; her sattığın elma seni zengin etmez, batırır! Birim ekonomi, harcadığın 1 TL'nin sana en az 3 TL olarak geri döndüğünden emin olmaktır.",
        "eli5_metaphor_en": "Imagine operating an apple orchard where picking an apple costs $10 in labor (CAC), but the market only pays you $8 (LTV). Selling one million apples doesn't make you a unicorn; it makes you bankrupt at scale. Mastering unit economics guarantees that every single dollar planted returns at least three dollars harvested.",
        "comparison_table": [
            {
                "topic_tr": "Birim Ekonomi Ölçümü",
                "topic_en": "Unit Economic Rigor",
                "old_way_tr": "Toplam ciroyu toplam müşteri sayısına bölüp yüzeysel ortalamalarla avunmak.",
                "old_way_en": "Dividing aggregate revenue by total signups, completely blinded by blended averages.",
                "ai_way_tr": "Kohort bazlı mikro-LTV ve kanallara göre net marjlı CAC hesaplaması.",
                "ai_way_en": "Cohort-specific predictive LTV and fully burdened granular CAC tracking per channel."
            },
            {
                "topic_tr": "Atıf Modellemesi (Attribution)",
                "topic_en": "Attribution Architecture",
                "old_way_tr": "İlkel 'Son Tıklama' (Last-Click) atfı ile müşteriyi getiren asıl kanalları görememek.",
                "old_way_en": "Naive last-click attribution giving 100% credit to the final retargeting banner.",
                "ai_way_tr": "Yapay zeka çok temaslı (Multi-Touch) Shapley değer modeliyle her temasın gerçek etkisini ölçmek.",
                "ai_way_en": "AI multi-touch Shapley-value models that mathematically credit every brand touchpoint."
            },
            {
                "topic_tr": "Geri Ödeme Süresi (Payback)",
                "topic_en": "CAC Payback Period",
                "old_way_tr": "CAC geri ödeme süresinin 18 ayı aşmasını dert etmeyip sürekli nakit yakmak.",
                "old_way_en": "Tolerating an 18-month payback period while recklessly burning venture runway.",
                "ai_way_tr": "Akıllı peşin ödeme teşvikleri ve upsell modelleriyle payback süresini 6 ayın altına çekmek.",
                "ai_way_en": "Compressing CAC payback to <6 months using predictive annual discount bundling and upsell triggers."
            }
        ],
        "framework_steps_tr": [
            "1. LTV/CAC Sağlık Kontrolü Yap: Oran < 1 ise battın; 1-3 arası kırılgansın; 3-5 arası mükemmel altın orandasın; > 5 ise pazarlamaya az para harcıyorsun demektir!",
            "2. CAC Payback Süresini Hesapla: Bir müşteriyi kazanmak için harcanan para kaç ayda geri dönüyor? (Hedef: 6-12 ay).",
            "3. Toksik Müşterileri AI ile Ayıkla: Sürekli indirim kodu kovalayan, destek ekibini kilitleyen ve ilk ayda giden müşterileri edinme kanallarından derhal çıkar.",
            "4. Erken Genişleme (Expansion MRR): Müşteriye 3. ayında otomatik AI önerileriyle ek özellik satarak LTV'yi organik olarak büyüt."
        ],
        "framework_steps_en": [
            "1. Execute the LTV/CAC Diagnostic: <1.0 is terminal hemorrhage; 1.0-3.0 is fragile; 3.0-5.0 is the venture sweet spot; >5.0 means under-investing in acquisition.",
            "2. Compress the Payback Horizon: Force CAC payback under 12 months (ideally <6 months) to finance growth from operational cash flow.",
            "3. Identify & Purge Toxic Cohorts: Run cluster analyses to identify low-LTV, high-support-ticket users and negate bidding on their source keywords.",
            "4. Engineer Net Negative Churn: Drive Expansion MRR through automated usage milestones to push Net Revenue Retention (NRR) above 120%."
        ],
        "case_study_tr": "Abonelik kutusu satan bir kahve girişimi, Instagram fenomenlerine para yağdırarak 10.000 abone topladı. Kurucu ciroyla övünüyordu ancak şirket her ay 50.000 $ nakit kaybediyordu. Yeni CFO, AI ile birim ekonomiyi inceledi: Müşteri edinme maliyeti (CAC) 180 TL iken, ortalama bir müşteri 1.8 kutu alıp aboneliği bırakıyordu (LTV = 140 TL). Şirket her kazandığı müşteride 40 TL zarar ediyordu! Strateji derhal değiştirildi: 'İlk kutu bedava' kampanyası iptal edildi, 6 aylık peşin taahhütlü paket çıkarıldı. CAC 90 TL'ye düştü, LTV 380 TL'ye çıktı ve şirket 60 günde kârlılığa geçti.",
        "case_study_en": "A direct-to-consumer specialty coffee subscription scaled to 10,000 subscribers through aggressive influencer sponsorships, yet burned $50k monthly in cash. A forensic unit economic audit revealed the fatal flaw: Blended CAC was $65, but average customer lifetime was only 1.8 months due to heavy discounting, generating an LTV of merely $48. Every new customer evaporated $17. The growth director scrapped the discount bait, introduced curated 6-month seasonal subscriptions with pre-paid commitments, and deployed predictive flavor matching. CAC fell to $38, LTV leaped to $145, and net operating cash turned positive.",
        "ai_prompts": [
            {
                "title_tr": "Birim Ekonomi ve LTV/CAC Kârlılık Cerrahı",
                "title_en": "Unit Economics & LTV/CAC Forensic Surgeon",
                "prompt_tr": "Sen girişim sermayesi fonunda (VC) en katı Büyüme ve Finans Ortağısın. Aşağıdaki birim ekonomi metriklerini incele: [CAC, LTV, CHURN ORANI, BRÜT MARJ, PAYBACK SÜRESİ]. 1) Bu şirketin finansal ölüm riskini analiz et ve LTV/CAC oranını yorumla, 2) Payback süresini 6 aya indirmek için uygulanabilecek 3 fiyatlama ve ödeme stratejisi sun, 3) Pazarlama ekibinin bütçesini çöpe attığı en olası kaçak noktasını teşhis et.",
                "prompt_en": "Act as a ruthless General Partner at a top-tier venture firm specializing in SaaS/D2C unit economics. Dissect these operational metrics: [INSERT CAC, LTV, CHURN, GROSS MARGIN, PAYBACK]. 1) Deliver an unvarnished post-mortem on unit economic viability, 2) Formulate three concrete monetization interventions to compress the CAC payback window to <6 months, 3) Identify the leaky marketing funnel point where ad capital is being incinerated."
            }
        ],
        "notebooklm_prompts_tr": "İki finans ve pazarlama yöneticisi: Biri cirosuyla övünüp arka planda batmakta olan bir şirketin kurucusu, diğeri LTV/CAC dengesini bir cerrah gibi yönetip her kuruşun hesabını bilen deneyimli bir büyüme direktörü. 'Birim ekonomi yalanları: Ciro bir makyajdır, kârlılık ise gerçeğin ta kendisi' konusunu çarpıcı bir dille masaya yatırın.",
        "notebooklm_prompts_en": "A gripping boardroom debate between a growth executive drunk on top-line revenue growth, and a battle-hardened Chief Revenue Officer who proves the company loses $15 on every customer it acquires. Explore why mastering LTV/CAC unit economics is the difference between an enduring enterprise and a venture catastrophe.",
        "udemy_outline_tr": [
            "00:00 - Ciro İllüzyonu: Neden Büyürken Batabilirsiniz?",
            "05:00 - LTV ve CAC Matematiğinin Temelleri: 3x Kuralı",
            "10:45 - CAC Payback Süresi Neden Nakit Akışının Kalbidir?",
            "16:30 - Canlı Uygulama: AI ile Bir Şirketin Birim Ekonomisini Röntgenlemek",
            "22:15 - Eylem Görevi: Kendi Şirketinin Gerçek LTV/CAC Oranını Hesapla"
        ],
        "udemy_outline_en": [
            "00:00 - The Revenue Vanity Trap: How Scaling Can Accelerate Bankruptcy",
            "05:00 - The Mathematical Core of LTV and Granular CAC: The Golden 3x Ratio",
            "10:45 - Why CAC Payback Period Governs Corporate Runway and Survival",
            "16:30 - Live Lab: Conducting an AI Forensic Audit of Broken Unit Economics",
            "22:15 - Action Assignment: Calculating True Segmented LTV/CAC for Your Business"
        ]
    },
    {
        "id": 14,
        "part_num": 3,
        "part_title_tr": "Bölüm 3: Büyüme, Pazarlama & Müşteri Deneyimi (The Growth & Marketing Director)",
        "part_title_en": "Part 3: Growth, Marketing & Hyper-Personalization (The Growth & Marketing Director)",
        "lesson_num": 14,
        "level_tr": "Seviye 3: Büyüme & Pazarlama / Growth Director",
        "level_en": "Level 3: Growth & Marketing / Growth Director",
        "title_tr": "Ders 14: Omnichannel & AI Müşteri Destek Sistemleri: Otonom Agentlar ile 7/24 Kesintisiz Marka Deneyimi",
        "title_en": "Lesson 14: Omnichannel Customer Experience: Deploying Autonomous Support Agents with Brand Empathy",
        "summary_tr": "Müşterileri 45 dakika telefonda bekletip 'Tüm temsilcilerimiz meşguldür' dedirten şirketler çağ dışı kaldı. Modern omnichannel mimarisi; WhatsApp'tan e-postaya tüm temas noktalarında müşteri geçmişini hatırlayan, karmaşık sorunları insan empatisiyle çözen ve ilk temasta çözüm oranını %85'e çıkaran otonom AI ajanlarıdır.",
        "summary_en": "Subjecting high-value customers to 45 minutes of elevator music and robotic hold menus is corporate brand suicide. Next-generation omnichannel architectures deploy contextual autonomous agents that maintain memory across voice, WhatsApp, and webchat—resolving 85% of complex tier-1 and tier-2 tickets with human-grade empathy in seconds.",
        "eli5_metaphor_tr": "Eski usul çağrı merkezi, bir devlet dairesinde elinde evrakla kapı kapı dolaşıp her memura derdini baştan anlatmaya benzer. AI destekli omnichannel sistem ise binanın kapısından girdiğin anda adını, derdini ve en son ne zaman çay içtiğini bilen, seni hiç bekletmeden işini halleden özel bir asistan gibidir.",
        "eli5_metaphor_en": "Legacy customer service is like visiting a dystopian bureaucracy where you must wait in four separate lines, retell your entire medical history to three hostile clerks, and get disconnected. AI omnichannel support is having a personal concierge who recognizes your voice instantly, knows your exact purchase history, and resolves the refund before you finish typing.",
        "comparison_table": [
            {
                "topic_tr": "Destek Yanıt Süresi",
                "topic_en": "First Response Time",
                "old_way_tr": "E-postalara 24-48 saat sonra dönmek, çağrılarda 30 dakika bekletmek.",
                "old_way_en": "Answering support tickets within 24-48 hours and keeping callers on hold for 30 minutes.",
                "ai_way_tr": "Ortalama 3 saniyede kişiselleştirilmiş, çözüm odaklı anlık yanıt.",
                "ai_way_en": "Sub-3-second contextual response across all channels simultaneously 24/7/365."
            },
            {
                "topic_tr": "Kanal Geçiş Hafızası",
                "topic_en": "Cross-Channel Memory",
                "old_way_tr": "WhatsApp'tan yazan müşterinin web sitesindeki geçmişinden bihaber olmak.",
                "old_way_en": "Complete amnesia: Webchat, WhatsApp, and call center operate in isolated data silos.",
                "ai_way_tr": "Tekil Müşteri Görünümü (Single Customer View): Tüm temas geçmişini birleştiren vektör hafıza.",
                "ai_way_en": "Unified semantic customer memory: The agent recalls past tickets, sentiment, and cart actions."
            },
            {
                "topic_tr": "Problem Çözme Gücü",
                "topic_en": "Resolution Capability",
                "old_way_tr": "Sadece hazır SSS cevaplarını kopyalayıp yapıştıran aptal sohbet botları (rule-based chatbots).",
                "old_way_en": "Dumb rule-based bots that loop endlessly through static FAQ links and infuriate users.",
                "ai_way_tr": "API çağrısı yapıp iade oluşturan, kargo güncelleyen ve indirim tanımlayan yetkili AI ajanları.",
                "ai_way_en": "Agentic tool-calling: Executing refunds, re-booking flights, and updating CRM records autonomously."
            }
        ],
        "framework_steps_tr": [
            "1. Destek Biletlerini (Tickets) Kümele: Gelen talepleri 3 seviyeye ayır (Seviye 1: Rutin SSS, Seviye 2: İşlem/API Yetkisi Gerektiren, Seviye 3: Yüksek Empati/İnsan Gerektiren).",
            "2. RAG ve Bilgi Bankası Temizliği: Şirketin tüm iade, kargo ve kullanım kılavuzlarını AI'ın semantik arayabileceği temiz bir vektör veritabanına yükle.",
            "3. Duygu Dedektörü ve İnsana Devir (Human Handoff): Müşteri sinirlendiğinde veya hakaret ettiğinde AI'ın tartışmaya girmeden durumu derhal kıdemli temsilciye aktarmasını sağla.",
            "4. CSAT ve Çözüm Takibi: Her konuşmanın sonunda AI ile anlık müşteri memnuniyetini (CSAT) ölç ve aksayan süreçleri operasyona raporla."
        ],
        "framework_steps_en": [
            "1. Tri-Tier Ticket Classification: Segment incoming tickets into Tier 1 (Informational RAG), Tier 2 (Actionable API execution), and Tier 3 (High-Empathy Human Escalation).",
            "2. Vectorized Knowledge Grounding: Ingest all return policies, warranty rules, and SOPs into clean semantic knowledge bases with guardrails.",
            "3. Sentiment Guardrails & Seamless Escalation: Detect rising frustration scores instantly and route the call to a human supervisor with full conversational context.",
            "4. Continuous CSAT Telemetry: Automatically score emotional sentiment shifts from greeting to resolution to flag defective internal workflows."
        ],
        "case_study_tr": "Büyük bir havayolu şirketi, kış fırtınasında 80 uçuşun iptal olmasıyla saatte 15.000 çağrı aldı. Telefon santrali çöktü, müşteriler havalimanında isyan çıkardı. Şirketin yeni dijital deneyim lideri, 2 saat içinde GPT-4 tabanlı bir WhatsApp Ajanı devreye aldı. Ajan, yolcunun bilet kodunu alıp PNR sistemine bağlanıyor, bir sonraki uygun uçuşu teklif ediyor ve onaylayana yeni biniş kartını 45 saniyede PDF olarak yolluyordu. Gece boyunca 11.200 yolcunun transferi sıfır insan müdahalesiyle çözüldü; şirketin kriz yönetimi uluslararası basında övgü topladı.",
        "case_study_en": "A major European carrier experienced 80 blizzard cancellations, triggering an avalanche of 15,000 inbound distress calls per hour that collapsed the telephony switches. The VP of Customer Experience deployed an emergency WhatsApp autonomous agent integrated via APIs into the flight reservation system. Travelers inputted their booking reference; the agent verified identity, analyzed available routing options, re-booked alternative seats, and dispatched new digital boarding passes in under 45 seconds. Over 11,200 stranded passengers were re-accommodated overnight with zero human rep intervention.",
        "ai_prompts": [
            {
                "title_tr": "Marka Elçisi Düzeyinde Omnichannel Destek Ajanı Promptu",
                "title_en": "Empathetic Omnichannel Support Agent & De-escalation Protocol",
                "prompt_tr": "Sen lüks bir e-ticaret markasının Baş Müşteri Deneyimi Temsilcisisin. Karşında siparişi 4 gün geciktiği için aşırı öfkeli bir müşteri var: [MÜŞTERİ MESAJI]. 1) Müşterinin öfkesini yatıştıracak, samimi, özür dileyen ama ezilmeyen son derece profesyonel bir yanıt yaz, 2) Şirket politikası gereği müşteriye 100 TL hediye çeki tanımla ve kargonun şu anki konumunu açıkla, 3) Bu olayın bir daha tekrarlanmaması için operasyon ekibine yazılacak iç sistem notunu hazırla.",
                "prompt_en": "Act as the Principal Customer Experience Concierge for an ultra-luxury consumer brand. You are addressing an enraged customer whose $1,200 anniversary gift was delayed: [INSERT CUSTOMER MESSAGE]. 1) Formulate a deeply empathetic, de-escalating response that takes immediate personal ownership, 2) Execute an automatic $100 concierge credit and clarify the live courier dispatch status, 3) Generate an internal incident ticket for the logistics team diagnosing the root cause."
            }
        ],
        "notebooklm_prompts_tr": "İki müşteri deneyimi yöneticisi: Biri müşteriyi dakikalarca bekletip sinir krizine sokan klasik çağrı merkezi müdürü, diğeri yapay zeka ajanlarıyla WhatsApp'tan 10 saniyede problemi çözüp müşteriye çiçek yollayan yeni nesil deneyim mimarı. 'Müşteri hizmetlerinin geleceği: Robotik ses bantlarından empati sahibi yapay zeka ajanlarına' konusunu eğlenceli örneklerle işleyin.",
        "notebooklm_prompts_en": "A vivid, comedic dialogue contrasting the torture of legacy corporate IVR menus ('Press 1 for endless hold') with modern autonomous agent swarms that resolve complex logistics disputes in thirty seconds. Unpack how exceptional customer resolution is the highest-ROI retention engine in business.",
        "udemy_outline_tr": [
            "00:00 - Çağrı Merkezlerinin Ölümü ve Bekleme Müziği İşkencesi",
            "04:50 - Kural Tabanlı Botlar vs. Otonom LLM Ajanları",
            "10:30 - Tekil Müşteri Görünümü (Single Customer View) ve Vektör Hafıza",
            "16:40 - Canlı Uygulama: Müşteri Öfkesini Dindiren ve API Çağıran Destek Ajanı Kurulumu",
            "22:55 - Eylem Görevi: Kendi Şirketinin En Zor Destek Senaryosunu AI ile Çöz"
        ],
        "udemy_outline_en": [
            "00:00 - The Extinction of the IVR Menu: Ending the Hold-Music Nightmare",
            "04:50 - Rule-Based Chatbots vs. Autonomous Agentic Tool-Calling",
            "10:30 - Unified Semantic Memory & The Single Customer Profile",
            "16:40 - Live Lab: Designing an Empathetic Autonomous Support Workflow",
            "22:55 - Action Assignment: Building a De-escalation & Refund Agent"
        ]
    },
    {
        "id": 15,
        "part_num": 3,
        "part_title_tr": "Bölüm 3: Büyüme, Pazarlama & Müşteri Deneyimi (The Growth & Marketing Director)",
        "part_title_en": "Part 3: Growth, Marketing & Hyper-Personalization (The Growth & Marketing Director)",
        "lesson_num": 15,
        "level_tr": "Seviye 3: Büyüme & Pazarlama / Growth Director",
        "level_en": "Level 3: Growth & Marketing / Growth Director",
        "title_tr": "Ders 15: Marka Kimliği, İtibar ve Kriz İletişimi: Sosyal Duygu Analizi (Sentiment Analysis) ile Kriz Önleme",
        "title_en": "Lesson 15: Brand Equity & Crisis Management: Real-Time Social Listening & Generative Response",
        "summary_tr": "Bir şirketin 50 yılda inşa ettiği marka itibarı, sosyal medyada patlayan tek bir kriz videosuyla 2 saatte yerle bir olabilir. Yapay zeka tabanlı gerçek zamanlı duygu analizi (sentiment analysis) radarları kurarak; yangın büyümeden dumanı tespit edin ve şeffaf, ikna edici kriz iletişimini dakikalar içinde yürütün.",
        "summary_en": "Brand equity accumulated over 50 years can be decimated in 120 minutes by a viral social media storm. By instituting 24/7 AI-powered semantic sentiment listening grids, modern marketing directors detect early acoustic smoke before the corporate blaze erupts, mobilizing transparent, bulletproof crisis responses in minutes.",
        "eli5_metaphor_tr": "Kriz yönetimi, mutfakta küçük bir tava tutuştuğunda yangın söndürücüyü hemen sıkmak gibidir. Eski şirketler yangın söndürücüyü ararken oturup 3 gün basın bülteni yazar ve bu sırada tüm ev kül olur. AI kriz iletişimi ise duman çıktığı anda alarm çalıp tavayı kapağıyla kapatan akıllı yangın sistemidir.",
        "eli5_metaphor_en": "Crisis management is extinguishing a kitchen pan fire the moment it sparks. Traditional corporations spend three days in legal committees drafting an evasive press release while the entire mansion burns to the ground. AI crisis response is an automated ceiling sprinkler that snuffs the flame in thirty seconds and airs out the smoke.",
        "comparison_table": [
            {
                "topic_tr": "Kriz Algılama Hızı",
                "topic_en": "Crisis Detection Latency",
                "old_way_tr": "Kriz ana haber bültenine düşene kadar yöneticilerin hiçbir şeyden haberdar olmaması.",
                "old_way_en": "Finding out about a PR disaster when the national news anchor calls your CEO.",
                "ai_way_tr": "Twitter, Reddit ve TikTok'ta duygu skoru negatifleştiği ilk 15 dakikada gelen AI uyarısı.",
                "ai_way_en": "Algorithmic anomaly alerts within 15 minutes of an abnormal negative sentiment spike."
            },
            {
                "topic_tr": "İletişim Tonu & Yanıt",
                "topic_en": "Response Posture",
                "old_way_tr": "Hukuk departmanının yazdığı soğuk, duygusuz ve inkar eden resmi açıklamalar.",
                "old_way_en": "Cold, evasive, legalistic statements that blame victims and fan public outrage.",
                "ai_way_tr": "Samimi, sorumluluk alan, şeffaf ve somut düzeltici eylemleri anlatan insan odaklı iletişim.",
                "ai_way_en": "Authentic, empathetic ownership detailing immediate, auditable corrective actions."
            },
            {
                "topic_tr": "İtibar İyileştirme",
                "topic_en": "Reputational Recovery",
                "old_way_tr": "Olayın unutulmasını bekleyip aylarca kafayı kuma gömmek.",
                "old_way_en": "Burying heads in the sand and hoping the internet forgets about the scandal.",
                "ai_way_tr": "Etkilenen kitlelere özel telafi programları ve proaktif itibar onarım kampanyaları başlatmak.",
                "ai_way_en": "Deploying micro-targeted reconciliation campaigns and transparent progress dashboards."
            }
        ],
        "framework_steps_tr": [
            "1. 7/24 Duygu Radarı Kur: Marka adı ve ürün anahtar kelimelerindeki duygu polaritesini (pozitif/negatif) anlık izle.",
            "2. Kriz Sınıflandırması Yap: Seviye 1 (Tekil şikayet), Seviye 2 (Yerel viral potansiyel), Seviye 3 (Varoluşsal marka tehdidi).",
            "3. 60 Dakika Protokolü: Kriz anında ilk 1 saat içinde özür dile, hatayı kabul et ve araştırma komisyonu kurduğunu açıkla.",
            "4. Şeffaflık Bülteni (Living Document): Sürecin nasıl düzeltildiğini gün be gün kamuoyuyla paylaşan şeffaf bir canlı takip sayfası aç."
        ],
        "framework_steps_en": [
            "1. Establish 24/7 Sentiment Telemetry: Monitor semantic brand sentiment velocity across social and news APIs.",
            "2. Triage Severity Tiers: Differentiate between Tier 1 (Isolated troll), Tier 2 (Emerging regional viral cluster), and Tier 3 (Existential brand breach).",
            "3. Execute the Golden Hour Protocol: Within 60 minutes, issue an authentic leadership statement taking ownership and establishing an immediate audit.",
            "4. Publish a Live Remediation Dashboard: Provide public, milestone-driven updates showing exact operational fixes implemented."
        ],
        "case_study_tr": "Organik bebek maması üreten bir gıda markasının ürününden küçük bir plastik parçası çıktığını iddia eden bir annenin TikTok videosu 4 saatte 1.5 milyon izlendi. Şirketin PR ajansı 'Pazartesiye kadar bekleyelim' dedi. Büyüme ve Marka Direktörü beklemeyi reddetti; AI kriz asistanını kullanarak CEO'nun ağzından 30 dakika içinde bir video metni hazırladı. CEO bizzat kameranın karşısına geçti: 'Bir anne olarak dehşete düştüm. O partideki tüm ürünleri tedbiren geri çağırıyoruz, tesislerimizi bağımsız denetçilere açıyoruz ve aileyle bizzat görüşüyorum.' Bu cesur ve hızlı açıklama sayesinde boykot çağrıları durdu; marka güven endeksi kriz öncesinin bile üzerine çıktı.",
        "case_study_en": "A viral TikTok video claiming a microplastic fragment was found inside an organic baby food pouch gathered 1.5M views in 4 hours. The legacy PR counsel recommended waiting over the weekend. The Brand Director immediately drafted a raw, unvarnished crisis address with an AI executive simulator. The CEO recorded a direct video within an hour: 'As a parent, I am appalled. We are proactively issuing a voluntary recall for the entire lot, halting production, and inviting independent laboratory testing.' The swift, radical transparency inverted the narrative—trust scores ended 12% higher post-crisis than pre-crisis.",
        "ai_prompts": [
            {
                "title_tr": "Kriz İletişimi ve Yönetici Basın Açıklaması Simülatörü",
                "title_en": "Executive Crisis Communications & Hostile Stakeholder Simulator",
                "prompt_tr": "Sen dünyanın en deneyimli Kriz Yönetimi Danışmanısın (Edelman kriz ekibi kalibresinde). Şirketimiz şu skandalla karşı karşıya: [KRİZ DETAYLARI]. 1) Sosyal medyadaki öfkeyi dindirecek, asla savunmaya geçmeyen, samimi ve kurumsal sorumluluk alan bir CEO Basın Açıklaması yaz, 2) Gazetecilerin ve influencerların soracağı en tuzak 3 soruya verilecek 'altın standart' cevapları hazırla, 3) Marka itibarını 30 günde onaracak 3 somut eylemi listele.",
                "prompt_en": "Act as a Senior Crisis Communications Partner at a top global advisory firm. Our enterprise is facing this unfolding PR catastrophe: [INSERT CRISIS DETAILS]. 1) Draft an urgent, highly accountable CEO address that disarms public hostility without admitting unverified legal liability, 2) Script airtight responses to the three most hostile questions investigative journalists will ask, 3) Formulate a 30-day operational remediation roadmap to restore consumer confidence."
            }
        ],
        "notebooklm_prompts_tr": "İki kriz yönetimi uzmanı: Biri basına yalan söyleyip skandalı örtbas etmeye çalışırken şirketi batıran eski kafalı yönetici, diğeri şeffaflık, hız ve yapay zeka duygu analiziyle krizi devasa bir itibar zaferine çeviren modern iletişim lideri. 'Kriz anında hayatta kalma rehberi: Neden inkar öldürür, şeffaflık kurtarır?' konusunu nefes kesen örneklerle tartışın.",
        "notebooklm_prompts_en": "An intense, masterclass podcast dissecting corporate PR disasters: Contrasting the catastrophic cover-up instinct of legacy executives with modern transparent crisis resolution. Explore how algorithmic listening and radical authenticity neutralize social media mob psychology.",
        "udemy_outline_tr": [
            "00:00 - 2 Saatte 50 Yıllık Markayı Yok Eden Sosyal Medya Dinamikleri",
            "04:40 - Sosyal Duygu Analizi (Sentiment Analysis) ile Yangından Önce Dumanı Görmek",
            "10:15 - 'Altın Saat' Kuralı: Krizin İlk 60 Dakikasında Ne Yapılmalı?",
            "16:20 - Canlı Uygulama: CEO Kriz İletişimi Metni ve Tuzak Soru Simülasyonu",
            "22:40 - Bölüm 3 Kapanış Sınavı: Büyüme ve Müşteri Deneyimi Sertifikasyon Görevi"
        ],
        "udemy_outline_en": [
            "00:00 - How Decades of Brand Equity Can Evaporate in 120 Minutes",
            "04:40 - Deploying Semantic Sentiment Grids for Early Anomaly Detection",
            "10:15 - The Golden Hour Rule: What to Execute in the First 60 Minutes of a Crisis",
            "16:20 - Live Lab: Simulating Hostile Press Conferences with AI",
            "22:40 - Part 3 Capstone Project: Growth & Marketing Leadership Certification Exercise"
        ]
    },

    # -----------------------------------------------------------------
    # PART 4: OPERASYONLAR, TEDARİK ZİNCİRİ & YALIN SÜREÇLER (LESSONS 16-20)
    # -----------------------------------------------------------------
    {
        "id": 16,
        "part_num": 4,
        "part_title_tr": "Bölüm 4: Operasyonlar, Tedarik Zinciri & Yalın Süreçler (The Operations & Supply Chain Leader)",
        "part_title_en": "Part 4: Operations, Supply Chain & Automation (The Operations & Supply Chain Leader)",
        "lesson_num": 16,
        "level_tr": "Seviye 4: Operasyon & Tedarik / Operations Director",
        "level_en": "Level 4: Operations & Supply Chain / Operations Director",
        "title_tr": "Ders 16: Yalın Yönetim 2.0 (Lean Six Sigma in AI): Süreç Madenciliği (Process Mining) ile İsrafı Yok Etmek",
        "title_en": "Lesson 16: Lean Operations 2.0: Eliminating Waste via AI Process Mining",
        "summary_tr": "Toyota'nın yalın üretim felsefesi (Kaizen ve Muda), yapay zeka çağında dijital süreç madenciliği (Process Mining) ile birleşiyor. Operasyon liderleri artık çalışanların hislerine göre değil, ERP ve CRM loglarını tarayan algoritmalarla şirket içindeki gizli darboğazları, tekrarlanan gereksiz onayları ve zaman israflarını milisaniye hassasiyetinde tespit edip yok ediyor.",
        "summary_en": "Toyota's classic lean philosophy (Kaizen and Muda) achieves its zenith through algorithmic Process Mining. Modern Chief Operating Officers no longer rely on subjective interviews; they ingest ERP, CRM, and communication event logs into graph neural networks to pinpoint hidden friction, redundant approval gates, and systemic waste with millisecond precision.",
        "eli5_metaphor_tr": "Eski usul operasyon yönetimi, bir su borusundaki tıkanıklığı bulmak için duvarı rastgele kırmaya benzer. Süreç madenciliği ise borunun içine küçük ışıklı bir kamera gönderip, tıkanıklığın tam olarak hangi dirsekte olduğunu ve oraya hangi paslı çivinin takıldığını ekranda net bir şekilde görmektir.",
        "eli5_metaphor_en": "Legacy operations management is guessing where a plumbing leak is by sledgehammering random walls across a building. AI Process Mining injects illuminated nano-tracers into the pipe network, mapping the exact microscopic valve obstruction on a digital twin display instantly.",
        "comparison_table": [
            {
                "topic_tr": "Süreç Haritalama",
                "topic_en": "Process Discovery",
                "old_way_tr": "Çalışanlarla anket yapıp duvara idealize edilmiş sahte akış şemaları çizmek.",
                "old_way_en": "Interviewing managers to draw idealized, fictional Visio flowcharts that reflect zero reality.",
                "ai_way_tr": "Sistem loglarını (SAP, Salesforce, Jira) okuyarak gerçekte ne yaşandığını gösteren canlı süreç ikizi çıkarmak.",
                "ai_way_en": "Ingesting raw system event logs to reconstruct the empirical digital twin of operational workflows."
            },
            {
                "topic_tr": "İsraf (Muda) Tespiti",
                "topic_en": "Waste (Muda) Identification",
                "old_way_tr": "Yılda bir kez verimlilik toplantısı yapıp genel tasarruf çağrıları yapmak.",
                "old_way_en": "Annual efficiency workshops pleading with employees to 'save paper and work smarter.'",
                "ai_way_tr": "En çok bekletilen onay adımlarını ve mükerrer işleri yapay zekayla otomatik işaretlemek.",
                "ai_way_en": "Continuous algorithmic scanning flagging rework loops, idle wait times, and bottlenecked approvers."
            },
            {
                "topic_tr": "İyileştirme Döngüsü",
                "topic_en": "Continuous Improvement",
                "old_way_tr": "Hantal 6 aylık danışmanlık projeleriyle küçük değişiklikler denemek.",
                "old_way_en": "Commissioning six-month consulting studies to recommend minor bureaucratic tweaks.",
                "ai_way_tr": "Haftalık Kaizen döngüleriyle süreçleri otonom kurallarla sürekli optimize etmek.",
                "ai_way_en": "Weekly automated Kaizen sprints adjusting routing logic dynamically based on volume."
            }
        ],
        "framework_steps_tr": [
            "1. 8 Büyük İsrafı (TIMWOODS) Dijitalleştir: Taşıma, Envanter, Hareket, Bekleme, Aşırı Üretim, Aşırı İşleme, Hatalar ve Kullanılmayan Yetenek.",
            "2. Olay Günlüklerini (Event Logs) Birleştir: Bir siparişin açılışından faturanın kapanışına kadar tüm zaman damgalarını (Timestamp) topla.",
            "3. Darboğaz Grafiği Çıkar: Hangi departman onayında ortalama bekleme süresi 48 saati aşıyor?",
            "4. Otonom Eleme: Katma değeri olmayan onay mekanizmalarını kaldır; belirli limitin altındaki kararları AI kurallarına delege et."
        ],
        "framework_steps_en": [
            "1. Digitalize the 8 TIMWOODS Wastes: Transport, Inventory, Motion, Waiting, Overproduction, Overprocessing, Defects, Skills.",
            "2. Ingest Universal Event Logs: Aggregate Case ID, Activity Name, and Timestamps across SAP, Jira, and email gateways.",
            "3. Generate the Friction Heatmap: Identify structural bottlenecks where cycle duration diverges from median SLA targets.",
            "4. Deprecate Low-Value Approval Gates: Replace bureaucratic sign-offs below predefined thresholds with algorithmic automated approvals."
        ],
        "case_study_tr": "Uluslararası bir üretim firmasında satın alma siparişlerinin onaylanması ortalama 18 gün sürüyordu ve fabrikada üretim aksıyordu. Yönetim 'daha çok personel alalım' diyordu. Yeni operasyon direktörü, son 6 aylık 14.000 satın alma sürecini AI süreç madenciliği yazılımına soktu. Şok edici gerçek ortaya çıktı: 500 TL'nin altındaki kırtasiye malzemeleri bile Genel Müdür Yardımcısı onayına gidiyor ve masasında ortalama 12 gün bekliyordu! Direktör 5.000 TL altındaki harcamaları otomatik onaylayan bir AI kuralı koydu. Sipariş süresi 18 günden 6 saate düştü ve şirket 2 milyon TL operasyonel maliyet tasarrufu sağladı.",
        "case_study_en": "A multinational manufacturing conglomerate suffered from an agonizing 18-day purchase order approval cycle that halted factory assembly lines. Management planned to hire 20 more procurement clerks. The newly appointed COO ran event-log process mining across 14,000 procurement cases. The audit exposed a ridiculous bottleneck: Even $40 stationery requests were routed to the Executive VP's desk, languishing in his queue for an average of 12 days. The COO automated all requisitions under $2,500 using rule-based AI verification. Cycle times collapsed from 18 days to 6 hours, saving $450k in annual overhead.",
        "ai_prompts": [
            {
                "title_tr": "Yalın Süreç Cerrahı ve Süreç Madenciliği Denetçisi",
                "title_en": "Lean Six Sigma Process Surgeon & Bottleneck Eliminator",
                "prompt_tr": "Sen dünyanın en kıdemli Yalın Altı Sigma Kara Kuşağı (Master Black Belt) ve Operasyon Direktörüsün. Sana şirketimizin şu operasyonel akışını veriyorum: [SÜREÇ ADIMLARI VE SÜRELERİ]. 1) Bu akıştaki en büyük 3 'Muda' (israf) noktasını TIMWOODS çerçevesinde teşhis et, 2) Katma değeri sıfır olan ve derhal kaldırılması gereken onay adımlarını belirle, 3) Süreç süresini %60 kısaltacak yapay zeka destekli otonom bir akış mimarisi tasarla.",
                "prompt_en": "Act as a Lean Six Sigma Master Black Belt and Principal Operations Architect. Analyze this enterprise operational workflow: [INSERT PROCESS STEPS & DURATIONS]. 1) Diagnose the primary bottlenecks using the TIMWOODS framework, 2) Identify zero-value bureaucratic approval gates that should be eliminated immediately, 3) Engineer an AI-orchestrated routing architecture to reduce cycle time by 60%."
            }
        ],
        "notebooklm_prompts_tr": "İki operasyon lideri: Biri her şeye imza atmak isteyen, masasında evrak dağları biriken hantal kurumsal müdür, diğeri süreç madenciliği ve yapay zekayla şirketteki tüm gereksiz bürokrasiyi tek gecede buharlaştıran yalın operasyon mimarı. 'Süreç madenciliği devrimi ve şirketlerdeki gizli zaman hırsızları' konusunu sürükleyici bir sohbetle ele alın.",
        "notebooklm_prompts_en": "A sharp, witty conversation exploring the absurdity of corporate bureaucracy: How an AI operations architect armed with process mining dismantled weeks of pointless approval chains, contrasting legacy paper-pushing with automated operational excellence.",
        "udemy_outline_tr": [
            "00:00 - Neden Şirketlerde İşler Bu Kadar Yavaş İlerler? Gizli İsraf",
            "04:30 - Toyota'nın Kaizen Felsefesinden Yapay Zeka Süreç Madenciliğine",
            "10:00 - TIMWOODS: Dijital Dünyanın 8 Büyük Zaman Hırsızı",
            "16:15 - Canlı Uygulama: 18 Günlük Süreci 6 Saate İndiren Akıllı Onay Sistemi",
            "22:30 - Eylem Görevi: Şirketindeki En Sıkıcı Onay Sürecini Haritala ve Yalınlaştır"
        ],
        "udemy_outline_en": [
            "00:00 - The Pathology of Corporate Sluggishness: Hidden Operational Friction",
            "04:30 - From Toyota Kaizen to Modern Algorithmic Process Mining",
            "10:00 - The Digital TIMWOODS Framework: Unmasking Cognitive Waste",
            "16:15 - Live Lab: Re-architecting an 18-Day Approval Nightmare into a 6-Hour Workflow",
            "22:30 - Action Assignment: Mapping and Deprecating Redundant Gates in Your Team"
        ]
    },
    {
        "id": 17,
        "part_num": 4,
        "part_title_tr": "Bölüm 4: Operasyonlar, Tedarik Zinciri & Yalın Süreçler (The Operations & Supply Chain Leader)",
        "part_title_en": "Part 4: Operations, Supply Chain & Automation (The Operations & Supply Chain Leader)",
        "lesson_num": 17,
        "level_tr": "Seviye 4: Operasyon & Tedarik / Operations Director",
        "level_en": "Level 4: Operations & Supply Chain / Operations Director",
        "title_tr": "Ders 17: Akıllı Tedarik Zinciri ve Lojistik: Talep Tahminleme, Stok Optimizasyonu ve Risk Modelleme",
        "title_en": "Lesson 17: Resilient Supply Chain: Predictive Demand Forecasting & Real-Time Logistics",
        "summary_tr": "Depolarda çürüyen atıl stoklar ile rafların boş kalması arasındaki ince çizgi, bir tedarik zincirinin kaderidir. Tarihsel verilere dayanan kör tahminleri bırakın; hava durumu, jeopolitik riskler, sosyal trendler ve makroekonomik sinyalleri birleştiren çok değişkenli AI modelleri ile 'Tam Zamanında' (Just-in-Time) değil, 'Her İhtimale Karşı Dayanıklı' (Just-in-Case Resilient) tedarik zincirleri kurun.",
        "summary_en": "The thin line between capital trapped in obsolete warehouse inventory and catastrophic stockouts dictates enterprise cash flows. Abandon static moving averages. Modern supply chain leaders orchestrate multi-modal AI systems integrating meteorological patterns, macroeconomic indices, and geopolitical friction to evolve from brittle Just-in-Time models into antifragile, predictive logistics networks.",
        "eli5_metaphor_tr": "Eski tedarik zinciri, araba kullanırken sadece dikiz aynasına bakmaya benzer; arkada ne gördüysen önünde de o var sanırsın ve virajı kaçırıp kaza yaparsın. Akıllı AI tedarik zinciri ise arabanın tepesindeki radar ve GPS gibidir: 10 kilometre ilerideki sisi, kayganlaşan yolu ve trafiği önceden görüp sana hızını ve rotanı anında ayarlar.",
        "eli5_metaphor_en": "Legacy supply chain planning is driving a truck on a mountain road while staring exclusively into the rearview mirror: You assume the road ahead is straight because it was straight 5 miles ago, until you fly off a cliff. Predictive AI is satellite radar scanning 20 miles ahead through fog, automatically recalculating brake timing before curves appear.",
        "comparison_table": [
            {
                "topic_tr": "Talep Tahmini (Forecasting)",
                "topic_en": "Demand Forecasting",
                "old_way_tr": "Geçen yılın satış rakamına %10 ekleyip Excel'de kaba tahminler yapmak.",
                "old_way_en": "Taking last year's sales and arbitrarily adding 8% in a spreadsheet.",
                "ai_way_tr": "Sosyal medya ilgisi, hava durumu, döviz kuru ve enflasyonu harmanlayan dinamik AI tahmini.",
                "ai_way_en": "Multi-variable forecasting ingesting macro indices, local weather patterns, and social search signals."
            },
            {
                "topic_tr": "Güvenlik Stoğu (Safety Stock)",
                "topic_en": "Safety Stock Strategy",
                "old_way_tr": "Korkudan depoyu gereksiz mallarla doldurup işletme sermayesini kilitlemek.",
                "old_way_en": "Hoarding excessive warehouse buffer stock that ties up critical working capital.",
                "ai_way_tr": "Olasılıksal talep eğrileriyle her SKU için dinamik ve optimize edilmiş güvenlik stoğu.",
                "ai_way_en": "Dynamic probabilistic SKU-level safety buffers calibrated to supplier lead-time variance."
            },
            {
                "topic_tr": "Jeopolitik & Lojistik Risk",
                "topic_en": "Supply Disruption Resilience",
                "old_way_tr": "Süveyş Kanalı tıkandığında veya kriz çıktığında çaresizce beklemek.",
                "old_way_en": "Paralyzed reactivity when a canal blocks or a primary supplier declares bankruptcy.",
                "ai_way_tr": "Tedarikçileri tek coğrafyaya bağlamayan, AI ile önceden alternatif rota simüle eden çoklu kaynak.",
                "ai_way_en": "Continuous multi-tier supplier stress-testing with automated contingency rerouting."
            }
        ],
        "framework_steps_tr": [
            "1. Kamçı Etkisi (Bullwhip Effect) Teşhisi: Müşteri talebindeki küçük bir dalgalanmanın fabrikada devasa stok krizine dönüşmesini engelle.",
            "2. SKU Bazlı ABC/XYZ Sınıflandırması: Ürünlerini hem ciro etkisine (A-B-C) hem de talep tahmin edilebilirliğine (X-Y-Z) göre matrise dök.",
            "3. Tedarikçi Dayanıklılık Skoru: Her tedarikçinin teslim süresi sapmalarını AI ile puanla; güvenilmez ortaklara bağımlılığı azalt.",
            "4. Dinamik Sipariş Noktası (ROP): Sabit sipariş günlerini kaldır; stok seviyesi kritik eşiğe geldiğinde sistemin otonom sipariş açmasını sağla."
        ],
        "framework_steps_en": [
            "1. Dampen the Bullwhip Effect: Share real-time point-of-sale data across tiers to prevent distorted upstream inventory panics.",
            "2. Execute ABC/XYZ Matrix Clustering: Categorize SKUs by revenue contribution (ABC) and consumption predictability (XYZ).",
            "3. Supplier Volatility Scoring: Track lead-time variance and geopolitical friction scores across all primary vendors.",
            "4. Algorithmic Reorder Point (ROP): Implement dynamic recalculations that trigger supplier orders automatically when risk thresholds breach."
        ],
        "case_study_tr": "Bir kış giyim markası, her yıl sonu 3 milyon dolarlık satılmayan mont stokuyla baş başa kalıyordu çünkü tahminler sadece önceki yılın satışlarına bakıyordu. Yeni tedarik zinciri direktörü, meteoroloji verilerini ve mikro-bölgesel soğuma modellerini satış verileriyle birleştiren bir AI talep motoru kurdu. Model, Doğu Anadolu'da kışın erken geleceğini, Batı'da ise pastırma yazı yaşanacağını öngörerek stok sevkiyatlarını yeniden planladı. Sezon sonunda stok fazlası %72 azaldı ve şirket 1.4 milyon $ nakit tasarrufu elde etti.",
        "case_study_en": "A premier winter apparel brand routinely suffered from $3M in leftover dead-stock coats because production orders were placed using naive historical averages. The supply chain leader deployed an AI predictive engine cross-referencing multi-month meteorological models with regional search velocity. Detecting delayed cold fronts across coastal regions alongside early freezes inland, the system shifted distribution allocations across warehouses dynamically. End-of-season inventory write-downs dropped by 72%, freeing $1.4M in operational liquidity.",
        "ai_prompts": [
            {
                "title_tr": "Tedarik Zinciri Risk Analisti ve Dinamik Stok Mimarı",
                "title_en": "Antifragile Supply Chain & Predictive Inventory Strategist",
                "prompt_tr": "Sen Fortune 500 şirketlerinin Baş Tedarik Zinciri Yöneticisisin (CSCO). Aşağıdaki ürün ve tedarikçi bilgilerini incele: [ÜRÜN, TEDARİKÇİ VE TESLİMAT VERİSİ]. 1) Bu tedarik ağındaki en kritik 2 tekil arıza noktasını (Single Point of Failure) ve kamçı etkisi riskini belirle, 2) Stok maliyetini %30 düşürürken 'Yok Satma' (Stockout) riskini sıfıra yakın tutacak dinamik bir Güvenlik Stoğu formülü öner, 3) Kızıldeniz veya Süveyş benzeri bir kriz için 48 saatlik acil B planı hazırla.",
                "prompt_en": "Act as a Chief Supply Chain Officer managing an antifragile global distribution network. Evaluate the following logistics parameters: [INSERT DATA]. 1) Identify the top two single points of failure and latent bullwhip vulnerabilities, 2) Design an automated safety stock protocol that lowers carrying costs by 30% without breaching 99% fulfillment SLAs, 3) Formulate an emergency contingency playbook for sudden maritime canal disruptions."
            }
        ],
        "notebooklm_prompts_tr": "İki lojistik uzmanı: Biri depoyu satılmayan mallarla doldurup şirket kasasını kilitleyen eski kafa lojistikçi, diğeri hava durumu ve pazar verilerini yapay zekayla okuyarak sıfır atıkla çalışan tedarik zinciri dehası. 'Kamçı etkisi nedir ve modern şirketler stok krizlerinden nasıl kaçınır?' konusunu sürükleyici bir vaka ile tartışın.",
        "notebooklm_prompts_en": "A gripping logistics podcast debate: Analyzing the devastating Bullwhip Effect, contrasting bloated warehouses of yesterday with modern predictive AI fulfillment networks that synchronize global shipping with consumer micro-trends.",
        "udemy_outline_tr": [
            "00:00 - Tedarik Zincirinin Sessiz Katili: Kamçı Etkisi (Bullwhip Effect)",
            "04:50 - 'Tam Zamanında' (JIT) Modelinin Çöküşü ve Dayanıklı Tedarik Zincirleri",
            "10:15 - ABC/XYZ Matrisi ile Akıllı Stok Sınıflandırması",
            "16:30 - Canlı Uygulama: Hava Durumu ve Trendleri Birleştiren AI Talep Tahmini",
            "22:50 - Eylem Görevi: Kendi Şirketinin Tedarikçi Bağımlılık Haritasını Çıkar"
        ],
        "udemy_outline_en": [
            "00:00 - The Silent Enterprise Killer: Unmasking the Bullwhip Effect",
            "04:50 - The Demise of Fragile Just-in-Time: Engineering Antifragility",
            "10:15 - Granular Portfolio Segmentation via the ABC/XYZ Matrix",
            "16:30 - Live Lab: Building a Weather-Aware AI Demand Forecast",
            "22:50 - Action Assignment: Stress-Testing Your Tier-1 Supplier Dependencies"
        ]
    },
    {
        "id": 18,
        "part_num": 4,
        "part_title_tr": "Bölüm 4: Operasyonlar, Tedarik Zinciri & Yalın Süreçler (The Operations & Supply Chain Leader)",
        "part_title_en": "Part 4: Operations, Supply Chain & Automation (The Operations & Supply Chain Leader)",
        "lesson_num": 18,
        "level_tr": "Seviye 4: Operasyon & Tedarik / Operations Director",
        "level_en": "Level 4: Operations & Supply Chain / Operations Director",
        "title_tr": "Ders 18: Otonom İş Akışları ve Robotik Süreç Otomasyonu (RPA & Agentic Workflows): Rutin Operasyonları Devretmek",
        "title_en": "Lesson 18: Autonomous Business Workflows: Orchestrating Agentic Workflows to 10x Operational Speed",
        "summary_tr": "Eski nesil Robotik Süreç Otomasyonu (RPA), ekranda bir butonun yeri 2 piksel değiştiğinde bozulan kırılgan kural tabanlı robotlardan ibaretti. Yeni nesil Agentic Workflows ise; algılayan, akıl yürüten, API'ları dinamik çağıran ve beklenmedik hatalarla karşılaştığında kendi kendine çözüm üreten otonom yapay zeka çalışanlarıdır.",
        "summary_en": "Legacy Robotic Process Automation (RPA) was a fragile illusion—breaking the moment a web button moved two pixels. Modern Agentic Workflows deploy autonomous cognitive loops (Perceive -> Reason -> Act -> Evaluate) powered by LLMs with tool-calling capabilities, executing multi-system business operations with resilient self-healing autonomy.",
        "eli5_metaphor_tr": "Eski RPA, gözleri bağlı olarak ezbere yürüyen bir robota benzer; önüne küçük bir sandalye koysan takılıp düşer ve kalkamaz. Ajan tabanlı yapay zeka ise gözleri açık, düşünen ve yoluna bir taş çıktığında 'Dur, ben bu taşın etrafından dolaşayım ya da vinç çağırıp taşı kaldırayım' diyen akıllı bir saha mühendisidir.",
        "eli5_metaphor_en": "Legacy RPA is a blindfolded worker walking a strictly memorized path: Place a pebble in his way, and he trips, crashing the entire factory. Modern Agentic Workflows are intelligent navigators with eyesight and reasoning: When a detour appears, they assess alternatives, consult documentation, call an API, and complete the delivery.",
        "comparison_table": [
            {
                "topic_tr": "Otomasyon Mimarisi",
                "topic_en": "Automation Architecture",
                "old_way_tr": "Kırılgan kural tabanlı RPA: 'A hücresini kopyala, B formuna yapıştır.'",
                "old_way_en": "Brittle script-based RPA: Hard-coded coordinate clicks that break constantly.",
                "ai_way_tr": "Hedef odaklı Ajan Akışı: 'Şu faturayı incele, vergi numarasını doğrula ve ödemeyi yap.'",
                "ai_way_en": "Goal-driven Agentic Loops: Autonomous reasoning with dynamic tool use and error handling."
            },
            {
                "topic_tr": "Hata ve İstisna Yönetimi",
                "topic_en": "Exception Handling",
                "old_way_tr": "En ufak format değişikliğinde akışın patlaması ve teknik destek çağrılması.",
                "old_way_en": "Throwing fatal exceptions and stalling business operations whenever formatting shifts.",
                "ai_way_tr": "Semantik anlama: Veri formatı bozuk olsa bile içeriği anlayıp düzelten yapay zeka.",
                "ai_way_en": "Semantic elasticity: Parsing unstructured PDFs, broken emails, and messy inputs with LLMs."
            },
            {
                "topic_tr": "İnsan Müdahalesi (HITL)",
                "topic_en": "Human-in-the-Loop Integration",
                "old_way_tr": "İnsanın ya sürecin başında ya da sonunda amelelik yapmaya devam etmesi.",
                "old_way_en": "Humans doing manual pre-formatting and post-cleanup around dumb automation scripts.",
                "ai_way_tr": "İnsanın sadece stratejik denetçi ve nihai onaylayıcı (Supervisor) olarak konumlanması.",
                "ai_way_en": "Humans elevated to supervisory architects reviewing high-risk exceptions above confidence thresholds."
            }
        ],
        "framework_steps_tr": [
            "1. Görev Ayrıştırması Yap: İşi Deterministik (Kurala bağlı) vs. Bilişsel (Muhakeme gerektiren) parçalara böl.",
            "2. Tool-Calling Mimarisi Kur: Yapay zekaya ERP'yi okuma, e-posta atma ve veritabanı sorgulama gibi spesifik 'araçlar' (Tools) ver.",
            "3. Güven Eşiği (Confidence Threshold): Ajanın doğruluğundan %95 emin olduğu işleri otomatik bitirmesini, %95 altındakileri insan onayına göndermesini sağla.",
            "4. Kendi Kendini Denetleyen Döngü (Self-Reflective Loop): Ajanın işlem yapmadan önce 'Bu çıktı şirket politikalarına ve bütçeye uygun mu?' kontrolü yapmasını sağla."
        ],
        "framework_steps_en": [
            "1. Task Decoupling: Partition workflows into deterministic calculations and probabilistic cognitive evaluations.",
            "2. Equip Agentic Toolboxes: Provide the LLM with structured API functions (e.g., query_sql, issue_refund, send_slack_alert).",
            "3. Confidence-Gated Escalation: Automate actions where model confidence exceeds 95%; route borderline cases to a human specialist.",
            "4. Self-Correction Reflexion Loop: Mandate a secondary verification step where the agent critiques its own proposed API payload against policy."
        ],
        "case_study_tr": "Büyük bir hukuk ve denetim şirketinde 15 kişilik bir stajyer ekibi, her gün gelen 800 farklı tedarikçi sözleşmesini okuyup 'cezai şartlar ve gizlilik maddelerini' Excel'e işliyordu. Hata oranı %14'tü ve haftalar sürüyordu. Operasyon lideri, açık kaynaklı bir Agentic Workflow (LangGraph / n8n tabanlı) kurdu. Birinci ajan sözleşmeyi tarayıp maddeleri ayıklıyor, ikinci ajan bunları şirketin yasal risk politikasıyla karşılaştırıyor, üçüncü ajan ise bulunan anomalileri avukata tek tıkla onaylanacak bir Slack mesajı olarak atıyordu. İşlem süresi 15 günden 4 dakikaya indi, hata oranı sıfırlandı ve 15 çalışan stratejik danışmanlık rollerine kaydırıldı.",
        "case_study_en": "A premier corporate audit firm employed 15 paralegals solely to review 800 incoming vendor contracts monthly, extracting indemnity clauses into spreadsheets with a 14% error rate. The COO orchestrated an agentic workflow using structured tool-calling. Agent 1 parsed unstructured PDFs into structured JSON schemas; Agent 2 cross-referenced contractual terms against corporate risk thresholds; Agent 3 compiled flagged redlines and pushed interactive Slack approval cards to senior partners. Processing cycle time crashed from 14 days to 4 minutes with 99.8% extraction fidelity.",
        "ai_prompts": [
            {
                "title_tr": "Otonom İş Akışı ve Agentic Tool-Calling Mimarı",
                "title_en": "Autonomous Workflow Architect & Agentic Orchestrator",
                "prompt_tr": "Sen dünyanın en iyi Kurumsal Otomasyon Mimarı ve CTO Danışmanısın. Şu manuel iş akışını ele al: [MANUEL SÜRECİ VE ARAÇLARI YAZ]. 1) Bu süreci otonom hale getirecek çoklu ajan mimarisini (Orchestrator, Worker ve Critic ajanları) tasarla, 2) Ajanların kullanacağı 3 temel API fonksiyonunu (Tool-calling şeması) tanımla, 3) Sürecin kontrolden çıkmasını ve şirket kasasını boşaltmasını önleyecek 'Human-in-the-Loop' güvenlik bariyerlerini yaz.",
                "prompt_en": "Act as an Enterprise Autonomous Systems Architect. For this multi-step manual workflow: [INSERT PROCESS & TOOLS]: 1) Design a multi-agent orchestration architecture (Dispatcher, Executor, Critic), 2) Define three JSON tool-calling schemas required to interface with core ERP/CRM databases, 3) Formulate strict confidence thresholds and human-in-the-loop circuit breakers to prevent erroneous transactions."
            }
        ],
        "notebooklm_prompts_tr": "İki teknoloji yöneticisi: Biri eski usul RPA robotlarının sürekli bozulmasından bıkmış bezgin bir IT müdürü, diğeri kendi kendini iyileştiren (self-healing) agentic sistemlerle şirketteki tüm rutin evrak işlerini sıfırlayan modern operasyon lideri. 'Robotik Süreç Otomasyonunun sonu ve düşünen yapay zeka ajanlarının iş dünyasını fethi' konusunu nefes kesici bir sohbetle dinleyin.",
        "notebooklm_prompts_en": "A dynamic podcast debate between an IT manager exhausted by fragile, brittle RPA scripts, and a forward-leaning operations executive running cognitive multi-agent workflows. Explore why agentic autonomy represents the greatest shift in white-collar productivity since the personal computer.",
        "udemy_outline_tr": [
            "00:00 - Neden Eski Nesil RPA Projelerinin %70'i Başarısız Oldu?",
            "04:40 - Agentic Workflows Nedir? Algıla -> Düşün -> Harekete Geç Döngüsü",
            "10:15 - Çoklu Ajan Sistemleri: Görev Dağıtımı ve Karşılıklı Denetim (Critic)",
            "16:20 - Canlı Uygulama: Fatura ve Sözleşmeleri 3 Dakikada İşleyen Otonom Akış",
            "22:45 - Eylem Görevi: Kendi Departmanındaki En Çok Zaman Alan İşi Ajan Akışına Çevir"
        ],
        "udemy_outline_en": [
            "00:00 - The Autopsy of Legacy RPA: Why Hard-Coded Scripts Collapse",
            "04:40 - The Architecture of Agentic Loops: Perceive, Reason, Act, Reflect",
            "10:15 - Multi-Agent Topologies: Orchestrators, Specialists, and Evaluators",
            "16:20 - Live Lab: Deploying an Autonomous Contract Ingestion & Triage Pipeline",
            "22:45 - Action Assignment: Designing Your Team's First Self-Correcting Business Agent"
        ]
    },
    {
        "id": 19,
        "part_num": 4,
        "part_title_tr": "Bölüm 4: Operasyonlar, Tedarik Zinciri & Yalın Süreçler (The Operations & Supply Chain Leader)",
        "part_title_en": "Part 4: Operations, Supply Chain & Automation (The Operations & Supply Chain Leader)",
        "lesson_num": 19,
        "level_tr": "Seviye 4: Operasyon & Tedarik / Operations Director",
        "level_en": "Level 4: Operations & Supply Chain / Operations Director",
        "title_tr": "Ders 19: Kalite Güvencesi ve Hizmet Seviyesi Anlaşmaları (SLA): Gerçek Zamanlı AI İzleme ve Anomali Tespiti",
        "title_en": "Lesson 19: Quality Management & SLA Enforcement: Real-Time AI Anomaly Detection",
        "summary_tr": "Kalite kontrolü iş bittikten sonra yapılan bir 'otopsi' olmamalıdır. Müşteri şikayet etmeden veya sistem çökmeden önce devreye giren gerçek zamanlı anomali dedektörleri, otomatik SLA ihlal uyarıları ve telemetri analizleri ile kusurları kaynağında yok eden sıfır hata (Zero-Defect) kültürünü inşa edin.",
        "summary_en": "Quality assurance must never be a post-mortem post-production autopsy. Modern enterprise excellence relies on real-time acoustic, visual, and telemetry anomaly detectors that flag sub-perceptual degradations before customer SLAs are breached, embedding a proactive Zero-Defect standard into every physical and digital workflow.",
        "eli5_metaphor_tr": "Eski kalite kontrolü, bir restoranda müşteriye yemeği servis ettikten sonra garsonun gelip 'Yemek zehirli miydi?' diye sormasıdır. Modern AI kalite kontrolü ise mutfakta yemeğin kokusunu, sıcaklığını ve tazeliğini pişerken kontrol eden ve tuz oranı 1 gram fazla olsa bile tabağın mutfaktan çıkmasına izin vermeyen akıllı bir şeftir.",
        "eli5_metaphor_en": "Legacy quality control is serving a diner a meal and waiting to see if they end up in the emergency room. Modern AI quality assurance is an optical and chemical sensor grid in the kitchen that halts the line the instant oil temperature or ingredient composition drifts by 0.5% from perfection.",
        "comparison_table": [
            {
                "topic_tr": "Kalite Kontrol Zamanı",
                "topic_en": "Inspection Timing",
                "old_way_tr": "Reaktif: Ürün üretilip depolandıktan veya müşteri şikayet ettikten sonra inceleme yapmak.",
                "old_way_en": "Reactive post-mortem: Inspecting random batch samples after production completes.",
                "ai_way_tr": "Proaktif: Süreç işlerken gerçek zamanlı sensör ve veri akışıyla anında müdahale.",
                "ai_way_en": "Real-time in-line telemetry detecting micro-drifts at the millisecond of occurrence."
            },
            {
                "topic_tr": "SLA Takip Mekanizması",
                "topic_en": "SLA Enforcement",
                "old_way_tr": "Ay sonunda hizmet seviyesi raporlarına bakıp ceza ödemeyi kabullenmek.",
                "old_way_en": "Reviewing monthly SLA penalty invoices after client trust has been shattered.",
                "ai_way_tr": "SLA ihlaline 15 dakika kala otomatik kaynak tahsis eden ve uyaran erken uyarı sistemleri.",
                "ai_way_en": "Predictive SLA breach interceptors that autonomously reallocate compute/staff buffers."
            },
            {
                "topic_tr": "Hata Kök Neden Analizi",
                "topic_en": "Root-Cause Diagnostics",
                "old_way_tr": "Haftalar süren suçlu arama toplantıları ve yüzeysel 'insan hatası' bahaneleri.",
                "old_way_en": "Endless corporate finger-pointing sessions concluding with 'operator error.'",
                "ai_way_tr": "AI ile '5 Neden' (5 Whys) ve Ishikawa balık kılçığı analizini sistem verisinden saniyeler içinde üretmek.",
                "ai_way_en": "Automated 5-Whys causal graph synthesis tracing anomalies back to subtle upstream changes."
            }
        ],
        "framework_steps_tr": [
            "1. İstatistiksel Süreç Kontrolü (SPC) + AI: Süreçteki doğal varyasyon ile anomaliyi birbirinden ayıran algoritmik kontrol limitleri koy.",
            "2. SLA Yanma Oranı (Burn Rate) Takibi: Hizmet seviyesi sözleşmesinin tükenme hızını izle; %70 risk eşiğinde otomatik kırmızı alarm ver.",
            "3. Bilgisayarlı Görü ve Telemetri: Fiziksel üretimde kameralarla mikroskobik çatlakları, dijitalde ise gecikme (latency) sıçramalarını yakala.",
            "4. Kusursuz Kök Neden Raporu (CAPA): Tespit edilen her hatadan sonra AI'a düzeltici ve önleyici eylem planı yazdır ve standardı güncelle."
        ],
        "framework_steps_en": [
            "1. Algorithmic Statistical Process Control: Establish dynamic machine-learning control boundaries distinguishing noise from signal.",
            "2. Monitor Error-Budget & SLA Burn Rate: Trigger automated escalation protocols when incident burn rate threatens quarterly SLA covenants.",
            "3. Multi-Modal Vision & Telemetry Auditing: Deploy computer vision on manufacturing lines and sub-millisecond tracing in cloud microservices.",
            "4. Automated CAPA Generation: Synthesize immediate Corrective and Preventive Action documentation to update standard operating procedures."
        ],
        "case_study_tr": "Fintech ölçeğinde bir mobil ödeme şirketi, büyük perakendecilerle %99.99 SLA taahhüdü yapmıştı. Her SLA ihlalinde 250.000 $ ceza ödüyorlardı. Eski izleme araçları sistem tamamen çöktüğünde haber veriyordu. Operasyon lideri, ödeme gecikmelerini ve başarısızlık oranlarını milisaniyelik anomali taramasına sokan bir yapay zeka sistemi kurdu. Sistem, bir veri merkezinde hafif bir gecikme başladığında, SLA ihlali yaşanmadan 7 dakika önce trafiği otonom olarak yedek veri merkezine aktarmayı başardı. Şirket 1 yıl boyunca sıfır SLA cezası ödedi ve 2.5 milyon $ tasarruf etti.",
        "case_study_en": "A fintech payment processor committed to a 99.99% uptime SLA with enterprise retail partners, backed by $250,000 breach penalties. Legacy monitoring only fired alarms after transactions were actively failing. The Operations VP implemented real-time isolation-forest anomaly scoring across API gateway latencies. Detecting a microscopic database connection drift, the AI autonomously drained and rerouted transaction traffic to redundant failover nodes 7 minutes before an outage would have manifested. The company recorded zero SLA penalties over 12 months, saving $2.5M in clawbacks.",
        "ai_prompts": [
            {
                "title_tr": "Sıfır Hata ve SLA Kök Neden Cerrahı (Ishikawa & 5 Whys)",
                "title_en": "Zero-Defect Quality Architect & Ishikawa Root-Cause Engine",
                "prompt_tr": "Sen dünyanın en katı Kalite Güvence ve Operasyon Direktörüsün. Yaşadığımız şu operasyonel arıza/hizmet kesintisi verisini incele: [ARIZA DETAYLARI]. 1) Ishikawa (Balık Kılçığı) metodolojisini kullanarak arızanın arkasındaki 4 ana kategoriyi (İnsan, Makine, Metot, Malzeme) analiz et, 2) '5 Neden' (5 Whys) tekniğiyle kök sebebi en derine inerek bul, 3) Bu hatanın gelecekte tekrarlanmasını imkansız kılacak otomatik bir Poka-Yoke (hata önleyici) kontrol mekanizması tasarla.",
                "prompt_en": "Act as a world-class Quality Assurance Executive and Reliability Engineer. For this catastrophic service outage or production defect: [INSERT INCIDENT LOGS]: 1) Structure a rigorous Ishikawa (Fishbone) diagram across Methods, Machinery, Materials, and Manpower, 2) Execute a deep '5 Whys' root-cause trajectory, 3) Formulate an automated Poka-Yoke (mistake-proofing) operational guardrail that mathematically precludes recurrence."
            }
        ],
        "notebooklm_prompts_tr": "İki kalite müdürü: Biri hata çıktığında çalışanları suçlayıp tutanak tutan eski kafalı fabrika müfettişi, diğeri gerçek zamanlı anomali dedektörleri ve yapay zekayla sıfır hata kültürünü kuran modern operasyon mimarı. 'Kalite kontrolünün geleceği ve arızaları daha yaşanmadan önleyen sistemler' üzerine heyecan verici bir sohbet yapın.",
        "notebooklm_prompts_en": "A fascinating discussion exploring the shift from punitive, backward-looking quality inspections to proactive, AI-driven zero-defect environments. Discover how real-time anomaly detection transforms operational discipline from a cost center into a core competitive moat.",
        "udemy_outline_tr": [
            "00:00 - Kalite Kontrolün Karanlık Yüzü: Otopsi Yapmaktan Vazgeçin",
            "04:50 - Gerçek Zamanlı Telemetri ve İstatistiksel Süreç Kontrolü (SPC)",
            "10:15 - SLA Yanma Hızı (Burn Rate) Takibi ve Milyon Dolarlık Cezaları Önleme",
            "16:20 - Canlı Uygulama: AI ile Ishikawa Balık Kılçığı ve 5 Neden Analizi",
            "22:30 - Eylem Görevi: Kendi Sürecin İçin Bir 'Poka-Yoke' Hata Engelleyici Tasarla"
        ],
        "udemy_outline_en": [
            "00:00 - The Pathology of Late Inspections: Stop Performing Quality Autopsies",
            "04:50 - Real-Time Telemetry & Algorithmic Statistical Process Control",
            "10:15 - SLA Error-Budget Burn-Rate Management in Enterprise Contracts",
            "16:20 - Live Lab: Automated Ishikawa Root-Cause and 5-Whys Synthesis",
            "22:30 - Action Assignment: Designing a Foolproof Poka-Yoke Mechanism for Your Team"
        ]
    },
    {
        "id": 20,
        "part_num": 4,
        "part_title_tr": "Bölüm 4: Operasyonlar, Tedarik Zinciri & Yalın Süreçler (The Operations & Supply Chain Leader)",
        "part_title_en": "Part 4: Operations, Supply Chain & Automation (The Operations & Supply Chain Leader)",
        "lesson_num": 20,
        "level_tr": "Seviye 4: Operasyon & Tedarik / Operations Director",
        "level_en": "Level 4: Operations & Supply Chain / Operations Director",
        "title_tr": "Ders 20: Yeşil Operasyonlar ve Sürdürülebilirlik (ESG): AI ile Karbon Ayak İzi Takibi ve Enerji Verimliliği",
        "title_en": "Lesson 20: Sustainable Operations & ESG: Optimizing Carbon Footprints via Machine Intelligence",
        "summary_tr": "Sürdürülebilirlik ve ESG (Çevresel, Sosyal, Yönetişim) artık sadece PR broşürlerini süsleyen bir vicdan tatmini değildir; sermayeye erişimi, regülasyon cezalarını ve şirket değerlemesini doğrudan belirleyen sert bir finansal zorunluluktur. Kapsam 1, 2 ve 3 emisyonlarını yapay zeka ile optimize ederek hem dünyayı koruyun hem de operasyonel giderleri (OPEX) radikal şekilde düşürün.",
        "summary_en": "Environmental, Social, and Governance (ESG) criteria are no longer glossy public relations window dressing; they dictate the weighted average cost of capital (WACC), regulatory licensing, and valuation multiples. By applying machine intelligence to Scope 1, 2, and 3 emissions auditing, forward-leaning COOs turn decarbonization into aggressive operational cost-reduction.",
        "eli5_metaphor_tr": "Eski şirketlerin çevreciliği, ofisteki çöp kutularının üzerine 'kağıtları buraya atın' yazıp arka tarafta elektrikleri sabaha kadar açık bırakmaya benzer. Akıllı yeşil operasyon ise fabrikanın her prizine, fırınına ve kamyonuna akıllı sayaçlar bağlayıp, gereksiz her watt enerjiyi saniyesinde kısarak hem doğayı hem de şirketin cüzdanını korumaktır.",
        "eli5_metaphor_en": "Greenwashing is putting a bamboo plant in the office lobby while diesel generators idle in the backyard. AI-driven sustainable operations is turning your entire enterprise into an energy-orchestrated organism: Algorithmic load-shifting that runs compute or machinery when renewable grid power is cheapest and cleanest.",
        "comparison_table": [
            {
                "topic_tr": "ESG ve Sürdürülebilirlik Yaklaşımı",
                "topic_en": "ESG Orientation",
                "old_way_tr": "'Yeşil aklama' (Greenwashing): Yüzeysel PR bültenleri ve ağaç dikme fotoğrafları.",
                "old_way_en": "Superficial greenwashing: Glossy marketing photos of executives planting saplings.",
                "ai_way_tr": "Sert Veri & ROI: Karbon tasarrufunu doğrudan enerji maliyeti düşüşüne bağlayan analitik.",
                "ai_way_en": "Empirical rigor: Decarbonization engineered directly as operational margin expansion."
            },
            {
                "topic_tr": "Emisyon Ölçümü (Scope 1, 2, 3)",
                "topic_en": "Emissions Telemetry",
                "old_way_tr": "Yılda bir kez tahmini katsayılarla doldurulan uydurma Excel tabloları.",
                "old_way_en": "Annual guestimates filled into compliance spreadsheets weeks before audit deadlines.",
                "ai_way_tr": "Tedarik zincirindeki IoT ve lojistik verilerini tarayan gerçek zamanlı karbon takibi.",
                "ai_way_en": "Continuous telemetry tracking Scope 1 direct, Scope 2 indirect, and Scope 3 supply chain footprints."
            },
            {
                "topic_tr": "Enerji Yönetimi",
                "topic_en": "Energy Optimization",
                "old_way_tr": "Klimaları ve makineleri sabit sıcaklıkta ve sabit tarifede çalıştırmak.",
                "old_way_en": "Static, uncalibrated HVAC and industrial machinery operations running 24/7.",
                "ai_way_tr": "Dinamik yük kaydırma (Load Shifting): Elektrik fiyatı ve karbon yoğunluğu düşükken üretim yapmak.",
                "ai_way_en": "Dynamic load shifting: Scheduling heavy compute and factory shifts during peak renewable grid windows."
            }
        ],
        "framework_steps_tr": [
            "1. Kapsam (Scope) Haritası Çıkar: Kapsam 1 (Doğrudan emisyonlar), Kapsam 2 (Satın alınan elektrik), Kapsam 3 (Tüm tedarik zinciri ve lojistik).",
            "2. IoT ve Sensör Entegrasyonu: Tesislerdeki en çok enerji tüketen ilk 5 varlığa akıllı telemetri sensörleri bağla.",
            "3. Rota ve Lojistik Optimizasyonu: Dağıtım filolarının rotalarını AI ile optimize ederek boş kilometreleri ve yakıt tüketimini %20 azalt.",
            "4. Yeşil Tedarikçi Puanlaması: Tedarikçileri sadece fiyata göre değil, karbon verimlilik skoruna göre de sıralayarak regülasyon cezalarını önle."
        ],
        "framework_steps_en": [
            "1. Map the Greenhouse Gas Protocol: Segment footprint into Scope 1 (Direct burning), Scope 2 (Purchased electricity), Scope 3 (Value chain lifecycle).",
            "2. Deploy Automated Energy Telemetry: Install IoT power meters on top industrial HVAC, refrigeration, and compute infrastructure.",
            "3. Route Fleet Optimization: Run topological genetic routing algorithms to cut logistics idle times and deadhead miles by 20%.",
            "4. Green Supplier Procurement Gate: Condition vendor contract awards on verified carbon intensity ratings to bulletproof EU CSRD compliance."
        ],
        "case_study_tr": "Avrupa'ya ihracat yapan büyük bir gıda işleme fabrikası, AB Karbon Düzenleme Mekanizması (CBAM) nedeniyle yıllık 1.8 milyon euro karbon vergisi riskiyle karşılaştı. Operasyon direktörü, soğuk hava depoları ve fırınların enerji tüketimini şebekenin anlık yenilenebilir enerji üretimiyle senkronize eden bir AI enerji orkestratörü kurdu. Sistem, rüzgar ve güneş enerjisinin bol ve ucuz olduğu saatlerde depoları ekstra soğutuyor (termal batarya etkisi), enerji pahalandığında ise tüketimi kısıyordu. Fabrika karbon emisyonunu %38 azalttı, elektrik faturasından yılda 750.000 euro tasarruf etti ve sıfır karbon cezası ödedi.",
        "case_study_en": "A premier cold-storage and food processing exporter faced $2M in punitive European Carbon Border Adjustment Mechanism (CBAM) tariffs. The Operations Director installed an AI thermal orchestrator across their refrigeration facilities. Acting as a synthetic thermal battery, the system hyper-chilled warehouses during midday hours when solar grid generation created negative wholesale power pricing, idling power draw during peak grid demand windows. The facility slashed carbon intensity by 38%, cut net power bills by $820,000 annually, and qualified for zero cross-border carbon tariffs.",
        "ai_prompts": [
            {
                "title_tr": "Kurumsal ESG Denetçisi ve Karbon Ayak İzi Optimizasyon Mimarı",
                "title_en": "Corporate ESG Auditor & Scope 1-2-3 Decarbonization Strategist",
                "prompt_tr": "Sen uluslararası kurumsal sürdürülebilirlik ve ESG Baş Danışmanısın (GRI ve GHG Protocol standartlarında). Şu operasyonel verileri incele: [TESİS, ENERJİ TÜKETİMİ VE LOJİSTİK BİLGİSİ]. 1) Bu şirketin Kapsam 1, 2 ve 3 emisyonlarındaki en büyük 3 karbon kaçağını belirle, 2) Şirketin hem karbonunu %30 düşürecek hem de yıllık en az 500.000 $ operasyonel maliyet tasarrufu sağlayacak 2 somut mühendislik müdahalesi tasarla, 3) Avrupa Birliği CSRD ve CBAM regülasyonlarına uyum için 90 günlük eylem planı yaz.",
                "prompt_en": "Act as a Lead ESG & Decarbonization Partner at an elite sustainability advisory. Evaluate these enterprise operational inputs: [INSERT ENERGY & FLEET DATA]. 1) Isolate the top three carbon-intensive operations across Scopes 1, 2, and 3, 2) Engineer two operational interventions that cut greenhouse gas emissions by 30% while generating at least $500k in annual OPEX savings, 3) Formulate a 90-day compliance roadmap for European CSRD and CBAM reporting standards."
            }
        ],
        "notebooklm_prompts_tr": "İki şirket lideri: Biri çevreciliği 'boş masraf ve PR broşürü' olarak gören eski kafalı CEO, diğeri yeşil operasyonları yapay zekayla harmanlayarak hem elektrik faturalarını yarı yarıya düşüren hem de şirketin piyasa değerini artıran modern operasyon direktörü. 'Yeşil dönüşümün gizli kârlılığı: Dünya kurtulurken kasalar nasıl dolar?' temasını çarpıcı örneklerle ele alın.",
        "notebooklm_prompts_en": "A lively, illuminating podcast debate: Exploding the myth that sustainability is an expensive corporate tax. Discover how intelligent load shifting, Scope 3 supply chain telemetry, and algorithmic route optimization turn environmental compliance into a ruthless profit engine.",
        "udemy_outline_tr": [
            "00:00 - Yeşil Aklamanın Sonu: Neden ESG Artık Bir Finans Meselesidir?",
            "04:45 - Kapsam 1, 2 ve 3 Emisyonlarını Anlamak (GHG Protocol)",
            "10:20 - Dinamik Enerji Yük Kaydırma (Load Shifting) ile Milyon Dolarlık Tasarruf",
            "16:40 - Canlı Vaka: Karbon Vergisinden Kaçarken Kârlılığı Artıran Akıllı Tesis",
            "23:10 - Bölüm 4 Kapanış Sınavı: Operasyon ve Tedarik Zinciri Sertifikasyon Görevi"
        ],
        "udemy_outline_en": [
            "00:00 - Beyond Greenwashing: Why ESG Dictates Your Cost of Capital",
            "04:45 - Demystifying Scope 1, 2, and 3 Emissions under the GHG Protocol",
            "10:20 - Dynamic Grid Load Shifting: The Architecture of the Thermal Battery",
            "16:40 - Live Case Study: Evading Carbon Border Tariffs While Sashing OPEX",
            "23:10 - Part 4 Capstone Project: Operations & Supply Chain Leadership Certification"
        ]
    }
]
