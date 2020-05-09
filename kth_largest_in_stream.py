import heapq


class KthLargest:
    def __init__(self, l, k):
        self.k = k
        self.l = l
        heapq.heapify(self.l)
        while len(self.l) > k:
            heapq.heappop(self.l)
        # print(self.l)

    def add(self, n):
        if len(self.l) < self.k:
            heapq.heappush(self.l, n)
        elif n > self.l[0]:
            heapq.heapreplace(self.l, n)
        # print(self.l)
        return self.l[0]


if __name__ == '__main__':
    ins = KthLargest([4, 5, 8, 2], 3)

    print(ins.add(3) == 4)
    print(ins.add(5) == 5)
    print(ins.add(10) == 5)
    print(ins.add(9) == 8)
    print(ins.add(4) == 8)

    ins = KthLargest([], 1)
    print(ins.add(-3) == -3)

    ins = KthLargest([5, -1], 3)
    print(ins.add(2) == -1)
    print(ins.add(1) == 1)
    print(ins.add(-1) == 1)
    print(ins.add(3) == 2)
