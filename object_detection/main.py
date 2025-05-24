import os, shutil
from ultralytics import YOLO
import cv2

MODEL_PATH = "yolov8n.pt"             # gunakan model pretrained dari YOLOv8
INPUT_FOLDER = r"D:/Python/Botol"     # folder untuk gambar input
OUTPUT_FOLDER = r"D:/Python/hasil"     # folder untuk menyimpan hasil

def detect_objects():
    # load model YOLOv8
    model = YOLO(MODEL_PATH)

    if os.path.exists(OUTPUT_FOLDER):
        shutil.rmtree(OUTPUT_FOLDER) # hapus folder output sebelumnya bila ada
        os.makedirs(OUTPUT_FOLDER)   # kemudian membuat folder menyimpan hasil / hasil yang baru

    for image_name in os.listdir(INPUT_FOLDER):
        input_path = os.path.join(INPUT_FOLDER, image_name)
        output_path = os.path.join(OUTPUT_FOLDER, image_name)

        # memastikan hanya file gambar yang diproses
        if not input_path.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        # deteksi objek pada gambar
        results = model.predict(input_path, conf=0.5, save=False)

        # simpan hasil deteksi ke file baru
        for result in results:
            filtered_boxes = []
            for box in result.boxes:
                class_id = int(box.cls) # id kelas deteksi
                if model.names[class_id] =="bottle": # cek hanya objek botol yang terdeteksi
                    filtered_boxes.append(box)
            # jika tidak ada botol yang terdeteksi, lanjutkan ke gambar berikutnya
            if not filtered_boxes:
                print(f"Tidak ada yang terdeteksi di: {image_name}")
                continue

            annotated_image = result.plot(boxes=filtered_boxes) # gambar hasil deteksi
            cv2.imwrite(output_path, annotated_image)
            print(f"hasil deteksi disimpan ke: {output_path}")


if __name__ == "__main__":
    detect_objects()