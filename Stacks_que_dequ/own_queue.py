'''
Queue() - creates new queue that is empty
enqueue(item) - adds new item to the rear of the queue
dequeue() - removes front item in queue
isEmpty() -tests if empty
size() - returns no of items
'''


class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
print(q.isEmpty())
