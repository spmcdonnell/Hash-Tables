class DynamicArray:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.count = 0

    def insert(self, index, value):
        if self.count == self.capacity:
            print('Array is full')
            return

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]

        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)

    def resize(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for i in range(self.count):
            new_storage[i] = self.storage[i]

        self.storage = new_storage

    def replace(self, index, value):
        self.storage[index] = value

    def add_to_front(self, value):
        self.insert(0, value)

    def slice(self, start_index, end_index):
        return
