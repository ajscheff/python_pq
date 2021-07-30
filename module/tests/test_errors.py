import time
from ..colors import colors
from ..pq import PriorityQueue


def error_test():
    print(colors.YELLOW + "Running test for error handling..." + colors.ENDC)
    time.sleep(1)

    pq = PriorityQueue()

    pq.insert("c", 3)
    pq.peek()

    print('hey')
