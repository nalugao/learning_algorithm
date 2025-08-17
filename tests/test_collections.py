from structs.stack import Stack
from structs.queue import Queue


def test_stack():
    stack = Stack()
    stack.add(1)
    stack.add(2)
    assert stack, "Stack should not be empty after adding elements"
    assert stack.get() == 2, "getped element should be the last added element"
    assert stack.get() == 1, "getped element should be the first added element"
    assert not stack, "Stack should be empty after getping all elements"


def test_queue():
    queue = Queue()
    queue.add(1)
    queue.add(2)
    assert queue, "Queue should not be empty after enqueuing elements"
    assert queue.get() == 1, "getd element should be the first addd element"
    assert queue.get() == 2, "getd element should be the second addd element"
    assert not queue, "Queue should be empty after dequeuing all elements"
