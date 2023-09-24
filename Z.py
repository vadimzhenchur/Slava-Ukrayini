import json

with open("task2.json", 'r', encoding="utf-8") as f:
    data = json.load(f)

a = input("шо треба?(name)")
b = input("шо треба?(surname)")

for name in data:
    print(name['оцінки'])