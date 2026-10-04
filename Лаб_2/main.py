"""Завдання 14. Відбір рядків за префіксом
Відберіть рядки, що починаються із заданого префікса (без урахування регістру).
Запишіть у файл *_report.txt заголовок із префіксом, рядок із 24 знаків =, далі номери
рядків у полі шириною 3 та перші 20 символів кожного рядка, і насамкінець підсумок про
кількість відібраних. Функція повертає цю кількість."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def prefix_filter(path, prefix: str) -> int:
    prefix_file = BASE_DIR / f"{prefix}_report.txt"
    with (open(path, "r", encoding="utf-8") as read_file,
          open(prefix_file, "w", encoding="utf-8") as write_file):
        
        count_line = 0
        write_file.write(f"Префікс: {prefix!r}\n")
        write_file.write("=" * 24 + "\n")
        
        for i, line in enumerate(read_file, start = 1):
            if line.lower().startswith(prefix.lower()):
                count_line += 1
                write_file.write(f"{i:>3}  {line.rstrip("\r\n")[:20]}\n")
                
        write_file.write(f"Відібрано: {count_line}\n")
        return count_line

def continue_my() -> bool:
    while True:
        match input("Якщо хочете продовжити напишіть Y. \nЯкщо не хочете напишіть N\nВаша відповідь = ").strip():
            case "Y":
                return True
            case "N":
                return False
            case _:
                print("Неправильна відповіль")
                               
def interface():
    while True:
        my_path = input("Введіть назву файла з якого будемо читати: ").strip()
        p = BASE_DIR / my_path
        
        if not p.is_file():
            print(f"Файл '{p}' не знайшли. Будь ласка повторно введіть назву файла")
            continue
        
        prefix = input("Введіть назву префікса: ")
        count_line = prefix_filter(p, prefix)
        print(f"Було відібрано {count_line} рядків\n")
        
        if not continue_my():
            break
        
interface()