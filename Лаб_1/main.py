# 14. Сума чисел до N iз перериванням: Обчислiть суму чисел вiд
# 1 до N, але зупинiть сумування, якщо зустрiли число, що дiлиться
# на 13 i 7

def get_number() -> int:
    while True:
        try:
            number = int(input("Введіть ціле число n = ").strip())
            if number >= 1:
                return number
            print("Число має бути більшим або рівним 1")
        except ValueError:
            print("Виявленна помилка в числі, будь ласка перепишіть")

def get_sum(n: int) -> tuple[int, int, bool]:
    summ = 0
    for i in range(1, n + 1):
        if i % 7 == 0 and i % 13 == 0:
            return summ, i, True
        summ += i
    return summ, i, False
    
def continue_my() -> bool:
    while True:
        match input("Якщо хочете продовжити напишіть Y. \nЯкщо не хочете напишіть N\nВаша відповідь = ").strip():
            case "Y":
                return True
            case "N":
                return False
            case _:
                print("Неправильна відповіль")
                
def display() -> None:
    while True:
        n = get_number()
        summ, finish, cont = get_sum(n)
        if cont:
            print(f"Було зустріто число яке ділиться і на 7 і нa 13. Це число {finish}")
            print (f"Сума чисел від 1 до {finish - 1} = {summ}")
        else:
            print("Ми не зустріли число яке ділиться і на 7 і нв 13.")
            print (f"Сума чисел від 1 до {n} = {summ}")
        if not continue_my():
            break
display()