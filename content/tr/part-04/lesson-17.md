# Ders 17: Akıllı Tedarik Zinciri ve Lojistik: Talep Tahminleme, Stok Optimizasyonu ve Risk Modelleme

> **Bölüm 4: Operasyonlar, Tedarik Zinciri & Yalın Süreçler (The Operations & Supply Chain Leader)** | *Seviye 4: Operasyon & Tedarik / Operations Director*

---

### 📌 Kısa Özet & Zihniyet Dönüşümü
Depolarda çürüyen atıl stoklar ile rafların boş kalması arasındaki ince çizgi, bir tedarik zincirinin kaderidir. Tarihsel verilere dayanan kör tahminleri bırakın; hava durumu, jeopolitik riskler, sosyal trendler ve makroekonomik sinyalleri birleştiren çok değişkenli AI modelleri ile 'Tam Zamanında' (Just-in-Time) değil, 'Her İhtimale Karşı Dayanıklı' (Just-in-Case Resilient) tedarik zincirleri kurun.

---

### 💡 Aptala Anlatır Gibi (ELI5) & Eğlenceli Hikaye
> Eski tedarik zinciri, araba kullanırken sadece dikiz aynasına bakmaya benzer; arkada ne gördüysen önünde de o var sanırsın ve virajı kaçırıp kaza yaparsın. Akıllı AI tedarik zinciri ise arabanın tepesindeki radar ve GPS gibidir: 10 kilometre ilerideki sisi, kayganlaşan yolu ve trafiği önceden görüp sana hızını ve rotanı anında ayarlar.

---

### ⚖️ Eski Usul vs. AI Destekli Yaklaşım
| Konu / Boyut | Eski Usul (Legacy Business) | AI Destekli Modern Yaklaşım |
|---|---|---|
| **Talep Tahmini (Forecasting)** | Geçen yılın satış rakamına %10 ekleyip Excel'de kaba tahminler yapmak. | Sosyal medya ilgisi, hava durumu, döviz kuru ve enflasyonu harmanlayan dinamik AI tahmini. |
| **Güvenlik Stoğu (Safety Stock)** | Korkudan depoyu gereksiz mallarla doldurup işletme sermayesini kilitlemek. | Olasılıksal talep eğrileriyle her SKU için dinamik ve optimize edilmiş güvenlik stoğu. |
| **Jeopolitik & Lojistik Risk** | Süveyş Kanalı tıkandığında veya kriz çıktığında çaresizce beklemek. | Tedarikçileri tek coğrafyaya bağlamayan, AI ile önceden alternatif rota simüle eden çoklu kaynak. |

---

### 🚀 Adım Adım Eylem Çerçevesi (Actionable Framework)
- 1. Kamçı Etkisi (Bullwhip Effect) Teşhisi: Müşteri talebindeki küçük bir dalgalanmanın fabrikada devasa stok krizine dönüşmesini engelle.
- 2. SKU Bazlı ABC/XYZ Sınıflandırması: Ürünlerini hem ciro etkisine (A-B-C) hem de talep tahmin edilebilirliğine (X-Y-Z) göre matrise dök.
- 3. Tedarikçi Dayanıklılık Skoru: Her tedarikçinin teslim süresi sapmalarını AI ile puanla; güvenilmez ortaklara bağımlılığı azalt.
- 4. Dinamik Sipariş Noktası (ROP): Sabit sipariş günlerini kaldır; stok seviyesi kritik eşiğe geldiğinde sistemin otonom sipariş açmasını sağla.

---

### 🚨 Gerçek Hayat Vaka / Kriz Analizi (War Story)
Bir kış giyim markası, her yıl sonu 3 milyon dolarlık satılmayan mont stokuyla baş başa kalıyordu çünkü tahminler sadece önceki yılın satışlarına bakıyordu. Yeni tedarik zinciri direktörü, meteoroloji verilerini ve mikro-bölgesel soğuma modellerini satış verileriyle birleştiren bir AI talep motoru kurdu. Model, Doğu Anadolu'da kışın erken geleceğini, Batı'da ise pastırma yazı yaşanacağını öngörerek stok sevkiyatlarını yeniden planladı. Sezon sonunda stok fazlası %72 azaldı ve şirket 1.4 milyon $ nakit tasarrufu elde etti.

---

### 🤖 Kullanıma Hazır AI Promptları & Şablonlar
#### 🛠️ Tedarik Zinciri Risk Analisti ve Dinamik Stok Mimarı
```text
Sen Fortune 500 şirketlerinin Baş Tedarik Zinciri Yöneticisisin (CSCO). Aşağıdaki ürün ve tedarikçi bilgilerini incele: [ÜRÜN, TEDARİKÇİ VE TESLİMAT VERİSİ]. 1) Bu tedarik ağındaki en kritik 2 tekil arıza noktasını (Single Point of Failure) ve kamçı etkisi riskini belirle, 2) Stok maliyetini %30 düşürürken 'Yok Satma' (Stockout) riskini sıfıra yakın tutacak dinamik bir Güvenlik Stoğu formülü öner, 3) Kızıldeniz veya Süveyş benzeri bir kriz için 48 saatlik acil B planı hazırla.
```

---

### 🎙️ NotebookLM Podcast Tartışma Komutu (Deep Dive Audio)
> **NotebookLM Audio Overview Komutu (Deep Dive 2-Speaker Script):**
> İki lojistik uzmanı: Biri depoyu satılmayan mallarla doldurup şirket kasasını kilitleyen eski kafa lojistikçi, diğeri hava durumu ve pazar verilerini yapay zekayla okuyarak sıfır atıkla çalışan tedarik zinciri dehası. 'Kamçı etkisi nedir ve modern şirketler stok krizlerinden nasıl kaçınır?' konusunu sürükleyici bir vaka ile tartışın.

---

### 🎓 Udemy Ders Özeti, Video Zaman Damgaları & Egzersiz
- 00:00 - Tedarik Zincirinin Sessiz Katili: Kamçı Etkisi (Bullwhip Effect)
- 04:50 - 'Tam Zamanında' (JIT) Modelinin Çöküşü ve Dayanıklı Tedarik Zincirleri
- 10:15 - ABC/XYZ Matrisi ile Akıllı Stok Sınıflandırması
- 16:30 - Canlı Uygulama: Hava Durumu ve Trendleri Birleştiren AI Talep Tahmini
- 22:50 - Eylem Görevi: Kendi Şirketinin Tedarikçi Bağımlılık Haritasını Çıkar
