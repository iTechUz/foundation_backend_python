Python print() funksiyasi bo‘yicha boshlang‘ich testlar
Quyidagi testlar Python dasturlash tilidagi print() funksiyasining asosiy xususiyatlarini sinash uchun mo‘ljallangan. Har bir savol print() funksiyasining separator (sep), qator oxiri (end), va escape belgilari (\n, \') kabi jihatlarini qamrab oladi. To‘g‘ri javob va tushuntirish har bir savol ostida keltirilgan.

1. Quyidagi dastur qanday natija chiqaradi?
print("Hello", "World", end="!")

Javoblar:

A) Hello World!
B) HelloWorld!
C) Hello World
D) SyntaxError

To‘g‘ri javob: A) Hello World!
Tushuntirish: end="!" parametri print() funksiyasining oxiriga yangi qator (\n) o‘rniga ! belgisini qo‘yadi. Hello va World o‘rtasida bo‘shliq avtomatik ravishda qo‘shiladi, chunki standart sep=" " parametri ishlatiladi.

2. Quyidagi dastur qanday natija chiqaradi?
print("Python", "is", "fun", sep="-")

Javoblar:

A) Python is fun
B) Python-is-fun
C) Pythonis-fun
D) Python-is fun

To‘g‘ri javob: B) Python-is-fun
Tushuntirish: sep="-" parametri argumentlar orasiga bo‘shliq o‘rniga - belgisini qo‘yadi. Shuning uchun natija Python-is-fun bo‘ladi.
