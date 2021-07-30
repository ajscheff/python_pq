#!/usr/bin/env python3

import time
from module.pq import simple_test, error_test

if __name__ == "__main__":
    simple_test()
    print("Initializing error test...")
    time.sleep(1)
    error_test()
