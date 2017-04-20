class BinarySearch(list):
    
    def __init__(self, length, step):
        
        super(BinarySearch, self).__init__()

        # populate the class based on the length and step arguments
        for i in range(1, length+1):
            self.append(i * step)

        # define a length attribute
        self.length = len(self)

    def search(self, val):
        
        # initialize the top and bottom indices
        top = 0
        bottom = len(self) - 1
        index = 0
        found = False

        # initialize counter
        counter = 0

        # check if val is the top or bottom element
        if val == self[top]:
            index = top
            found = True
        elif val == self[bottom]:
            index = bottom
            found = True

        # check if val is not present in the list
        if val not in self:
            found = True
            index = -1

        # binary search algorithm using a while loop
        while top <= bottom and not found:
            middle = (top + bottom) // 2
            if self[middle] == val:
                found = True
                index = middle
            else:
                counter += 1  # update counter when an interaction occurs
                if val < self[middle]:
                    bottom = middle - 1
                else:
                    top = middle + 1

        return {'count': counter, 'index': index}

