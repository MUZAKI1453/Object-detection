import cv2
import mediapipe as mp

# inisialisasi mediapipe pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# membuka webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # konversi gambar ke rgb
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Proses gambar dengan mediapipe pose
    results = pose.process(image_rgb)

    # Gambar landmark jika terdeteksi
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # tampilkan gambar
    cv2.imshow('Pose Estimation', frame)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# tutup webcam dan jedela
cap.release()
cv2.destroyAllWindows()
