#Lists are ordered,muteable and allows duplicate
# The elements of a list can be accessed by Indexing

scores = [88, 92, 79, 92, 65]
scores[0]        # 88  (first element)
scores[-1]       # 65  (last element)
scores[1:3]      # [92, 79]  (slice: index 1 up to, not including, 3)
scores[::-1]     # [65, 92, 79, 92, 88]  (reversed)
scores[::2]      # every 2nd element


#Mutating lists
scores.append(100)          # add to end
scores.insert(0, 50)        # insert at position
scores.remove(92)           # removes FIRST occurrence of value 92
scores.pop()                 # removes & returns last element
scores.pop(0)                # removes & returns element at index 0
scores.sort()                 # sorts in place, ascending
scores.sort(reverse=True)     # descending
sorted(scores)                 # returns a NEW sorted list, original untouched

'''
Important notes:
1. sorted() returns a new list, while .sort() sorts the list in place and returns None.
'''

#list comphrehensions
squared = [x**2 for x in scores]
passing = [x for x in scores if x >= 70]              # filter
labels  = ["pass" if x >= 70 else "fail" for x in scores]  # conditional expression