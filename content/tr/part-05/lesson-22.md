# Ders 22: Şirket Değerleme Metodolojileri: DCF, Çarpanlar ve AI Destekli Senaryo Simülasyonları

> **Bölüm 5: Finansal Yönetim, Değerleme & Sermaye Tahsisi (The Financial Leader & VP Finance)** | *Seviye 5: Finansal Liderlik / VP Finance*

---

### 📌 Kısa Özet & Zihniyet Dönüşümü
Bir şirketin değeri ne kasanın büyüklüğüdür ne de sahibinin hayalleridir. Bir işletmenin değeri; gelecekte üreteceği serbest nakit akışlarının (FCF) bugünkü net değeridir. İndirgenmiş Nakit Akışı (DCF), Çarpanlar (EBITDA, ARR katları) ve Monte Carlo simülasyonlarını yapay zeka ile harmanlayarak şirket değerlemelerini spekülasyondan çıkarıp bilimsel bir zemine oturtun.

---

### 💡 Aptala Anlatır Gibi (ELI5) & Eğlenceli Hikaye
> Bir şirketi satın almak, her yıl altın yumurtlayan bir tavuk satın almaya benzer. Tavuğun değeri, tavuğun tüylerinin güzelliği (ofis binaları) değildir; ömrü boyunca yumurtlayacağı altınların bugünkü parayla ne ettiğidir. Eğer tavuk her yıl 1 altın veriyorsa ve 5 yıl yaşayacaksa, ona 20 altın ödeyen kişi fena halde kazıklanmıştır!

---

### ⚖️ Eski Usul vs. AI Destekli Yaklaşım
| Konu / Boyut | Eski Usul (Legacy Business) | AI Destekli Modern Yaklaşım |
|---|---|---|
| **Değerleme Yaklaşımı** | Sektör dedikodularına veya yatırımcının keyfine göre kaba bir çarpan (Örn: 10x ARR) uydurmak. | İçsel Değerleme (DCF) ile Piyasa Çarpanlarını (Comps) birleştiren hibrit değerleme. |
| **İskonto Oranı (WACC)** | WACC oranını sabit bir varsayımla %10 alıp piyasa faiz oynaklığını unutmak. | Borç/Özsermaye maliyetini ve ülke risk primini AI ile anlık güncelleyerek dinamik WACC hesaplamak. |
| **Belirsizlik ve Risk Modelleme** | Sadece tek bir 'en iyi ihtimal' senaryosu çizipExcel'de kendini kandırmak. | 10.000 farklı ekonomik senaryoyu koşturan olasılıksal Monte Carlo AI simülasyonu. |

---

### 🚀 Adım Adım Eylem Çerçevesi (Actionable Framework)
- 1. Serbest Nakit Akışı (Unlevered FCF) Modelle: Faaliyet kârından vergiyi düş, amortismanı ekle, CapEx ve İşletme Sermayesi değişimini çıkar.
- 2. WACC Hesapla: Şirketin ağırlıklı ortalama sermaye maliyetini (Borç Maliyeti x Borç Oranı + Özkaynak Maliyeti x Özkaynak Oranı) belirle.
- 3. Uç Değer (Terminal Value) Tahmini: Şirketin sonsuza dek büyüme hızını (Gordon Growth) makul ülke büyüme oranına (%2-3) sabitle.
- 4. Monte Carlo Duyarlılık Matrisi: Büyüme oranı %2 düşer veya iskonto oranı %1 artarsa şirket değerinin ne olacağını ısı haritasında göster.

---

### 🚨 Gerçek Hayat Vaka / Kriz Analizi (War Story)
Bir lojistik yazılımı girişimi, Seri A turunda 'Biz geleceğin unicornuyuz, değerlememiz 50 milyon $' diyerek yatırımcı masasına oturdu. Yatırımcılar bu afaki rakamı reddetti ve görüşmeler tıkandı. Girişimin finans danışmanı, şirketin son 3 yıllık kohort verilerini ve geleceğe dönük UFCF projeksiyonlarını AI tabanlı bir DCF ve Monte Carlo motoruna döktü. Simülasyon, şirketin en olası içsel değerinin 32.4 milyon $ olduğunu, %80 güven aralığında 28M $ ile 36M $ arasında kaldığını kanıtladı. Girişim bu bilimsel raporu masaya koydu; VC fonu 32 milyon $ değerleme üzerinden 8 milyon $ yatırımı tereddütsüz imzaladı.

---

### 🤖 Kullanıma Hazır AI Promptları & Şablonlar
#### 🛠️ DCF Şirket Değerleme ve Monte Carlo Simülatörü
```text
Sen Goldman Sachs veya Morgan Stanley'de Baş Şirket Değerleme (M&A Valuation) Direktörüsün. Aşağıdaki şirket finansallarını incele: [GELİR, BÜYÜME, FAVÖK MARJI, CAPEX VE BORÇ DURUMU]. 1) Gelecek 5 yıllık Serbest Nakit Akışı (FCF) projeksiyonunu kur, 2) Şirket için uygun WACC iskonto oranını ve Terminal Değer çarpanını belirle, 3) Farklı büyüme ve iskonto senaryolarına göre şirketin değerleme aralığını (Bear, Base, Bull senaryoları) tablo halinde hesapla.
```

---

### 🎙️ NotebookLM Podcast Tartışma Komutu (Deep Dive Audio)
> **NotebookLM Audio Overview Komutu (Deep Dive 2-Speaker Script):**
> İki yatırım uzmanı: Biri kafadan çarpan uydurup şişirme değerlemelerle yatırımcıları kandırmaya çalışan bir hayal tüccarı, diğeri DCF ve Monte Carlo simülasyonlarıyla bir şirketin kuruşu kuruşuna içsel değerini hesaplayan usta değerleme mimarı. 'Şirket değerleme sanatı: Değerleme bir his midir yoksa nakit akışının bilimi midir?' konusunu eğlenceli ve derin bir sohbetle dinleyin.

---

### 🎓 Udemy Ders Özeti, Video Zaman Damgaları & Egzersiz
- 00:00 - Değerleme Yalanları: Çarpan Balonları Neden Patlar?
- 04:45 - Bir Şirketin İçsel Değeri (Intrinsic Value) ve FCF Mantığı
- 10:15 - Ağırlıklı Ortalama Sermaye Maliyeti (WACC) Nasıl Hesaplanır?
- 16:20 - Canlı Uygulama: AI ile Bir Şirketin 5 Yıllık DCF Modelini Kurmak
- 22:45 - Eylem Görevi: Kendi İşletmenin veya Bir Halka Açık Şirketin Değerlemesini Yap
