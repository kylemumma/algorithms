'''
This is my implementation of randomized linear time selection
algorithm. i.e. quickselect
'''
import random
class Select:
    # selects and returns kth smallest element of arr
    def randlinearselect(self, arr, k):
        return self._randlinearselect(arr, k, 0, len(arr)-1)
    
    def _randlinearselect(self, arr, k, start, stop):
        #if stop-start == 0:
            #return arr[start]
        
        p = self.randpivot(start, stop)

        p = self.partition(arr, start, stop, p)

        if (p-start+1) == k:
            return arr[p]
        elif (p-start+1 > k):
            # recurse left
            return self._randlinearselect(arr, k, start, p-1)
        else:
            # recurse right
            return self._randlinearselect(arr, k-(p-start+1), p+1, stop)
    
    # partition around elem at p (lumoto) return new pivot idx
    def partition(self, arr, start, stop, p):
        self.swap(arr, start, p)
        i,j = start+1, start+1
        while j <= stop:
            if arr[j] < arr[start]:
                self.swap(arr,i,j)
                i += 1
            j += 1
        self.swap(arr, start, i-1)
        return i-1

    # swap elements i and j
    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    def randpivot(self, start, stop):
        return random.randint(start, stop)

sel = Select()
arr = [1,1,1,1,1,1,8]
print(sel.randlinearselect(arr, 7))