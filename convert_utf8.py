# Convert db.json to UTF-8
input_file = 'db.json'
output_file = 'db_utf8.json'

with open(input_file, 'rb') as f:
    raw_bytes = f.read()

# Decode using Windows-1252 (common source of 0x92)
text = raw_bytes.decode('cp1252')

# Save as UTF-8
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(text)

print("Converted db.json to UTF-8 successfully.")