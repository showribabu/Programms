
import math
n=int(input('Enter how many points are there:'))
l=list(map(int,input('Enter '+str(3*n)+' elemnts:').split()))

print(l)

ll=[]
#seperate 3 points..
for i in range(0,len(l),3):
    # d=[l[i],l[i+1],l[i+2]]
    d=l[i:i+3]
    ll.append(d)

l=ll[::]
print(l)

#now we can calculate the distance based on the movements...

def distance(x1,y1,z1,x2,y2,z2):
    # return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z2-z1)**2)
    return (math.sqrt((x2 - x1)**2 + (y2 - y1)**2)) + abs(z2 - z1)


total=0

for x in range(n-1):
    x1,y1,z1=l[x]
    x2,y2,z2=l[x+1]
    # print(x1,y1,z1)
    # print(x2,y2,z2)
    if z1==z2:
        #same surface..arc distance.. (deg * distance)
        # dis=distance(x1,y1,z1,x2,y2,z2)
        arc_d=(2*math.pi*distance(x1,y1,z1,x2,y2,z2))/6
        total+=round(arc_d,2)
    else:
        #diff ..distance..
        sur_d=distance(x1,y1,z1,x2,y2,z2)
        total+=round(sur_d,2)

print(total)
        
        
    





# import math

# def shortest_distance(x1, y1, z1, x2, y2, z2):
#     # Calculate the shortest distance between two points (x1, y1, z1) and (x2, y2, z2)
#     return (math.sqrt((x2 - x1)**2 + (y2 - y1)**2)) + abs(z2 - z1)

# def total_distance_traveled(N, points):
#     total_distance = 0.0
    
#     for i in range(1, N):
#         x1, y1, z1 = points[3*(i-1)], points[3*(i-1)+1], points[3*(i-1)+2]
#         x2, y2, z2 = points[3*i], points[3*i+1], points[3*i+2]
        
#         # If points are on the same face, move in an arc of a circle with a subtended angle of 60 degrees
#         if z1 == z2:
#             arc_distance = (2 * math.pi * shortest_distance(x1, y1, z1, x2, y2, z2)) / 6
#             total_distance += round(arc_distance, 2)
#         else:
#             # Points are on different faces, move by the shortest path on the surface of the cube
#             surface_distance = shortest_distance(x1, y1, z1, x2, y2, z2)
#             total_distance += round(surface_distance, 2)
    
#     return total_distance

# # Example 1
# N1 = 3
# points1 = [1, 1, 10, 2, 1, 10, 0, 1, 9]
# print(total_distance_traveled(N1, points1))  # Output: 4.05

# # Example 2
# N2 = 3
# points2 = [1, 1, 10, 2, 1, 10, 0, 5, 9]
# print(total_distance_traveled(N2, points2))  # Output: 6.05



    
    