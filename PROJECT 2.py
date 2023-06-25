Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #program to perform different set operations
>>> 
>>> #sets are define
>>> A={0,2,4,6,8};
>>> B={1,2,3,4,5}
>>> 
>>> #union
>>> print("Union :", A | B)
Union : {0, 1, 2, 3, 4, 5, 6, 8}
>>> 
>>> #intersection
>>> print("Intersection :",A & B)
Intersection : {2, 4}
>>> 
...  
>>> #difference
>>> print("Difference  :",A-B)
Difference  : {0, 8, 6}
>>> 
>>> #symmetri difference
>>> 
>>> #symmetric difference
>>> print("Symmetric difference  :",A^B)
Symmetric difference  : {0, 1, 3, 5, 6, 8}
