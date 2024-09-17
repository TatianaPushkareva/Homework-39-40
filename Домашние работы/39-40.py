#Напишите функцию для перевода рублей в доллары.
# Функция принимает в себя два аргумента:
# количество рублей, курс доллара к рублю.
# Возвращает: количество долларов

def exchange(rubles, rate):
    dollars = rubles/rate
    return dollars

print(exchange(100, 110))

# Напишите функцию для проверки пользователя на
# совершеннолетие. Функция принимает в себя
# возраст. Возвращает True либо False.

def isadult(age):
    if age >= 18:
        return True
    else:
        return False

print(isadult(int(input('Введите возраст'))))


