from pathlib import Path
from typing import Tuple


def total_salary(path: str) -> Tuple[int, float]:
    file_path = Path(path)
    if file_path.exists():
        with open(file_path, encoding='UTF-8') as fh:
            data = fh.readlines()
            if data:
                user_and_salary = [line.split(',') for line in data]
                try:
                    user_salaries = [int(item[1].strip())
                                     for item in user_and_salary]
                except IndexError:
                    print('Неправильна розмітка в файлі. має бути так\n'
                          '(text,value)')
                    return
                except ValueError:
                    print(f'в рядку (text,value), value має бути числом')
                    return
            else:
                print('Файл пустий')
                return
    else:
        print('Такий шлях не існує')
        return

    total_salary = sum(user_salaries)
    avarage_salary = total_salary / len(user_salaries)
    return (total_salary, avarage_salary)


# приклад використання
def main():
    data = total_salary("data_task1.txt")
    if data:
        total, average = data
        print(f"Загальна сума заробітної плати: {
            total}, Середня заробітна плата: {average:.2f}")


if __name__ == '__main__':
    main()
