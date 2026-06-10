import re

file_path = "report.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    "[Placeholder Image: Kode import css &amp; js datatables]": '<div class="report-image-container"><img src="images/report_laravel/54_kode_css_datatables.png" alt="Kode import css datatables" class="report-screenshot" style="margin-bottom: 10px;"><br><img src="images/report_laravel/55_kode_js_datatables.png" alt="Kode import js datatables" class="report-screenshot"></div>'
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
