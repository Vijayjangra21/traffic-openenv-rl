from pydantic import BaseModel
from typing import List


class State(BaseModel):
    queue_lengths: List[int]
    waiting_times: List[int]


class Action(BaseModel):
    lane: int