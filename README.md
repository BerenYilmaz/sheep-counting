# Şablon Eşleştirme ile Koyun Sayımı

OpenCV şablon eşleştirmesiyle bir görüntüdeki benzer koyun şekillerini bulur. Ek scriptler renk kanallarını, negatif görüntüleri ve histogramları inceler. Bu çalışma öğrenilmiş bir nesne tespit modeli kullanmaz.

## Kurulum ve çalıştırma

Görseller depo kökünde olduğu için komutları **depo kökünden** çalıştırın:

```powershell
python -m pip install -r requirements.txt
python findSheep.py
python grayScale.py
python histogramGrayScale.py
```

## Algoritma

`findSheep.py`, `images2.jpeg` ve `template2.jpeg` dosyalarını gri tonlamalı okur. Şablonun normal ve ters çevrilmiş yoğunluk değerleriyle `TM_CCOEFF_NORMED` eşleştirmesi yapar ve her konumda daha yüksek skoru seçer. `0.5` eşiğini geçen adaylar arasından hem x hem y farkı `25` pikselden küçük olan yakın eşleşmeler elenir. Kalan noktalar kutularla gösterilir ve sayıları konsola yazdırılır. Pencereleri kapatmak için bir tuşa basın.

## Diğer uygulamalar

| Script | İşlev | Girdi |
|---|---|---|
| `grayScale.py` | B, G ve R kanallarını ayrı gri görüntüler olarak gösterir | `images2.jpeg` |
| `histogramGrayScale.py` | Kanal histogramlarını normalize ederek çizer | `images2.jpeg` |
| `negative.py` | Her kanalın `255 - kanal` negatifini gösterir | `example1.jpeg` |

`example1.jpeg` kaynak klasörde bulunmadığından depoda yoktur. `negative.py` çalıştırmadan önce depo köküne bu isimde bir görsel koyun veya scriptteki yolu mevcut bir görsele değiştirin.

## Sınırlamalar

Şablon eşleştirme ölçek, açı ve arka plan değişimlerine duyarlıdır; eşik ve mesafe değerleri görüntüye göre ayarlanmalıdır. Yakın adayları eleme işlemi basit konumsal bir filtredir, IoU tabanlı NMS değildir. Histogram scriptindeki `cv.calcHist(image, ...)` çağrısı orijinal haliyle korunmuştur; histogramları analiz amacıyla kullanmadan önce OpenCV'nin beklediği görüntü listesi biçimiyle (`[image]`) doğrulayın.
