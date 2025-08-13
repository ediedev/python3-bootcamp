import codecs

input_file = "quotes.txt"
output_file = "quotes.txt"

cleaned_lines = []

# Read in binary and decode correctly
with open(input_file, "rb") as f:
    content = f.read()

# Try decoding as UTF-8 first; if that fails, fallback
try:
    text = content.decode("utf-8")
except UnicodeDecodeError:
    text = content.decode("windows-1252")

# Replace curly quotes and fix en dash
lines = [line.strip() for line in text.splitlines() if line.strip()]

for line in lines:
    # Normalize quotes and dashes
    line = (line.replace("“", '"')
                 .replace("”", '"')
                 .replace("–", " - ")  # en dash to regular dash
                 .replace("—", " - "))  # em dash to regular dash

    if line.startswith('"'):  # quote
        cleaned_lines.append(line)
    elif line.startswith('-') and cleaned_lines:  # author
        cleaned_lines[-1] += " " + line

with open(output_file, "w", encoding="utf-8") as f:
    for line in cleaned_lines:
        f.write(line + "\n")
