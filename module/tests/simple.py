import time
from ..colors import colors
from ..pq import PriorityQueue


def simple_test():
    print(colors.YELLOW + "Running simple test..." + colors.ENDC)
    time.sleep(1)
    pq = PriorityQueue()

    pq.insert("c", 3)
    pq.insert("a", 1)
    pq.insert("b", 2)

    print(pq)

    assert(pq.pop() == "a")
    assert(pq.pop() == "b")
    assert(pq.pop() == "c")

    print(colors.GREEN + "Simple test passed!" + colors.ENDC)
