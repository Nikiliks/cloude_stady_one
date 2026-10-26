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

if __name__ == "__main__":
    expenses = load_expenses()
    print(f"Было записей: {len(expenses)}")

