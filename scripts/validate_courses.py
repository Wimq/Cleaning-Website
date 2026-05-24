import json

with open("js/courses.js", "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("const courseDatabase = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

try:
    data = json.loads(json_str)
    for i, c in enumerate(data):
        for field in ["title", "category", "url", "desc"]:
            if field not in c:
                print(f"Course index {i} is missing field: {field}")
            elif not isinstance(c[field], str):
                print(f"Course index {i} field '{field}' is not string")
    print(f"Validated {len(data)} courses successfully.")
except Exception as e:
    print(f"Error: {e}")
