"""Завдання 14. Об'єднання складів
Залишки товарів на складах задано словниками «товар → кількість». Функція
отримує довільну кількість таких словників, а також окремі товари іменованими
аргументами, і повертає новий словник, де кількості однакових товарів додано.
Вхідні словники не змінюються"""

def merge_stock(*stores: dict, **extra: int) -> dict:
    storex_plus_extra = [*stores, extra]
    all_dict = {}
    for one_dict in storex_plus_extra:
        if not isinstance(one_dict, dict):
            raise TypeError("Замість dict додали не правильний тип")
        for name, cnt in one_dict.items():
            if not isinstance(cnt, int):
                raise TypeError("Замість числа в кількості передали не правильний тип")
            all_dict[name] = all_dict.get(name, 0) + cnt
    return all_dict
    
if __name__ == "__main__":
    try:
        res1 = merge_stock({"хліб": 10, "молоко": 5}, {"молоко": 3, "сир": 7}, сир=1)
        print(res1)

        res2 = merge_stock(хліб=2)
        print(res2)
    except TypeError as err:
        print(err)