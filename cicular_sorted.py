#circular sorted array ...

# 11 12 3 5 6 7 8 9
# >pivot< both values are greather in surrounding...
# That index represents no of rotations required....

"""
1) Linear approach -> if i use linear to find pivot elements it is not good

2) Binary appproach -> if i use binary to find pivot elements it is easyly foundated..

""" 

#we are always search for smaller element ...


def binary_circular(l):
    low=0
    high=len(l)-1

    while(low <= high):
        mid=low+ (high-low)//2
        nxt =(mid+1)%len(l)
        prev=(mid-1)%len(l)

        if l[low]<=l[high]: 
            return low
            #corrrect order... like low <high... 
        #     print('Base')
        #     return low 
        # mid=low+ (high-low)//2

        #check pivot.. 
        if l[mid]<=l[nxt] and l[mid]<=l[prev]:
            return mid 
        
        '''
        if l[mid] >= l[low]:
            low = (mid + 1) % len(l)
        elif l[mid] <= l[high]:
            high = (mid - 1) % len(l)
        '''
        if l[mid]>=l[high]:
            low=(mid+1)%len(l)
        elif l[mid]<=l[low]:
            high=(mid-1)%len(l)
        
            
            
      

l=[int(x) for x in input().split()]
print(l)
print(binary_circular(l))


'''

def binary_circular(l):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = low + (high - low) // 2
        nxt = (mid + 1) % len(l)
        prev = (mid - 1) % len(l)

        # Check if array is in the correct order without any rotation
        if l[low] <= l[high]:
            return low

        # Check if mid element is the pivot
        if l[mid] <= l[nxt] and l[mid] <= l[prev]:
            return mid

        # Adjust low or high index based on the comparison with mid element
        if l[mid] >= l[low]:
            low = (mid + 1) % len(l)
        elif l[mid] <= l[high]:
            high = (mid - 1) % len(l)

l = [int(x) for x in input("Enter the elements of the circularly sorted array: ").split()]
pivot_index = binary_circular(l)
print("The index of the pivot element is:", pivot_index)
'''