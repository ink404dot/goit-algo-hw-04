from sys import argv
from pathlib import Path
from colorama import Fore, Style, init


init(autoreset=True)


def show_dir_structure(path: Path, level: int = 0):
    if not path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{path}' не існує.")
        return

    if not path.is_dir():
        print(f"{Fore.RED}Помилка: '{path}' не є директорією.")
        return
    
    if level == 0:
        print(f"{Fore.YELLOW}📦 {path.name}")
        level +=1

    dir_list = []

    for item in path.iterdir():
        indent = ' ' * level * 4
        if item.is_dir():
            dir_list.append(item)
        else:
            print(f"{indent}{Fore.GREEN}📜 {item.name}")

    for item in dir_list:
        print(f"{indent}{Fore.BLUE}📂 {item.name}")
        show_dir_structure(item, level + 1)

# приклад використання
def main():
    if len(argv) < 2:
        print(f"{Fore.RED}Будь ласка, передайте шлях до директорії як аргумент.")
        return

    dir_path = Path(argv[1])
    show_dir_structure(dir_path)


if __name__ == '__main__':
    main()
