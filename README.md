# �ablon E�le�tirme ile Koyun Say�m�

OpenCV �ablon e�le�tirmesiyle bir g�r�nt�deki benzer koyun �ekillerini bulur. Ek scriptler renk kanallar�n�, negatif g�r�nt�leri ve histogramlar� inceler. Bu �al��ma ��renilmi� bir nesne tespit modeli kullanmaz.

## Kurulum ve �al��t�rma

G�rseller depo k�k�nde oldu�u i�in komutlar� **depo k�k�nden** �al��t�r�n:

```powershell
python -m pip install -r requirements.txt
python findSheep.py
python grayScale.py
python histogramGrayScale.py
```

## Algoritma

`findSheep.py`, `images2.jpeg` ve `template2.jpeg` dosyalar�n� gri tonlamal� okur. �ablonun normal ve ters �evrilmi� yo�unluk de�erleriyle `TM_CCOEFF_NORMED` e�le�tirmesi yapar ve her konumda daha y�ksek skoru se�er. `0.5` e�i�ini ge�en adaylar aras�ndan hem x hem y fark� `25` pikselden k���k olan yak�n e�le�meler elenir. Kalan noktalar kutularla g�sterilir ve say�lar� konsola yazd�r�l�r. Pencereleri kapatmak i�in bir tu�a bas�n.

## Di�er uygulamalar

| Script | ��lev | Girdi |
|---|---|---|
| `grayScale.py` | B, G ve R kanallar�n� ayr� gri g�r�nt�ler olarak g�sterir | `images2.jpeg` |
| `histogramGrayScale.py` | Kanal histogramlar�n� normalize ederek �izer | `images2.jpeg` |
| `negative.py` | Her kanal�n `255 - kanal` negatifini g�sterir | `example1.jpeg` |

`example1.jpeg` kaynak klas�rde bulunmad���ndan depoda yoktur. `negative.py` �al��t�rmadan �nce depo k�k�ne bu isimde bir g�rsel koyun veya scriptteki yolu mevcut bir g�rsele de�i�tirin.

## S�n�rlamalar

�ablon e�le�tirme �l�ek, a�� ve arka plan de�i�imlerine duyarl�d�r; e�ik ve mesafe de�erleri g�r�nt�ye g�re ayarlanmal�d�r. Yak�n adaylar� eleme i�lemi basit konumsal bir filtredir, IoU tabanl� NMS de�ildir. Histogram scriptindeki `cv.calcHist(image, ...)` �a�r�s� orijinal haliyle korunmu�tur; histogramlar� analiz amac�yla kullanmadan �nce OpenCV'nin bekledi�i g�r�nt� listesi bi�imiyle (`[image]`) do�rulay�n.
