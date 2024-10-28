import os
import json
from utils import transform_numbers, compare_numbers, translate_text

# Ім'я файлу для збереження даних
FILENAME = "MyData.txt"

def load_data():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, 'r') as file:
                data = json.load(file)
                numbers = data.get("numbers")
                lang = data.get("lang", "uk")
                if isinstance(numbers, list) and len(numbers) == 3 and lang in ["uk", "en"]:
                    return numbers, lang
        except (json.JSONDecodeError, KeyError):
            pass
    return None, None

def save_data(numbers, lang):
    data = {"numbers": numbers, "lang": lang}
    with open(FILENAME, 'w') as file:
        json.dump(data, file)
    print(translate_text("Дані збережено в файл", lang), FILENAME)

def main():
    numbers, lang = load_data()
    
    if numbers is None:
        print("Введіть три числа a, b, c:")
        numbers = list(map(int, input().split()))
        
        print("Введіть мову інтерфейсу (uk або en):")
        lang = input().strip()
        
        save_data(numbers, lang)
        return

    # Виконати обробку чисел
    print(translate_text("Мова:", lang), translate_text("Українська" if lang == "uk" else "Англійська", lang))
    print(translate_text("Три числа a, b, c:", lang), numbers)
    
    transformed_numbers = transform_numbers(numbers)
    inequality = compare_numbers(transformed_numbers)
    
    print(translate_text("Додатні возвести в куб, а від’ємні замінити на 0, порівняти додатні числа:", lang))
    print(" ".join(map(str, transformed_numbers)))
    print(inequality)

if __name__ == "__main__":
    main()
