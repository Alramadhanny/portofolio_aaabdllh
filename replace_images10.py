import re

file_path = "report.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Using a flexible regex that allows newlines and spacing anywhere inside the placeholder span/div
pattern = r'<div class="report-image-placeholder">\s*<span>\s*\[\s*Placeholder Image:\s*Kode Select2 di main\.blade\.php\s*\]\s*</span>\s*</div>'
replacement = '<div class="report-image-container"><img src="images/report_laravel/58_kode_select2.png" alt="Kode Select2 di main.blade.php" class="report-screenshot"></div>'

content, count = re.subn(pattern, replacement, content, flags=re.DOTALL | re.IGNORECASE)

if count == 0:
    print(f"Warning: Could not find Placeholder")
else:
    print(f"Replaced {count} instance(s)")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done.")
