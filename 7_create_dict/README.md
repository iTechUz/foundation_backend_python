# 7. Lug'at Yaratish

## Vazifa:
`create_dict.py` faylida `def create_user(name: str, age: int) -> dict:` funksiyasi yozilsin.  
Foydalanuvchi ma'lumotlarini lug'at ko'rinishida qaytarsin.

## Test:
```python
from create_dict import create_user

user = create_user("Ali", 20)
assert user == {"name": "Ali",
