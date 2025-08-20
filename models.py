### setup class names for future use

from __future__ import annotations
from typing import Dict, List, TypedDict

DATA_FILE = "data.json"
DEFAULT_CATEGORY_ID = 1  # set default category for general tasks

class Category(TypedDict):
    id: int
    name: str

class Task(TypedDict):
    id: int
    title: str
    done: bool
    category_id: int
    created_at: str  # ISO timestamp