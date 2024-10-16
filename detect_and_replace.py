import re
import os

# Function to perform the replacements
def replace_shorthands_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        original_content = file.read()

    # Copy the original content
    content = original_content

    # Define the replacements as patterns
    replacements = {
        r"var\(--main-color\)": "$main-color",            # Detect var(--main-color)
        r"var\(--hover-color\)": "$hover-color",          # Detect var(--hover-color)
        r"var\(--text-normal\)": "$text-normal",          # Detect var(--text-normal)
        r"var\(--background-shading\)": "$bg-shading",    # Detect var(--background-shading)
        r"cv\('colors\.main'\)": "$main-color",           # Detect cv('colors.main')
        r"cv\('colors\.hover'\)": "$hover-color",         # Detect cv('colors.hover')
        r"cv\('bg\.app\.shading'\)": "$bg-shading",       # Detect cv('bg.app.shading')
        r"calc\(\#\{cv\('bg\.app\.shading'\)\} \* (\d*\.?\d+)\)": r"calc($bg-shading * \1)"  # Detect calc(#{cv('bg.app.shading')} * 0.6)
    }

    # Apply all replacements
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)

    # Only write back if there are changes
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Replaced shorthand variables in {file_path}")
    else:
        print(f"No changes needed for {file_path}")

# Define the directory to scan for SCSS files
def replace_in_directory(directory):
    # List of files to ignore
    ignored_files = [
        os.path.normpath('src/defaultSettings.scss'),
        os.path.normpath('src/variables.scss')
    ]

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".scss"):
                file_path = os.path.normpath(os.path.join(root, file))
                # Skip ignored files
                if file_path in ignored_files:
                    print(f"Skipping {file_path}")
                    continue
                replace_shorthands_in_file(file_path)

# Specify the 'src' directory for scanning
replace_in_directory('./src')
