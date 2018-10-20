class Safe(object):
    def __init__(self, capacity):
        self._capacity = capacity
        self._items = []

    @property
    def capacity(self):
        return self._capacity

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        try:
            if (len(self._items) > self._capacity):
                raise ValueError
            self._items.append(item)

        except ValueError:
            print('Safe is full')

    def __repr__(self):
        return "Safe: " + str(len(self._items)) + "/" + str(self._capacity)


# To see the output, uncomment the lines belows:
safe = Safe(2)
safe.add_item("item")
safe.add_item("item2")
safe.add_item("item3")
print(safe)