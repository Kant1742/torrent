# a = []
# l = int(input())
# h = int(input())

# for i in range(l):
#     a += [input().split()]

# for i in range(h):
#     for b in range(l-1, 0, -1):
#         print(a[b][i], end=' ')
#     print(a[0][i])

a_string = "1 2 3"
print(a_string)
splited = a_string.split()
print(splited)
print(list(map(int, splited)))
print('---'.ljust(23, 'w'))

print(pow(10, 4, 2))

from typing import Optional, List, Tuple, Union, Dict

amount: int
amount = 12
# amount = None  # error (None)
print(amount)

# title: List[Union[int, str]] = [43, 'ds', 'dfsf', 12.3]  # error (float)
# title: List[Union[int, str]] = [43, '329', 'efsdf', 'dfsf']  # correct
title: List[int] = [43, 5, 44]  # correct (if we do not uncomment another `title`)
print(title)


my_tuple: Tuple[int, int, str] = (1, 2, 'hui')  # each item has its own type
my_tuple2: Tuple = (1, 2, 3, 'hui')
print(my_tuple)

# for Dict the type of the keys and the type of the values
my_dict: Dict[str, str] = {'Some shit': 'has flavour', 'other shit': 'has not'}
print(my_dict)


class MyClass:
    
    TOTAL_OBJECTS=0
    
    def __init__(self):
        MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS+1
       
    @classmethod
    def total_objects(cls):
        print("Total objects: ", cls.TOTAL_OBJECTS)

# Creating objects of parent class       
my_obj1 = MyClass()
my_obj2 = MyClass()


# Creating a child class
class ChildClass(MyClass):
    TOTAL_OBJECTS=0    
    pass

ChildClass.total_objects()


class MyClassStatic:
    
    TOTAL_OBJECTS=0
    
    def __init__(self):
        MyClassStatic.TOTAL_OBJECTS += 1
       
    @staticmethod
    def total_objects(self):
        print("Total objects: ", self.TOTAL_OBJECTS)

my_static_class = MyClassStatic()
my_static_class_2 = MyClassStatic()

# Creating a child class
class ChildClass(MyClassStatic):
    TOTAL_OBJECTS=0

ChildClass.total_objects(my_static_class_2)
