# 🔢 Even or Odd – Son juftmi yoki toqmi aniqlovchi funksiya

Ushbu modulda `is_even(number: int) -> bool` nomli funksiya mavjud bo‘lib, u berilgan butun son **juft bo‘lsa `True`**, **toq bo‘lsa `False`** qiymatni qaytaradi.

---

## 📄 Funksiya ta’rifi

```python
def is_even(number: int) -> bool:
    """
    Son juft bo‘lsa True, toq bo‘lsa False qaytaradi.

    :param number: Tekshiriladigan butun son
    :return: bool – True agar juft bo‘lsa, False agar toq bo‘lsa
    """
    return number % 2 == 0
