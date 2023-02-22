"""
Задание 6.

Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
 и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
a = float(input('Результат пробежки в первый день:'))
b = float(input('Введите результат пробежки:'))
day = 1
while a < b:
    day += 1
    a *= 1.1
    print(f"{day}-й день:", a)
print(f"Ответ: на {day} -й "
      f"день спортсмен достиг результата — не менее {b} км.")
