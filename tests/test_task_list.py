from lib.task_list import TaskList
from unittest.mock import Mock

def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour

def test_task_added_to_list():
    task_list = TaskList()

    fake_task_one = Mock()
    fake_task_one.all.return_value = fake_task_one
    fake_task_two = Mock()
    fake_task_two.all.return_value = fake_task_two
    fake_task_three = Mock()
    fake_task_three.all.return_value = fake_task_three

    task_list.add(fake_task_one)
    task_list.add(fake_task_two)
    task_list.add(fake_task_three)

    assert task_list.all() == [fake_task_one, fake_task_two, fake_task_three]

def test_task_added_to_list_one_complete_and_one_not_complete():
    task_list = TaskList()

    fake_task_one = Mock()
    fake_task_one.is_complete.return_value = True
    fake_task_two = Mock()
    fake_task_two.is_complete.return_value = False

    task_list.add(fake_task_one)
    task_list.add(fake_task_two)

    assert task_list.all_complete() == False

def test_task_added_to_list_two_complete():
    task_list = TaskList()

    fake_task_one = Mock()
    fake_task_one.is_complete.return_value = True
    fake_task_two = Mock()
    fake_task_two.is_complete.return_value = True

    task_list.add(fake_task_one)
    task_list.add(fake_task_two)

    assert task_list.all_complete() == True