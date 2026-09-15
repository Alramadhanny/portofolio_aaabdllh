import pdfplumber

pdf_path = r"D:\Dhan'sky\Tugas\Semester 5\Aplikasi Mobile\Laprak\Laporan Praktikum 1_Aplikasi Mobile_ Abdullah Al Ramadhani_2411533016.pdf"

with pdfplumber.open(pdf_path) as pdf:
    print(f'Total halaman: {len(pdf.pages)}')
    print('='*80)
    # Baca 5 halaman pertama untuk memahami isinya
    for i, page in enumerate(pdf.pages[:5]):
        text = page.extract_text()
        if text:
            print(f'\n--- Halaman {i+1} ---')
            print(text[:2000] if len(text) > 2000 else text)
