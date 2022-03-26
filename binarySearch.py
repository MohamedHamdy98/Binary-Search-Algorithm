class BinarySearch:
    def __init__(self, list, item):
        self.list = list
        self.item = item

    def showList(self):
        print(f'The list is = {self.list}')

    def showNumber(self):
         print(f'The item is = {self.item}')

    def binary_search(list, item):
        low = 0
        high = len(list) - 1
        while low <= high:
            mid = (low + high)
            guess = list[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1 
            else:
                low = mid + 1
        return None


ls = [1,3,5,2,4,6]
sortList = sorted(ls)

bs = BinarySearch(sortList, 3)

bs.showList()
bs.showNumber()
print(f'The index of the number is : {BinarySearch.binary_search(sortList,3)}')
    
