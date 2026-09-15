import zipfile
import os

zip_path = r"D:\Dhan'sky\Tugas\Semester 5\Aplikasi Mobile\Laprak\gambar.zip"
extract_path = r"D:\Dhan'sky\penting\27\portofolio_aaabdllh-main - Copy\gambar_aplikasi_mobile"

os.makedirs(extract_path, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
    print(f'Extracted {len(zip_ref.namelist())} files to {extract_path}')
    print('\nFiles in zip:')
    for name in zip_ref.namelist():
        print(f'  - {name}')
