"""
Removing Elements Without Using Any Auxilary array change list item in place.
Ex:- Remove  elements which are greater thanor equal to 27 in given list
list=[27,85,0,5,7,29,22,3,1,44,0,10,29]
"""
list=[27,85,0,5,7,29,22,3,1,44,0,27,10,29]
print(f"Original list {list}")
"""
Since I am using remove() i m using two loops cause when "remove()" will remove one element it 
will skip one index so two consecutive removal not possible so in 2nd interation those target element
not removed in first iteration will remove
"""
for i in range(0,2):
    for item in list:
        if item >= 27:
            list.remove(item)

print(f'After Removing Element List: {list}')