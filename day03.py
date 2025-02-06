#LIST:-[] 
#......Mutable data type
# ...store different type of element
#.......allow duplicates
#.....allow indexing


am=[8,6,1,8,1,2,9,0,7,1,"chandra"]
print(am)
print(len(am))

#indexing

#Positive indexing
print(am[6])
print(am[3])
print(am[7])

#Negative indexing
print(am[-1])
print(am[-2])
print(am[-5])

#Slicing
print(am[0:6:2])
print(am[-1:-4:3])
print(am[-1:5:-3])

#Append:-    Element add to last.

am=[8,6,1,8,1,2,9,0,7,1,"chandra"]
am.append("solo leveing")
print(am)

#extaent:-   Add bulk data (or) multi data last.
am=[8,6,1,8,1,2,9,0,7,1,"chandra"]
am.extend([7,76,6,7,89,4,2,5,83,2])
print(am)

#Count:-  Count to the elements.
am=[8,6,1,8,1,2,9,0,7,1,"chandra"]
print(am.count(8))


#REmove:-    RE-move the element
am=[8,6,1,8,1,2,9,0,7,1,"chandra"]
am.remove(0)
print(am)

#Pop:-  Pop is take index and remove the element.
am=[8,6,1,8,1,2,9,0,7,1,"chandra"]
am.pop(3)
print(am)

#Instert:- Particular position  add elements and data .
am=[8,6,1,8,1,2,9,0,7,1,"chandra"]
am.insert(4,"Solo leveing")
print(am)


#TUPLE:-   
# allow different types of elements
#allow duplicates
#allow index and slicing
#INmutabul
#no methods we can use bluitin

an=(9,8,8,0,2,9,3,0,7,7,"avinash")
print(len(an))

#indexing
print(an[-1])
print(an[0])
print(an[1])
print(an[-3])
print(an[5])

#slicing
print(an[0:4:2])
print(an[0:4:-1])
print(an[4:1:2])

#Tuples NO methods use MIN and Max
solo=(9,8,8,0,2,9,3,0,7,7,"avinash")
#print(min(solo))
#print(max(solo))
#print(sum(solo))
print(len(solo))


#type of Tuple:-
# 1. Concatenation
# 2. Iteration
# 3.Mumbership operation
# 4.Identity operation
# 5.Repetation 
                         # print(type(solo))


# 1. Concatenation:-()

t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)

# 5.Repetation
solo=(9,8,8,0,2,9,3,0,7,7,"avinash")
print(solo*2)

# 2. Iteration
for i in solo:
    print(i)
# 3.Mumbership operation
print(1 in solo)
print(11  not in solo)
t1=(1,2,3)
t2=(4,5,6)
t3=(1,2,3)
print(t1 is t2)
print(t1 is t3)
print(t1 is not t2)
