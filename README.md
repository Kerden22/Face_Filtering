
# Gerçek Zamanlı Yüz Filtreleme Uygulaması

Bu proje, OpenCV ve MediaPipe kütüphanelerini kullanarak gerçek zamanlı yüz algılama ve çeşitli filtre uygulama işlemlerini gerçekleştirir. Web kamerasından alınan canlı görüntü üzerinde, tespit edilen yüzlere kullanıcı tarafından seçilebilen farklı filtreler uygulanır.

## Özellikler

- **Gerçek Zamanlı Yüz Algılama:** MediaPipe yüz algılama modülü sayesinde yüzler anlık olarak tespit edilir.
- **Çeşitli Görüntü Filtreleri:** Uygulama üzerinde aşağıdaki filtreler arasında seçim yapabilirsiniz:
  - Ortalama Filtre
  - Medyan Filtre
  - Gauss Filtre
  - Sobel Filtre
  - Prewitt Filtre
  - Laplacian Filtre
  - Geniş Bulanıklaştırma
- **Canlı Video Akışı:** Web kamerasından alınan görüntü üzerinde anlık işlemler gerçekleştirilir.
- **Klavye ile Kolay Kontrol:** Belirli tuşlara basarak filtreleri değiştirebilir ve uygulamayı sonlandırabilirsiniz.

## Gereksinimler

- Python 3.x
- [OpenCV](https://opencv.org/) (`opencv-python`)
- [MediaPipe](https://mediapipe.dev/)
- [NumPy](https://numpy.org/)
