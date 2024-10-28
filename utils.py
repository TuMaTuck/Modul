def transform_numbers(numbers):
    return [x**3 if x > 0 else 0 for x in numbers]

def compare_numbers(numbers):
    positives = sorted([x for x in numbers if x > 0])
    return " < ".join(map(str, positives)) if positives else "No positive numbers"

def translate_text(text, lang):
    translations = {
        "uk": {
            "Мова:": "Мова:",
            "Українська": "Українська",
            "Англійська": "Англійська",
            "Три числа a, b, c:": "Три числа a, b, c:",
            "Дані збережено в файл": "Дані збережено в файл",
            "Додатні возвести в куб, а від’ємні замінити на 0, порівняти додатні числа:": 
                "Додатні возвести в куб, а від’ємні замінити на 0, порівняти додатні числа:"
        },
        "en": {
            "Мова:": "Language:",
            "Українська": "Ukrainian",
            "Англійська": "English",
            "Три числа a, b, c:": "Three numbers a, b, c:",
            "Дані збережено в файл": "Data saved in file",
            "Додатні возвести в куб, а від’ємні замінити на 0, порівняти додатні числа:": 
                "Positive numbers cubed, negative numbers set to 0, compare positive numbers:"
        }
    }
    return translations.get(lang, translations["uk"]).get(text, text)
