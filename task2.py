from pathlib import Path
from typing import List, Dict, Union


def get_cats_info(path: str) -> List[Dict[str, Union[str, int]]]:
    file_path = Path(path)
    if file_path.exists():
        with open(file_path, encoding='UTF-8') as fh:
            data = fh.readlines()
            if data:
                items = [line.split(',') for line in data]
                try:
                    handled_data = [{"id": item[0].strip(), "name": item[1].strip(
                    ), "age": item[2].strip()} for item in items]
                except IndexError:
                    print('Неправильна розмітка в файлі. має бути так\n'
                          '(text,value)')
                except ValueError:
                    print(f'в рядку (text,value), value має бути числом')
            else:
                print('Файл пустий')
    else:
        print('Такий шлях не існує')

    return handled_data


# приклад використання
def main():
    cats_info = get_cats_info("data_task1.txt")
    print(cats_info)


if __name__ == '__main__':
    main()
