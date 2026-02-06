"""
Write a python program to perform following operations on Tuples :
a) Create and access a Tuple
b) Nested Tuple
c) Repetition of Tuple
d) Concatenation of Tuples
"""

# a) Create and access a Tuple

Tuple1 = (10,20,30,40,50)
print("Tuple :", Tuple1)
print("First Element :", Tuple1[0])
print("Last Element :", Tuple1[-1])


# b) Nested Tuple

Tuple2 = (1,2,(3,4,5),6)
print("Nested Tuple :", Tuple2)
print("Access Nested Element :", Tuple2[2][1])


# c) Repetition of Tuple

Tuple3 = ('A','B')
Repeated_tuple = Tuple3*3
print("Original Tuple :", Tuple3)
print("Repeated Tuple :", Repeated_tuple)

# d) Concatenation of Tuples

Tuple4 = (100,200)
Tuple5 = (300,400)
Concatenated_tuple = Tuple4 + Tuple5
print("First Tuple :", Tuple4)
print("Second Tuple :", Tuple5)
print("Concatenated Tuple:", Concatenated_tuple)