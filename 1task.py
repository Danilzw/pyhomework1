#Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input("Number:"))
result = int((number // 100) + (number // 10 % 10) + (number % 10))
print(result)

