import random
class Sort:
    # quicksort using lomuto partition and random pivot
    def quicksort(self, arr):
        self._quicksort(arr, 0, len(arr)-1)

    def _quicksort(self, arr, start, stop):
        if stop-start <= 0:
            return

        p = self.randpivot(start,stop)

        p = self.lomutopartition(arr, start, stop, p)

        self._quicksort(arr, start, p-1)
        self._quicksort(arr, p+1, stop)

    # returns a random pivot index
    def randpivot(self, start, stop):
        return random.randint(start,stop)

    # partition around the element at i, 
    # returns new idx of pivot
    def lomutopartition(self, arr, start, stop, i):
        self.swap(arr, start, i)
        i, j = start+1, start+1
        while j <= stop:
            if arr[j] < arr[start]:
                self.swap(arr,i,j)
                i += 1
            j += 1
        self.swap(arr,start,i-1)
        return i-1

    # swap the elements at i1 and i2
    def swap(self, arr, i1, i2):
        tmp = arr[i1]
        arr[i1] = arr[i2]
        arr[i2] = tmp


if __name__ == "__main__":
    sort = Sort()
    tests = [[0], 
             [2,4],
             [5,3],
             [],
             [4,67,2,1,54,8,0,3,56,12,6],
             [1,2,3,4,5,6,7,8,9],
             [9,8,7,6,5,4,3,2,1],
             [1,1,1,1,1,1,1],
             [1,1,1,8,1,1,1],
             [1,4,6,3,4,7,12,4,7,3,9]]
    for arr in tests:
        sort.quicksort(arr)
        print(arr)