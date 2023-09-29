from lib.task_formatter import TaskFormatter
from unittest.mock import Mock

def test_format_task_string_when_incomplete():
    task = Mock()

    task.title = "Laundry"
    task.complete = False
    task.format.return_value = "- [ ] Laundry"

    formatter = TaskFormatter(task)
    assert formatter.format() == "- [ ] Laundry"

def test_format_task_String_when_complete():
    task = Mock()

    task.title = "Gym"
    task.complete = True
    task.format.return_value = "- [x] Gym"

    formatter = TaskFormatter(task)
    assert formatter.format() == "- [x] Gym"

