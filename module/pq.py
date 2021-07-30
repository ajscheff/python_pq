#!/usr/bin/env python3

import time
from .colors import colors
from .errors import EmptyQueueException


class Item:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority

    def __repr__(self):
        val = colors.LIGHTGREY + "  {}".format(self.val) + colors.ENDC
        arrow = colors.YELLOW + " -----> " + colors.ENDC
        priority = colors.LIGHTGREY + "{}".format(self.priority) + colors.ENDC
        queue = val + arrow + priority
        return queue


class PriorityQueue:

    def __init__(self):
        self.storage = []

    def __str__(self):
        arrow = colors.YELLOW + "<--------------> \n" + colors.ENDC
        priority_results = colors.BOLD + \
            "Find the priority of each value in descending order:\n" \
            + colors.ENDC + \
            arrow + \
            colors.LIGHTGREY + "Value -> Priority\n" + colors.ENDC + \
            arrow + \
            "\n".join([str(item) for item in self.storage])
        return priority_results

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
        if len(self.storage) == 1:
            raise EmptyQueueException(
                "Priority queue only has one value. There is nothing to peek at!")
        return self.storage[-1].val

    def pop(self):
        if len(self.storage) == 0:
            raise EmptyQueueException(
                "Priority queue is empty. There is nothing to pop!")
        return self.storage.pop().val


# def simple_test():
#     print(colors.YELLOW + "Running simple test..." + colors.ENDC)
#     time.sleep(1)
#     pq = PriorityQueue()

#     pq.insert("c", 3)
#     pq.insert("a", 1)
#     pq.insert("b", 2)

#     print(pq)

#     assert(pq.pop() == "a")
#     assert(pq.pop() == "b")
#     assert(pq.pop() == "c")

#     print(colors.GREEN + "Simple test passed!" + colors.ENDC)


# def error_test():
#     print(colors.YELLOW + "Running test for error handling..." + colors.ENDC)
#     time.sleep(1)

#     pq = PriorityQueue()

#     pq.insert("c", 3)
#     pq.peek()

#     print('hey')


# if __name__ == "__main__":
#     simple_test()
#     print("Initializing error test...")
#     time.sleep(1)
#     error_test()
