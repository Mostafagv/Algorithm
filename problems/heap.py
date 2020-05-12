class MaxHeap:
    def __init__(self, l=[]):
        self.l = []
        self.sorted = []
        for i in l:
            self.add(i)


    def swap(self, parent, child):
        check = self.l[parent] >= self.l[child]
        while not check and parent>=0:
            check = self.l[parent] >= self.l[child]
            self.l[parent], self.l[child] = self.l[child], self.l[parent]
            child = parent
            parent = (child ) // 2

    def add(self, n):
        if len(self.l) > 0:
            """
            we are in 2i+1 or 2i+2
            idx = len 
            parent = idx - 1 // 2
            smaller than parent? -> pass
            larger than parent? -> switch
            --> recursive call
            """
            parent = (len(self.l)-1) // 2
            child = len(self.l)
            self.l = self.l + [n]
            self.swap(parent, child)
        else:
            self.l = [n]

    def find_place_of_i(self, i):
        left_child = 2*i+1
        right_child = 2*i+2

        if left_child < len(self.l) and self.l[left_child] > self.l[i]:
            self.l[i], self.l[left_child] = self.l[left_child], self.l[i]
            self.find_place_of_i(left_child)
        elif right_child < len(self.l) and self.l[right_child] > self.l[i]:
            self.l[i], self.l[right_child] = self.l[right_child], self.l[i]
            self.find_place_of_i(right_child)



    def heapsort(self):
        if len(self.l) == 1:
            self.sorted.append(self.l[0])
        elif len(self.l) == 2:
            if self.l[0] > self.l[1]:
                self.l[0], self.l[1] = self.l[1], self.l[0]
            tmp = self.l.pop()
            self.sorted += [tmp]
            self.heapsort()
        else:
            self.l[0], self.l[-1] = self.l[-1], self.l[0]

            tmp = self.l.pop()
            self.sorted += [tmp]
            while self.l[0] < self.l[1] or (len(self.l) > 2 and self.l[0] < self.l[2]):
                self.find_place_of_i(0)
            self.heapsort()


if __name__ == '__main__':
    ins = MaxHeap([4, 1, 3, 6, 7, 5])
    ins.add(2)
    ins.add(8)
    print(ins.l)
    ins.heapsort()
    print(ins.sorted)