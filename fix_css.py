file_path = "style.css"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the broken CSS
broken_css = """.report-challenge-list,
.report-objective-list {
    padding-left: 24px;
}
}

.report-code-line code,"""

fixed_css = """.report-challenge-list,
.report-objective-list {
    padding-left: 24px;
}

.report-tools-list {
    padding-left: 22px;
}

.report-code-line,
.report-code-block {
    margin-top: 25px;
    margin-bottom: 25px;
    padding: 12px 14px;
    border-radius: var(--radius-std);
    background-color: #0f172a;
    color: #f8fafc;
    overflow-x: auto;
}

.report-code-line code,"""

if broken_css in content:
    content = content.replace(broken_css, fixed_css)
    print("Fixed broken CSS.")
else:
    print("Broken CSS not found.")

# Add heading overrides
additions = """

/* --- Report Detail Spacing Adjustments --- */
.report-detail-content h3, 
.report-detail-content h4, 
.report-detail-content h5 {
    margin-top: 40px;
    margin-bottom: 15px;
}

.report-detail-content p {
    margin-bottom: 20px;
}

.report-code-line,
.report-code-block {
    margin-top: 25px !important;
    margin-bottom: 25px !important;
}

.report-image-container {
    margin-top: 30px !important;
    margin-bottom: 30px !important;
}
"""

if "/* --- Report Detail Spacing Adjustments --- */" not in content:
    content += additions
    print("Added overrides.")
else:
    print("Overrides already exist.")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
