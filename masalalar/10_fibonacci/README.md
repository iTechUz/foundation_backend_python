# 🌀 Fibonacci – Birinchi **n** ta Fibonachchi sonlarini hisoblovchi funksiya

Ushbu modulda `fibonacci(n: int) -> list` nomli funksiya mavjud bo‘lib, u birinchi **n ta Fibonachchi sonlarini** ro‘yxat ko‘rinishida qaytaradi.

---

## 📄 Funksiya ta’rifi

```python
def fibonacci(n: int) -> list:
    """
    Birinchi n ta Fibonachchi sonlarini hisoblab, ro'yxat ko'rinishida qaytaradi.

    :param n: Nechta Fibonachchi soni kerakligi
    :return: Fibonachchi sonlari ro'yxati
    """
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
