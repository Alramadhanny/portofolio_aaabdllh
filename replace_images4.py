import re

file_path = "report.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    "36_kode_action_update.png": "[Placeholder Image: Kode action update di UserController]",
    "38_proses_update_user_2.png": "[Placeholder Image: Proses update user input form]",
    "39_tampilan_users_update_success.png": "[Placeholder Image: Tampilan halaman users setelah update success]",
    "40_kode_tombol_hapus.png": "[Placeholder Image: Kode tombol hapus di index.blade.php]"
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
