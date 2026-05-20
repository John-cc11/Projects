import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from Utils.json_shortcut import load_json, add_data,update_data, remove_data

data = load_json("sched.json")

# ---------------- ADD ----------------
add_data("sched.json", {
    "id": 1,
    "title": "Study Python"
})

print("After Add:")
print(load_json("sched.json"))


# ---------------- UPDATE ----------------
update_data(
    "sched.json",
    "id",
    1,
    {
        "title": "Learn CustomTkinter"
    }
)

print("After Update:")
print(load_json("sched.json"))


# ---------------- REMOVE ----------------
remove_data("sched.json", "id", 1)

print("After Remove:")
print(load_json("sched.json"))

print("Saved!")