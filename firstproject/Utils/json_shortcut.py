import json
from pathlib import Path

BASE_PATH = Path(__file__).parent.parent
DATA_PATH = BASE_PATH / "Data"


def load_json(filename):
    path = DATA_PATH / filename

    if not path.exists():
        return []

    with open(path, "r") as f:
        return json.load(f)


def save_json(filename, data):
    path = DATA_PATH / filename

    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def add_data(filename, new_data):
    data = load_json(filename)

    data.append(new_data)

    save_json(filename, data)


def remove_data(filename, key, value):
    data = load_json(filename)

    data = [item for item in data if item.get(key) != value]

    save_json(filename, data)


def update_data(filename, key, value, updated_data):
    data = load_json(filename)

    for item in data:
        if item.get(key) == value:
            item.update(updated_data)

    save_json(filename, data)