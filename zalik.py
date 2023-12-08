def read_and_filter(file_path, threshold):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                # Розділення рядка на час та значення
                time, value = line.split(' ')

                # Перевірка, чи значення перевищує поріг
                if float(value) > threshold:
                    print(f'Час: {time}, Значення: {value}')
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


# Отримання введення користувача
user_input = input("Введіть значення AAA: ")

try:
    # Перетворення введеного значення користувача в число
    aaa_threshold = float(user_input)

    # Виклик функції зчитування та фільтрації
    read_and_filter('text1.txt', aaa_threshold)
except ValueError:
    print("Будь ласка, введіть числове значення.")