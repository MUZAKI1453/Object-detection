# import library openCV
import cv2

# membuka kamera dengan openCV
cap = cv2.VideoCapture(0)

# cek apakah kamera terbuka dengan benar
if not cap.isOpened():
    print("tidak dapat membuka kamera")
    exit()

while True:
    # membaca frame dari kamera
    ret, frame = cap.read()

    # jika frame berhasil dibaca
    if not ret:
        print("tidak dapat membaca frame")
        break

    # menampilkan frame pada jendela
    cv2.imshow("Kamera", frame)

    # menunggu input dari keyboard, jika tombol 'q' ditekan maka keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# menutup kamera dan jendela setelah selesai
cap.release()
cv2.destroyAllWindows()