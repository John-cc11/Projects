import sys
from pathlib import Path

from Utils.database_func import load_schedule,delete_schedule,save_schedule

save_schedule(
    None,  # create
    "Test Title",
    "Test Content",
    "2026-05-24",
    "3:00 PM",
    "High",
    "School",
    0
)