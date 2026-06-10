import re

file_path = "report.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    "41_kode_action_destroy.png": "[Placeholder Image: Kode action destroy di UserController]",
    "42_popup_konfirmasi_hapus.png": "[Placeholder Image: Tampilan popup konfirmasi hapus]",
    "43_tampilan_users_setelah_hapus.png": "[Placeholder Image: Tampilan halaman users setelah berhasil hapus]",
    "44_kode_menu_sidebar.png": "[Placeholder Image: Kode menu user di sidebar.blade.php]",
    "45_tampilan_sidebar.png": "[Placeholder Image: Tampilan sidebar dengan menu Users]"
}

for img_file, placeholder_text in replacements.items():
    pattern = r'<div class="report-image-placeholder">\s*<span>' + re.escape(placeholder_text) + r'</span>\s*</div>'
    replacement = f'<div class="report-image-container"><img src="images/report_laravel/{img_file}" alt="{placeholder_text.replace("[Placeholder Image: ", "").replace("]", "")}" class="report-screenshot"></div>'
    
    content, count = re.subn(pattern, replacement, content)
    if count == 0:
        print(f"Warning: Could not find {placeholder_text}")
    else:
        print(f"Replaced {placeholder_text}")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done.")
