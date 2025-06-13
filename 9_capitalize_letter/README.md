# 9. Harflarni Katta Qilish

## Vazifa:
`capitalize.py` faylida `def capitalize(text: str) -> str:` funksiyasi yozilsin.  
Matndagi harflarni katta harfga o'zgartirib qaytarsin.

## Test:
```python
from capitalize import capitalize

assert capitalize("hello") == "HELLO", "'hello' → 'HELLO' bo'lishi kerak"
assert capitalize("") == "", "Bo'sh matn o'zgarishsiz qaytishi kerak"
