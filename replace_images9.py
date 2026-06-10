import re

file_path = "report.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    "[Placeholder Image: Kode tombol edit di index.blade.php]": '<div class="report-image-container"><img src="images/report_laravel/56_kode_tombol_edit.png" alt="Kode tombol edit di index.blade.php" class="report-screenshot"></div>',
    "[Placeholder Image: Tampilan list user]": '<div class="report-image-container"><img src="images/report_laravel/57_tampilan_list_user.jpg" alt="Tampilan list user" class="report-screenshot"></div>'
}

for placeholder_text, replacement in replacements.items():
    pattern = r'<div class="report-image-placeholder">\s*<span>' + re.escape(placeholder_text) + r'</span>\s*</div>'
    
    content, count = re.subn(pattern, replacement, content)
    if count == 0:
        print(f"Warning: Could not find {placeholder_text}")
    else:
        print(f"Replaced {placeholder_text}")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done.")
