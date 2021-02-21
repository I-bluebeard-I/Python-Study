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

# Объявление переменных
split_time = {'day': 0, 'hour': 0, 'min': 0, 'sec': 0}
day_sec = 24 * 60 * 60
hour_sec = 60 * 60
min_sec = 60

# Запрос интервала у пользователя
user_sec = int(input('Введите размер интервала (в секундах): '))

# Вычисление данных
split_time['day'] = user_sec // day_sec
split_time['hour'] = (user_sec - split_time['day'] * day_sec) // hour_sec
split_time['min'] = (user_sec - split_time['day'] * day_sec - split_time['hour'] * hour_sec) // min_sec
split_time['sec'] = user_sec - split_time['day'] * day_sec - split_time['hour'] * hour_sec - split_time['min'] * min_sec

# Вывод результата
if user_sec >= day_sec:
    print(f"{split_time['day']} дн {split_time['hour']} час {split_time['min']} мин {split_time['sec']} сек")
elif user_sec >= hour_sec:
    print(f"{split_time['hour']} час {split_time['min']} мин {split_time['sec']} сек")
elif user_sec >= min_sec:
    print(f"{split_time['min']} мин {split_time['sec']} сек")
else:
    print(f"{split_time['sec']} сек")
