import os
import glob
import json

# Path to markdown files directory
docs_dir = "/data/docs/"

# Find all .md files in the directory
md_files = glob.glob(os.path.join(docs_dir, "*.md"))

# Dictionary to store filename-title mapping
index = {}

# Process each markdown file
for md_file in md_files:
    try:
        with open(md_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):  # First H1 title
                    index[os.path.basename(md_file)] = line[2:].strip()
                    break  # Stop reading after the first title
    except Exception as e:
        print(f"Error reading {md_file}: {e}")

# Save the index to a JSON file
output_file = "/data/docs/index.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(index, f, indent=4)

print(f"Index file saved to {output_file}")
