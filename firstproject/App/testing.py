import sys
from pathlib import Path


print(Path(__file__).parent.parent)

sys.path.append(str(Path(__file__).resolve().parent.parent))
from Utils.database_func import load_schedule,delete_schedule,save_schedule



delete_schedule(1)
