# 14. Сума чисел до N iз перериванням: Обчислiть суму чисел вiд
# 1 до N, але зупинiть сумування, якщо зустрiли число, що дiлиться
# на 13 i 7

def get_number() -> int:
    while True:
        number = input("Введіть ціле число n = ").strip()
        try:
            number_new = int(number)
            if number_new < 1:
                print("Число має бути більшим або рівним 1")
                continue
            return number_new
        except ValueError:
            print("Виявленна помилка в числі, будь ласка перепишіть")

def get_sum(n: int, start: int = 1) -> tuple[int, int, bool]:
    summ = 0
    while start <= n:
        if start % 7 == 0 and start % 13 == 0:
            return summ, start, True
        summ += start
        start += 1
    return summ, start, False
    
def continue_my() -> bool:
    while True:
        ask = input("Якщо хочете продовжити напишіть Y. \nЯкщо не хочете напишіть N\nВаша відповідь = ").strip()
        match ask:
            case "Y":
                return True
            case "N":
                return False
            case _:
                print("Неправильна відповіль")
                
def display() -> None:
    while True:
        n = get_number()
        summ, start, cont = get_sum(n)
        if cont:
            print(f"Було зустріто число яке ділиться і на 7 і нa 13. Це число {start}")
            print (f"Сума чисел від 1 до {start - 1} = {summ}")
        else:
            print("Ми не зустріли число яке ділиться і на 7 і нв 13.")
            print (f"Сума чисел від 1 до {start - 1} = {summ}")
        if not continue_my():
            break
display()