items= [14,33,27,35,10]
def bubble_sort(items):
        """ Implementation of bubble sort """
        for i in range(len(items)):
                for j in range(len(items)-1-i):
                        if items[j] > items[j+1]:
                                items[j], items[j+1] = items[j+1], items[j]     # Swap!
        return items
print bubble_sort([14,33,27,35,10])
 