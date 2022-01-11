# @Time: 2022/1/11 11:29 上午
# @Author: Bruce

import datetime


class Todo:
    def __init__(self, task, category,
                 date_added=None,
                 date_completed=None,
                 status=None,
                 position=None):
        self.task = task
        self.category = category
        self.date_added = date_added if date_added is not None else datetime.datetime.now().isoformat()
        self.date_completed = date_completed if date_completed is not None else None
        self.status = status if status is not None else 1
        self.position = position if position is not None else None

    def __repr__(self) -> str:
        return f"({self.task}, " \
               f"{self.category}, " \
               f"{self.date_added}, " \
               f"{self.date_completed}, " \
               f"{self.status}, " \
               f"{self.position})"
