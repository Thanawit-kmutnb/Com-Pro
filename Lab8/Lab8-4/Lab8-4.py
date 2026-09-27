import os

def process_directory(dir_path):
    if not os.path.exists(dir_path):
        print(f"ไม่พบโฟลเดอร์: {dir_path}")
        return

    all_entries = os.listdir(dir_path)
    
    total_all_size = 0
    total_image_size = 0
    
    image_extensions = ('.jpg', '.jpeg', '.gif', '.png')
    image_files_list = []

    print("=== 1. รายชื่อไฟล์ทั้งหมด ===")
    for name in all_entries:
        full_path = os.path.join(dir_path, name)

        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            total_all_size += size
            print(f"- {name} (ขนาด: {size:,} bytes)")

            if name.lower().endswith(image_extensions):
                image_files_list.append((name, size))
                total_image_size += size

    print(f"\n--> ขนาดรวมของไฟล์ทั้งหมด: {total_all_size:,} bytes\n")

    print("=== 2. รายชื่อเฉพาะไฟล์รูปภาพ (Binary Files) ===")
    for img_name, img_size in image_files_list:
        print(f"- {img_name} (ขนาด: {img_size:,} bytes)")
        
    print(f"\n--> ขนาดรวมของไฟล์รูปภาพทั้งหมด: {total_image_size:,} bytes")

# ให้ target_directory ชี้ไปยังโฟลเดอร์ที่ไฟล์ .py นี้ตั้งอยู่โดยตรง
target_directory = os.path.dirname(__file__)

process_directory(target_directory)