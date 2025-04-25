import pytest
from io import StringIO
from contextlib import redirect_stdout

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes import Task, OrderBook

def test_task_creation():
    task = Task("Fix bug", "Alice", 5)
    assert task.description == "Fix bug"
    assert task.programmer == "Alice"
    assert task.workload == 5
    assert task.finished is False
    assert isinstance(task.id, int)

def test_task_mark_finished():
    task = Task("Test", "Bob", 3)
    assert task.is_finished() is False
    task.mark_finished()
    assert task.is_finished() is True

def test_task_str():
    task = Task("Do something", "Charlie", 4)
    assert "NOT FINISHED" in str(task)
    task.mark_finished()
    assert "FINISHED" in str(task)

def test_orderbook_add_and_retrieve_orders():
    ob = OrderBook()
    ob.add_order("Build API", "Dana", 10)
    orders = ob.all_orders()
    assert len(orders) == 1
    assert orders[0].description == "Build API"

def test_orderbook_programmers_list():
    ob = OrderBook()
    ob.add_order("Task A", "Alice", 3)
    ob.add_order("Task B", "Bob", 4)
    ob.add_order("Task C", "Alice", 5)
    programmers = ob.all_programmers()
    assert programmers == {"Alice", "Bob"}

def test_programmers_orders():
    ob = OrderBook()
    ob.add_order("Task A", "Alice", 3)
    ob.add_order("Task B", "Alice", 4)
    ob.add_order("Task C", "Bob", 5)
    result = ob.programmers_orders()
    assert result["Alice"] == ["Task A", "Task B"]
    assert result["Bob"] == ["Task C"]

def test_orderbook_finished_unfinished_orders():
    ob = OrderBook()
    ob.add_order("Task A", "Eve", 3)
    ob.add_order("Task B", "Eve", 4)
    task_ids = [task.id for task in ob.all_orders()]
    ob.mark_finished(task_ids[0])
    
    finished = ob.finished_orders()
    unfinished = ob.unfinished_orders()
    assert any(task.description == "Task A" for task in finished)
    assert any(task.description == "Task B" for task in unfinished)

def test_orderbook_status_of_programmer():
    ob = OrderBook()
    ob.add_order("Task A", "Alice", 2)
    ob.add_order("Task B", "Alice", 4)
    ob.add_order("Task C", "Alice", 3)
    ids = [task.id for task in ob.all_orders()]
    ob.mark_finished(ids[0])
    ob.mark_finished(ids[2])
    
    status = ob.status_of_programmer("Alice")
    assert status == (2, 1, 5, 4)  # finished:2, unfinished:1, done:2+3=5, scheduled:4

def test_mark_finished_invalid_id():
    ob = OrderBook()
    ob.add_order("Task X", "Zara", 2)
    initial_status = ob.all_orders()[0].is_finished()
    ob.mark_finished(999)  # nonexistent ID
    # Ensure task not accidentally marked
    assert ob.all_orders()[0].is_finished() == initial_status

def test_task_str_after_mark_finished():
    task = Task("Test Task", "Tester", 1)
    task.mark_finished()
    assert "FINISHED" in str(task)
