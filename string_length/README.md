# 🔠 String Length – Matn uzunligini hisoblovchi funksiya

Ushbu modulda `get_length(text: str) -> int` nomli funksiya mavjud. Funksiya foydalanuvchi kiritgan matnning **belgilar sonini** (uzunligini) aniqlab qaytaradi.

---

## 📄 Funksiya ta’rifi

```python
def get_length(text: str) -> int:
    """
    Berilgan matn uzunligini (ya'ni belgilar sonini) qaytaradi.

    :param text: Hisoblanadigan matn
    :return: Matn uzunligi (butun son)
    """
    return len(text)
