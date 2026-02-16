# Object Oriented Programming in Python

- data type is a class
- variable of a data type is an obejct
- class name is in PascalCase
- Varibale name is in snake_case
- private data members are denoted by -
- public member functions(methods) are denoted by +
---
- `mylist1 = [1,2,3,4,5]`
   - When i do this, I m creating an object of `list` class and the members of `mylist1` are passed as arguments to the constructor of the list class and assigned to `mylist1[0]`, `mylist1[1]` and so on (index of the list object).
   - After the elements are assigned, mylist1 becomes an object of the list class, and you can access its elements using index notation.
- `mylist1 = list([1,2,3,4,5])`
   - explicitly calling list constructor
---
- built-in classes are : `list`, `dict`, `set`, `int`, `float`
   - no need to define classes for these built-in classes because python has provided us facility to use them directly

## METHODS VS FUNCTIONS
1. A method is essentially a function that is associated with an object. Methods are functions defined inside a class, and they are called on instances (objects) of that class. They always take the object itself (self in Python) as the first argument, which allows the method to operate on the object's attributes.
2. A function is a block of code that performs a specific task and can be called independently. Functions can take input arguments, perform operations, and return a value. They are defined using the `def` keyword.
3. `len()` is a function but `mylist.append()` is a method defined inside list class.

## Constructor = special / magic / dunder method <br>
- A constructor in Python is a special method that is automatically called when an object of a class is created. It is used to initialize the object's attributes (properties) when it is instantiated.
- The constructor method in Python is called `__init__()`.This method is automatically invoked when you create an object from a class.
- The first parameter of the constructor is always `self`, which refers to the current object being created.
Consturctor contains configuration code, initialization.

## self = keyword
- When you call a method on an object:
   - The object itself is automatically passed as the first argument to the method. The method receives this object using the `self` parameter.
- In OOP, only the objects of the class can access the methods of the class. This means that one method can not access any other methods of the same class. For calling one method from another method of the same class, self parameter i.e. the object itself is automatically passed to the method during method call. 

## Displaying Fractions using `__str__` method:
- `__str__` is a magic/dunder method in OOP
   - It is automatically called when we try to print an object. Whatever is the value returned by this method is printed.
   - If there is no such method, python displays the default string representation of the object
- `__add__` magic method: It is called when there is binary operation +  between two objects
- `__sub__` magic method: It is called when there is binary operation -  between two objects
- `__mul__` magic method: It is called when there is binary operation *  between two objects
- `__truediv__` magic method: It is called when there is binary operation /  between two objects

## Instance Variable:
- It belongs to a specific instance(object) of a class in Python.
- Each instance of the class has its own separate copy of the instance variables.
- Changes to instance variable of one object do not affect the instance variables of another object, even if both objects are from the same class.
- Defined in the constructor using `self` keyword


## Name Mangling: 
- Name mangling in Python is a mechanism used to make certain class attributes (usually those marked as private) less accessible from outside the class. 
- When you prefix a variable or method name with double underscores (__), Python changes the name internally by adding the class name as a prefix. 

## Encapsulation:
- Encapsulation refers to the concept of bundling data (attributes) and methods (functions) that operate on the data into a single unit, typically a class, and restricting direct access to some of the object's components.
- To make a varibale private (not accessible outside the class), data members' and methods' name is prefixed with `__`. Now this data member and method cant be accessed, even by object from outside the class.
- Data members and methods are hidden after doing this

## Reference Variable:
A variable that holds a reference (or pointer) to an object, rather than the object itself.

##
- Instance variable has separate value for each object/instance. They are defined inside the constructor
- Static variable/Class variable is maintained for all the objects of the class. They are defined outside the class


## Relationship: 
- describes how different classes or objects in python are related to each other
- Two types: Aggregation(has a) and Inheritance(is a)
   1. Aggregation(has a) : 
one class (the whole) contains objects of another class (the parts). 

## super() function:
Used to give access to methods and properties of a parent or sibling class. It allows you to call a method from the parent class inside a child class

## Polymorphism:
1. Method Overriding
2. Method Overloading
3. Operator Overloading

## Method Overloading:
- Not possible in python. Can be achieved logically.

## Operator Overloading:
- Can be done using magic methods.


