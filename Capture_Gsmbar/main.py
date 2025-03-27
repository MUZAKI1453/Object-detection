import cv2

# Membuka kamera
cap = cv2.VideoCapture(0)

# Cek apakah kamera terbuka
if not cap.isOpened():
    print("Tidak dapat membuka kamera")
    exit()

while True:
    # Membaca frame dari kamera
    ret, frame = cap.read()

    # Jika frame berhasil dibaca
    if not ret:
        print("Tidak dapat membaca frame")
        break

    # Menampilkan frame pada jendela
    cv2.imshow('Kamera', frame)

    # Menunggu input dari keyboard, jika tombol 'c' ditekan maka capture gambar
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):  # Jika tombol 'c' ditekan
        # Menyimpan gambar yang sedang ditampilkan
        cv2.imwrite('captured_image.jpg', frame)
        print("Gambar telah disimpan sebagai 'captured_image.jpg'")

    # Menunggu tombol 'q' untuk keluar dari program
    elif key == ord('q'):
        break

# Menutup kamera dan jendela setelah selesai
cap.release()
cv2.destroyAllWindows()
