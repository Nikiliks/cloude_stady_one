import argparse
import json
import sys
from pathlib import Path

DATA_FILE = Path("expenses.json")


def load_expenses() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Ошибка: файл {DATA_FILE} повреждён")
        sys.exit(1)


def save_expenses(expenses: list[dict]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, ensure_ascii=False, indent=4)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Учёт расходов")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # команда add: три аргумента
    add_parser = subparsers.add_parser("add", help="Добавить расход")
    add_parser.add_argument("amount", type=float, help="Сумма расхода")
    add_parser.add_argument("category", help="Категория расхода")
    add_parser.add_argument("description", help="Описание расхода")

    # команда list: без аргументов
    subparsers.add_parser("list", help="Показать все расходы")

    # команда total: один необязательный аргумент
    total_parser = subparsers.add_parser("total", help="Посчитать сумму расходов")
    total_parser.add_argument("--category", help="Посчитать только по этой категории")

    return parser.parse_args()


def main() -> None:
    args = parse_args()   # разобрать то, что ввёл пользователь
    print(args)           # пока просто показать результат


if __name__ == "__main__":
    main()                # запустить программу




