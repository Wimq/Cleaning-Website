import json

with open("js/courses.js", "r", encoding="utf-8") as f:
    content = f.read()

# remove 'const courseDatabase = ' and ';'
json_str = content.replace("const courseDatabase = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

try:
    data = json.loads(json_str)
    print(f"Loaded {len(data)} courses successfully.")
except Exception as e:
    print(f"Error parsing JSON: {e}")
