phones = [
    {"make": "Google", "model": 216, "color": "Black"},
    {"make": "Mi Max", "model": "2", "color": "Gold"},
    {"make": "Samsung", "model": 7, "color": "Blue"},
]

sorted_phones = sorted(
    phones,
    key=lambda phone: int(phone["model"]),
    reverse=True,
)

print("Original list:")

for phone in phones:
    print(phone)

print("\nSorted list:")

for phone in sorted_phones:
    print(phone)
    