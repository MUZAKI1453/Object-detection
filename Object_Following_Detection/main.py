"""
object detection menggunakan YOLO (You Only Look Once) untuk mendeteksi objek pada
gambar atau video secara real time
"""

# import library
from ultralytics import YOLO
import cv2

# Load the YOLO model
model = YOLO('yolov8n.pt') # yolov8n.pt adalah fiule model yang sudah dilatih sebelumnya

# Loop untuk menangkap setiap frame video
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Deteksi objek dengan model yolo
    results = model(frame)

    # Menampilkan hasil deteksi
    boxes = results[0].boxes  # Kotak pembatas dari hasil deteksi
    for box in boxes:
        # Dapatkan koordinat xywh dan confidences (kepercayaan) untuk tiap objek
        x, y, w, h = box.xywh[0]  # Kotak pembatas (x, y, width, height)
        confidence = box.conf[0]   # Kepercayaan dari deteksi

        # Gambar kotak di atas objek yang terdeteksi
        cv2.rectangle(frame, (int(x - w / 2), int(y - h / 2)),
                      (int(x + w / 2), int(y + h / 2)), (0, 255, 0), 2)

    # Tampilkan hasil di jendela
    cv2.imshow('Object Detection', frame)

    # Keluar jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# melepaskan kamera dan menutup jendela
cap.release()
cv2.destroyAllWindows()
