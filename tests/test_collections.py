from structs import Stack
from structs import Queue


def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack, "Stack should not be empty after pushing elements"
    assert stack.pop() == 2, "Popped element should be the last pushed element"
    assert stack.pop() == 1, "Popped element should be the first pushed element"
    assert not stack, "Stack should be empty after popping all elements"


def test_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue, "Queue should not be empty after enqueuing elements"
    assert queue.dequeue() == 1, "Dequeued element should be the first enqueued element"
    assert queue.dequeue() == 2, "Dequeued element should be the second enqueued element"
    assert not queue, "Queue should be empty after dequeuing all elements"
