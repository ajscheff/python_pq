# Priority Queue

This is a very simple implementation of a priority queue. It doesn't handle edge cases well and it certainly isn't the most efficient. It's a start.

Read through the file `pq.py` and make sure you understand everything that's going on. The `simple_test()` method very simply demonstrates the purpose of a priority queue. In this queue, lower numbers for priority come first. Run the test with `python pq.py` and notice how no matter the order that we insert items into the queue, they always come out in the order "A", "B", "C".

Below is a list of ways that we can improve the structure. Feel free to do any or all of them.

## Code Quality Improvements

### Override the `<` operator for Item

Our priority queue uses instances of the `Item` class to store values alongside priorities. Right now, we use a separate comparison function `standard_priority_func` to compare `Item` priorities during insertion.

A cool feature of classes in most languages is operator overriding. This allows us to compare instances of a class directly using operators like `<`, `==`, and others. Python makes it really easy to do this. Implement a method `def __lt__(self, other):` in the class `Item`. Then, modify the `insert` method to compare items in `self.storage` to `to_insert` directly using `<`.

### Handle user errors gracefully

Right now, if you try to `pop` or `peek` from an empty queue, an error that's specific to the internal implementation of the queue will bubble up. It would be more helpful to a future consumer of this queue if we handled that error and raised a specific exception that clearly indicates the problem. Here are the [python docs on raising custom exceptions](https://docs.python.org/3/tutorial/errors.html#raising-exceptions).

Add an `EmptyQueueException` and raise it appropriately in `peek` and `pop`. Think of errors that can occur during `insert` and use the same technique of raising a custom exception to handle those gracefully as well. You can make more varieties of specific exceptions.

### Write a better string representation of the queue

The `__str__` method of `PriorityQueue` is not great because it's not very human readable and it would print a very long string if the queue had a lot of items in it. Update it to print a string that is easier to read and provides better insight into the state of the structure. Consider what information a consumer of this queue might want to see when they print it out.

## Testing / Correctness Improvements

### Handle priority equality correctly

This example doesn't consider the case when multiple items in the queue have equal priority. In this case, we'd like those items to go through the queue in a FIFO order. Add this behavior to the queue.

### Write a robust series of tests

There's one simple test included as an example, but it definitely doesn't thoroughly test the data structure. Change that by adding tests for the following cases:

- Ensure the queue works with many of items inserted in different orders
- Ensure items with same priority go through the queue First In First Out
- Ensure the error cases from the previous section are all handled correctly
- Ensure the queue works with negative or floating point priorities

## Efficiency Improvements

For each of the below tasks, copy the priority queue into a new file first before modifying. We'll want to keep all of these implementations side-by-side for testing speed later.

### Prioritize speed in `insert` rather than `peek`/`pop`

For list-backed priority queues, we have two basic approaches. The one you see here is to maintain a sorted list and always pop from the end. A different approach is to not worry about maintaining a sorted list and search through the list for the item with the smallest priority value during `peek` and `pop`. This implementation makes `insert` much faster and `peek` and `pop` much slower, which may be a desireable trade off for some circumstances.

### Improve speed with a linked list for storage

We use a standard python list as the backing data structure for this priority queue, but that's definitely not the most time-efficient choice. A big reason for this is the shifting and resizing required to maintain an array in memory. Update this priority queue so that it uses a linked list for storage rather than a standard python list.

### Improve speed even further with a heap for storage (hard!)

The most efficient implememntation of a priority queue is with a heap. This is a tricky structure to build, but there are a lot of examples out there. Check out this [video for a great explanation](https://www.youtube.com/watch?v=t0Cq6tVNRBA)

Fun fact: Once you've done this, you've actually implemented one of the most efficient sorting algorithms out there. It's called heapsort. You can now sort numbers with world-class efficiency by inserting them all into your heap-backed priority queue and pulling them out one by one.

### Benchmark different implementations to test performance

Once you've done the work to build a linked list or heap-backed priority queue, it's fun to actually demonstrate that it's faster than the list-backed one you started with. Make a test case that puts a lot of items into the queue and use `time.time()` before and after running it to measure the speed of the test. Try different priority queue implementations, different input sizes, and different usage patters (e.g. 1000 inserts then 1000 removes vs. 10 inserts then 10 removes repeated 100 times )

## Real world use cases

Priority queues are incredibly practical structures that are used all over the place in software. Do some googling to teach yourself about a real world use case of a priority queue that's relevant to your domain. For example, priority queues can be used to implement Dijkstra's algorithm or for bandwidth management.
