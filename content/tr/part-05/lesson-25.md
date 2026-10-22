# Ders 25: Risk Yönetimi ve Türev Araçlar: Kur, Enflasyon ve Piyasa Şoklarına Karşı AI Koruma Kalkanı

> **Bölüm 5: Finansal Yönetim, Değerleme & Sermaye Tahsisi (The Financial Leader & VP Finance)** | *Seviye 5: Finansal Liderlik / VP Finance*

---

### 📌 Kısa Özet & Zihniyet Dönüşümü
Döviz kurlarındaki bir gecelik sıçrama, emtia fiyatlarındaki patlama veya faiz şokları; yıllardır başarıyla yönetilen bir şirketi haftalar içinde iflasa sürükleyebilir. Türev araçları (Forward, Futures, Opsiyonlar) ve yapay zeka destekli Risk Değeri (Value at Risk - VaR) modellerini kullanarak, şirketin bilançosunu öngörülemez makroekonomik fırtınalara karşı zırh gibi koruyun.

---

### 💡 Aptala Anlatır Gibi (ELI5) & Eğlenceli Hikaye
> Türev araçlarla risk yönetimi (Hedging), tatile çıkarken yağmur yağma ihtimaline karşı küçük bir şemsiye parası ödemeye benzer. Hava güneşli kalırsa şemsiyeye verdiğin küçük para yanar ama tatilin güzel geçer; eğer şiddetli bir fırtına koparsa, o şemsiye seni zatürre olmaktan ve hastaneye düşmekten kurtarır!

---

### ⚖️ Eski Usul vs. AI Destekli Yaklaşım
| Konu / Boyut | Eski Usul (Legacy Business) | AI Destekli Modern Yaklaşım |
|---|---|---|
| **Makroekonomik Risk Duruşu** | Kadercilik: 'Döviz yükselirse zam yaparız, yapacak bir şey yok' tembelliği. | Proaktif Korunma (Hedging): Kur ve faiz riskini türev kontratlarla önceden kilitlemek. |
| **Risk Ölçüm Yöntemi** | Sadece sezgilere ve televizyondaki yorumcuların tahminlerine göre hareket etmek. | Riske Maruz Değer (VaR) ve stres testi senaryolarını günlük simüle etmek. |
| **Bilanço Dayanıklılığı** | Açık pozisyon taşıyıp devalüasyon gecelerinde kabus görmek. | Doğal korunma (Natural Hedge) ve finansal türevleri harmanlayan zırhlı bilanço. |

---

### 🚀 Adım Adım Eylem Çerçevesi (Actionable Framework)
- 1. Net Açık Pozisyonu Haritala: Döviz cinsinden varlıkların ile borçların arasındaki farkı (Döviz Pozisyon Açığı) netleştir.
- 2. Doğal Korunma (Natural Hedge) Uygula: Mümkünse döviz borcun varsa döviz cinsi ihracat gelirlerini artırarak riski sıfırla.
- 3. Finansal Korunma (Forward & Opsiyonlar): Kalan açık risk için vadeli forward anlaşması yap veya aşağı yönlü riski sınırlayan Put opsiyonu satın al.
- 4. Riske Maruz Değer (VaR) Limiti: Şirket yönetim kurulunun onayladığı maksimum günlük kayıp eşiğini belirle; aşılırsa otomatik hedge pozisyonu aç.

---

### 🚨 Gerçek Hayat Vaka / Kriz Analizi (War Story)
Türkiye'de faaliyet gösteren büyük bir kimya üreticisi, hammaddelerini euro ile ithal edip iç pazara TL ile vadeli satıyordu. Şirketin 12 milyon euro döviz açığı vardı. Yeni Finans Direktörü (Treasury VP), AI destekli makro senaryo analizinde dövizde ani bir dalgalanma riskini yüksek gördü. Şirket genel müdürünü ikna ederek açığın %75'ini vadeli forward sözleşmeleriyle sabitledi. İki ay sonra kurda beklenmedik bir devalüasyon şoku yaşandı ve kur %35 fırladı. Sektördeki rakipler devasa kur zararları yazıp konkordato ilan ederken; bu üretici forward sözleşmesi sayesinde hammaddeyi kriz öncesi fiyattan aldı, pazar payını ikiye katladı ve yılı rekor kârla kapattı.

---

### 🤖 Kullanıma Hazır AI Promptları & Şablonlar
#### 🛠️ Hazine Direktörü ve Kurumsal Risk Kalkanı Mimarı
```text
Sen dünyanın en büyük yatırım bankalarından birinin Kurumsal Hazine ve Risk Yönetimi Direktörüsün (Head of Corporate Treasury). Şirketimizin şu bilanço ve piyasa risklerini incele: [DÖVİZ BORCU, GELİR DAĞILIMI, EMTAİ GİRDİLERİ VE FAİZ YAPISI]. 1) Bu şirketin Net Döviz ve Emtia Pozisyon Açığını analiz et, 2) Şirketi batmaktan koruyacak en maliyet etkin Korunma (Hedging) stratejisini (Forward, Opsiyon veya Doğal Hedge) kurgula, 3) Dövizin %25 artması veya hammadde fiyatının %30 fırlaması durumunda şirketin nakit akışını koruyacak eylem planını yaz.
```

---

### 🎙️ NotebookLM Podcast Tartışma Komutu (Deep Dive Audio)
> **NotebookLM Audio Overview Komutu (Deep Dive 2-Speaker Script):**
> İki finans lideri: Biri kur ve faiz riskine karşı hiçbir önlem almayıp devalüasyon gecesinde şirketi batıran kumarbaz ruhlu patron, diğeri türev araçlar ve yapay zeka risk modelleriyle şirketin bilançosuna çelik bir zırh giydiren usta risk direktörü. 'Risk yönetimi kumar değil, hayatta kalma kalkanıdır' konusunu nefes kesen bir finansal kriz hikayesiyle tartışın.

---

### 🎓 Udemy Ders Özeti, Video Zaman Damgaları & Egzersiz
- 00:00 - Bir Gecede Şirket Batıran Makro Şoklar: Devalüasyon ve Enflasyon
- 04:50 - Riske Maruz Değer (Value at Risk - VaR) Nedir ve Nasıl Hesaplanır?
- 10:15 - Türev Araçlar Cephaneliği: Forward, Futures, Opsiyonlar ve Swapr
- 16:20 - Canlı Vaka: 12 Milyon Euroluk Döviz Açığını Sıfır Maliyetli Yaka (Collar) ile Korumak
- 22:50 - Bölüm 5 Kapanış Sınavı: Finansal Yönetim ve Değerleme Sertifikasyon Görevi
