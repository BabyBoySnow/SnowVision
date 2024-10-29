import re

# File paths (change these paths if necessary)
selector_file_path = r"C:\Users\earlw\OneDrive\Documents\GitHub\SnowVision\lib\selectors\selectorPlaceholders.scss"
winter_wonderland_file_path = r"C:\Users\earlw\OneDrive\Documents\GitHub\SnowVision\src\winter-wonderland.scss"

# Step 1: Extract the mappings from selectorPlaceholders-updated.scss
mappings = {}
with open(selector_file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    placeholder_pattern = re.compile(r"\.(\w+_\w+)\s*\{\s*@extend\s*(%[\w-]+)")
    for match in placeholder_pattern.finditer(content):
        class_name, variable = match.groups()
        mappings[class_name] = variable

# Step 2: Read winter-wonderland.scss and replace classes
with open(winter_wonderland_file_path, 'r', encoding='utf-8') as file:
    ww_content = file.read()

# Define a function to replace classes
def replace_classes(content, mappings):
    class_pattern = re.compile(r"\.(\w+_\w+)(?![\w-])")
    def class_replacement(match):
        class_name = match.group(1)
        return mappings.get(class_name, f".{class_name}")
    return class_pattern.sub(class_replacement, content)

# Replace the classes using the mappings
updated_content = replace_classes(ww_content, mappings)

# Step 3: Save the updated content back to winter-wonderland.scss
with open(winter_wonderland_file_path, 'w', encoding='utf-8') as file:
    file.write(updated_content)

print("Update complete!")
