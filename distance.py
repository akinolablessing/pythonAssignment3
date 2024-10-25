import math
radius= 6371.01
x1 =float(input("Input the latitude of coordination:"))
y1 =float(input("Input the longitude of coordinaton:"))
x2 =float(input("Input the latitude of coordination:"))
y2 =float(input("Input the longitude of coordinaton:"))
result = math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2)
distance =radius*math.acos(result)
print(f"The distance between those points is:{distance} km")