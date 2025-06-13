# ➕ Sum List – Ro'yxatdagi sonlar yig'indisini hisoblash

Bu modulda `sum_numbers(numbers: list) -> int` nomli funksiya mavjud. U berilgan sonlar ro'yxatining yig'indisini hisoblab qaytaradi. Agar ro'yxat bo‘sh bo‘lsa, `0` natija qaytadi.

---

## 📄 Funksiya ta’rifi

```python
def sum_numbers(numbers: list) -> int:
    """
    Ro'yxatdagi sonlar yig'indisini qaytaradi.

    :param numbers: Butun sonlardan iborat ro'yxat
    :return: Yig'indisi (int)
    """
    return sum(numbers)
