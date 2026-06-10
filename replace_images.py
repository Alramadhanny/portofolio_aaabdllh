import re

file_path = "report.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    "01_login_default.png": "[Placeholder Image: Halaman Login Default]",
    "02_register_default.png": "[Placeholder Image: Halaman Register Default]",
    "03_home_after_login.png": "[Placeholder Image: Halaman Home setelah login]",
    "04_form_edit_user.png": "[Placeholder Image: Tampilan form edit user]",
    "05_env_database.png": "[Placeholder Image: Konfigurasi .env Database]",
    "06_composer_require_ui.png": "[Placeholder Image: Terminal composer require laravel/ui]",
    "07_php_artisan_ui_bootstrap.png": "[Placeholder Image: Terminal php artisan ui bootstrap --auth]",
    "08_php_artisan_migrate.png": "[Placeholder Image: Terminal hasil migrate auth]",
    "09_folder_migrations.png": "[Placeholder Image: File costum_table_users.php]",
    "10_code_costum_table_users.png": "[Placeholder Image: Kode costum_table_users]",
    "11_struktur_tabel_users_lama.png": "[Placeholder Image: Struktur tabel users lama]",
    "12_struktur_tabel_users_baru.png": "[Placeholder Image: Struktur tabel users baru]",
    "13_kode_adminseeder.png": "[Placeholder Image: Kode AdminSeeder]",
    "14_output_db_seed.png": "[Placeholder Image: Terminal hasil seeder AdminSeeder]",
    "15_kode_login_awal.png": "[Placeholder Image: Kode app.blade.php part 1]",
    "16_kode_login_form.png": "[Placeholder Image: Kode app.blade.php part 2]",
    "17_kode_login_script.png": "[Placeholder Image: Kode app.blade.php part 3]",
    "18_tampilan_login_baru.png": "[Placeholder Image: Tampilan halaman login SB Admin 2]",
    "19_kode_main_awal.png": "[Placeholder Image: Kode main.blade.php part 1]",
    "20_kode_main_footer.png": "[Placeholder Image: Kode main.blade.php part 2]",
    "21_kode_main_modal.png": "[Placeholder Image: Kode main.blade.php part 3]",
    "22_tampilan_dashboard.png": "[Placeholder Image: Tampilan halaman home SB Admin 2]",
    "23_terminal_usercontroller.png": "[Placeholder Image: Terminal make:controller UserController]",
    "24_kode_usercontroller_1.png": "[Placeholder Image: Kode UserController part 1]",
    "25_kode_usercontroller_2.png": "[Placeholder Image: Kode UserController part 2]"
}

for img_file, placeholder_text in replacements.items():
    # Find the div that contains this placeholder
    # <div class="report-image-placeholder"><span>[Placeholder Image: ...]</span></div>
    
    # We will replace the whole div
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
