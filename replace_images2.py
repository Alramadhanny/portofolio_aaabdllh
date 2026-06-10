import re

file_path = "report.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    "26_kode_create_blade_1.png": "[Placeholder Image: Kode form input di create.blade.php part 1]",
    "27_kode_create_blade_2.png": "[Placeholder Image: Kode form input di create.blade.php part 2]",
    "28_kode_action_create.png": "[Placeholder Image: Kode action create di UserController]",
    "29_tampilan_form_create.png": "[Placeholder Image: Tampilan form input user]",
    "30_kode_action_index.png": "[Placeholder Image: Kode action index di UserController]"
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
