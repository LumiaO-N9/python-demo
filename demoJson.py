import json as j

with open("students.json", encoding="utf-8") as f:
    for i in range(8):
        json1 = j.loads(f.readline())
        print(json1["id"])
        print(json1["name"])
        print(json1["age"])
