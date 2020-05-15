class Item:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority

    def __repr__(self):
        return "Item(val: {}, pri: {})".format(self.val,
                                               self.priority)


class PriorityQueue:

    def __init__(self):
        self.storage = []

    def __str__(self):
        return "[" + ", ".join([str(item) for item in self.storage]) + "]"

    def standard_priority_func(self, p1, p2):
        return p1 < p2

    def insert(self, val, priority):
        to_insert = Item(val, priority)

        insert_index = 0
        while insert_index < len(self.storage):
            if self.standard_priority_func(self.storage[insert_index].priority, priority):
                break
            insert_index += 1

        self.storage.insert(insert_index, to_insert)

    def peek(self):
        return self.storage[-1].val

    def pop(self):
        return self.storage.pop().val


def simple_test():
    pq = PriorityQueue()

    pq.insert("c", 3)
    pq.insert("a", 1)
    pq.insert("b", 2)

    assert(pq.pop() == "a")
    assert(pq.pop() == "b")
    assert(pq.pop() == "c")


if __name__ == "__main__":
    simple_test()
