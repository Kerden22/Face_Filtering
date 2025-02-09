import cv2
import mediapipe as mp
import numpy as np

COLOR = (255, 0, 0)
mp_face_detection = mp.solutions.face_detection

def process_frame(image, draw_box=True, filtre_türü=None):
    face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)
    image = cv2.flip(image, 1)
    annotated_image = image.copy()
    height, width, _ = image.shape
    coordinates = []
    results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            origin_x = int(bboxC.xmin * width)
            origin_y = int(bboxC.ymin * height)
            bbox_width = int(bboxC.width * width)
            bbox_height = int(bboxC.height * height)
            yüz_bölgesi = annotated_image[origin_y:origin_y + bbox_height, origin_x:origin_x + bbox_width]
            if filtre_türü == 'ortalama':
                yüz_bölgesi = cv2.blur(yüz_bölgesi, (15, 15))
            elif filtre_türü == 'median':
                yüz_bölgesi = cv2.medianBlur(yüz_bölgesi, 15)
            elif filtre_türü == 'gauss':
                yüz_bölgesi = cv2.GaussianBlur(yüz_bölgesi, (15, 15), 0)
            elif filtre_türü == 'sobel':
                yüz_bölgesi = cv2.Sobel(yüz_bölgesi, cv2.CV_64F, 1, 1, ksize=5)
                yüz_bölgesi = cv2.convertScaleAbs(yüz_bölgesi)
            elif filtre_türü == 'prewitt':
                kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
                kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
                yüz_bölgesi = cv2.filter2D(yüz_bölgesi, -1, kernelx) + cv2.filter2D(yüz_bölgesi, -1, kernely)
            elif filtre_türü == 'laplacian':
                yüz_bölgesi = cv2.Laplacian(yüz_bölgesi, cv2.CV_64F)
                yüz_bölgesi = cv2.convertScaleAbs(yüz_bölgesi)
            elif filtre_türü == 'bulanık':
                yüz_bölgesi = cv2.GaussianBlur(yüz_bölgesi, (99, 99), 30)
            annotated_image[origin_y:origin_y + bbox_height, origin_x:origin_x + bbox_width] = yüz_bölgesi
            coordinates.append((origin_x, origin_y, bbox_width, bbox_height))
            if draw_box:
                start_point = (origin_x, origin_y)
                end_point = (origin_x + bbox_width, origin_y + bbox_height)
                cv2.rectangle(annotated_image, start_point, end_point, COLOR, 3)
    return annotated_image, coordinates

cap = cv2.VideoCapture(0)
geçerli_filtre = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Hata: Çerçeve yakalanamadı.")
        break
    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):
        geçerli_filtre = 'ortalama'
    elif key == ord('2'):
        geçerli_filtre = 'median'
    elif key == ord('3'):
        geçerli_filtre = 'gauss'
    elif key == ord('4'):
        geçerli_filtre = 'sobel'
    elif key == ord('5'):
        geçerli_filtre = 'prewitt'
    elif key == ord('6'):
        geçerli_filtre = 'laplacian'
    elif key == ord('7'):
        geçerli_filtre = 'bulanık'
    annotated_image, _ = process_frame(frame, filtre_türü=geçerli_filtre)
    cv2.imshow("filtre gösterme başladı", annotated_image)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
