time_data = '1h 45m,360s,25m,30m 120s,2h 60s'

# Разделим строку по запятой
parts = time_data.split(',')

# Переменная для хранения общего количества минут
total_minutes = 0

# Проходим по каждому элементу списка
for part in parts:
    # Разделим возможные единицы в одном фрагменте (например: '1h 45m')
    units = part.split()

    # Обрабатываем каждую единицу: '1h', '45m' и т.д.
    for unit in units:
        if 'h' in unit:
            total_minutes += int(unit.replace('h', '')) * 60
        elif 'm' in unit:
            total_minutes += int(unit.replace('m', ''))
        elif 's' in unit:
            total_minutes += int(unit.replace('s', '')) // 60

print(total_minutes)
