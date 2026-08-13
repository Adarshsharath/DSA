class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        self.mp.move_to_end(key)
        return self.mp[key]

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.mp.move_to_end(key)
        self.mp[key] = value
        if len(self.mp) > self.cap:
            self.mp.popitem(last=False)