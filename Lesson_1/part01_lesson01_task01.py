"""
ЗАДАНИЕ 1

Человеко-ориентированное представление интервала времени
Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:

1) до минуты: <s> сек;
2) до часа: <m> мин <s> сек;
3) до суток: <h> час <m> мин <s> сек;
4) сутки или больше: <d> дн <h> час <m> мин <s> сек

Например, если пользователь введет 4567 секунд, вывести:
1 час 16 мин 7 сек
"""


day_sec = 24 * 60 * 60
hour_sec = 60 * 60
min_sec = 60


user_sec = int(input('Введите размер интервала (в секундах): '))

day = user_sec // day_sec
hour = (user_sec - day * day_sec) // hour_sec
minute = (user_sec - day * day_sec - hour * hour_sec) // min_sec
sec = user_sec - day * day_sec - hour * hour_sec - minute * min_sec

if user_sec >= day_sec:
    print(f"{day} дн {hour} час {minute} мин {sec} сек")
elif user_sec >= hour_sec:
    print(f"{hour} час {minute} мин {sec} сек")
elif user_sec >= min_sec:
    print(f"{minute} мин {sec} сек")
else:
    print(f"{sec} сек")
