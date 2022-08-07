#Theory

1. How does Object Oriented Programming differ from Process Oriented Programming?

The objective of Process Oriented programming is to break down a program into a collection of variables and data structures whereas in object-oriented programming the program is broken down into objects. Process Oriented programming uses procedures to operate on data structures, while object-oriented uses objects.
Some key differences include:
Characteristic differences
Process oriented programming uses local variables, selection, modularisation, iteration and sequence.
OOP uses objects, abstraction, polymorphism, encapsulation,  inheritance and methods.
Accessing:
OOP has 3 accessing modes, public, private, protected, whereas process orientated has none.
Execution of code:
In Process Oriented Programming functions are executed systematically one-by-one whereas OOP functions can execute simultaneously
Division:
In Object-oriented programming, the program is divided into objects whereas in Process Oriented programming the program is divided into sub-procedures.
Although both approaches are good and used widely, generally OOP is better for bigger and more complex applications as it is easier to maintain, modify and reuse. However, OOP is harder to master due to the concepts of inheritance, abstraction, polymorphism and encapsulation. So in the case of building smaller applications or for inexperienced engineers, using Process Oriented programming is quicker and more suitable.

2. What's polymorphism in OOP?

Polymorphism is one of the core concepts of object oriented programming. It is the ability to present the same interface for differing data types. Although polymorphism is not a concept related to OOP, OOP is related to polymorphism as it inherently supports it.
An example of polymorphism would be having a base class of Vehicle which has a Wheels property. When sub-classes are created e.g. car, bike etc. the sub-class is responsible for assigning it’s own number of Wheels. The base class doesn’t concern itself with how many wheels it’s sub-classes have. Although the sub-classes share a common interface, they have their own values and functionality.
Polymorphism allows OOP code to be more extendable and modular. It removes the need for conditional statements as the objects are interchangeable. Ultimately it simplifies the programming interface and can be reused and implemented easily.

3. What's inheritance in OOP?

Inheritance is one of the core concepts of object oriented programming. It is the concept of deriving properties and methods from another class via a hierarchy of classes. Typically you will see a child/parent relationship where a child inherits that of the parents class.
An example of inheritance would be having a parent class of Animal where it has the property of firstname and a method to printname. On its own this class can be used and executed. From here a child class of Cat can be created which inherits the Animal properties and methods by passing it in the parameters:
class Cat(Animal):
  pass
Here the Cat will also have a firstname property and printname method and can be executed like so:
x = Cat("Bob")
x.printname()
You can add additional properties/methods to the Cat class and it will not affect the parent class. You can also override anything passed down by giving it the same name in the child class, this also won’t affect the parent class.
Inheritance in OOP has lots of benefits. For example it creates code reusability as the multiple children can inherit a parent's properties, meaning the code is only needed to be written in the parent class. For this reason it is also quicker and easier to maintain.

4. If you had to make a program that could vote for the top three funniest people in the office, how would you do that? How would you make it possible to vote on those people?

```
nominees = {}


def funniest(nominee):
    if nominee in nominees:
        new_value = int(nominees[nominee]) + 1
        nominees.update({f"{nominee}": f"{new_value}"})
    else:
        nominees.update({f"{nominee}": 1})
    return nominees


print(funniest("james"))
print(funniest("james"))
print(funniest("james"))
print(funniest("Michelle"))
```

5. What's the software development cycle?

The Software Development Lifecycle (SDLC) is a methodology that defines the process of creating software. It focuses on these key phases:
Requirement analysis
Gets input from all stakeholders to analyse current systems, identifying their pros and cons and either carrying them forward (in the case of pros) or working to eliminate them (in the case of cons)
Planning
Determines how those pros/cons can be managed. This stage looks at risks and feasibility whilst keeping quality, cost and timeframe at the forefront.
Software design such as architectural design
Beginnings of turning specifications into design plans. This stage also has intense scrutinisation and input across the board to encourage feedback and suggestions.
Software development
This is the stage where those designs are now put into code and actually built into a product.
Testing
Testing is both manual and programmatic. It looks at whether what was built is what is wanted. It highlights any defects and deficiencies. In the SDLC there is a big focus on testing.
Deployment
This is the stage where the product is actually used. It includes pushing to production so the public can use it as well as staging and testing environments so the software can be tested internally and externally (e.g. by a focus group).
The cycle prioritises producing software that is of the highest quality with the lowest cost in the shortest time possible. It works by cyclically looking at current systems and evaluating where they fall short in achieving the 3 goals. It then defines a new system i.e. how can current shortcoming be removed/reduced? This is applied to the creation of the software, starting with planning then moving through design, development, testing and finally deployment. The evaluation of current systems means that mistakes that could’ve happened are removed before these steps take place. Examples of SDLC models are agile and waterfall.

6. What's the difference between agile and waterfall?

Agile separates the project development lifecycle into sprints and is known for its flexibility which allows changes to be made even if the initial planning has been completed whereas Waterfall is divided into distinct phases and can at most times be quite rigid as there is no scope for changing requirements once the project development starts. Agile follows an incremental approach and can be considered as a collection of many different projects but Waterfall methodology is a sequential design process and will be completed as one single project. Agile follows an iterative development approach because of this planning, development, prototyping and other software development phases may appear more than once and the requirements are expected to change and evolve. However all the project development phases like designing, development, testing, etc. are completed once in the Waterfall model, this method is ideal for projects which have definite requirements and changes not at all expected. Finally Agile Team members are interchangeable, as a result, they work faster. There is also no need for project managers because the projects are managed by the entire team. In the waterfall method, the process is always straightforward so, project manager plays an essential role during every stage of the software development life cycle.

7. What is a reduced function used for?

Python has a function called reduce() that allows you to reduce a list in a more concise way. Below is the syntax:\
`reduce(fn,list)`\
To use the reduce() function, you need to import it from the functools module:\
`from functools import reduce`\
The reduce() function cumulatively adds two elements of the list from left to right and reduces the whole list into a single value.

At first step, first two elements of sequence are picked and the result is obtained.\
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.\
This process continues till no more elements are left in the container.\
The final returned result is returned and printed on console.

The reduce() function can also be combined with operator functions to achieve the similar functionality as with lambda functions and makes the code more readable.\
`import functools`\
`lis = [1, 3, 5, 6, 2, ]`\
`print(functools.reduce(lambda a, b: a+b, lis))`

`import functools`\
`import operator`\
`lis = [1, 3, 5, 6, 2, ]`\
`print(functools.reduce(operator.add, lis))`

8. How does merge sort work

Merge Sort is a sorting algorithm that works by breaking down a problem until it becomes simple enough to be solved directly. So in this algorithm, the array is initially divided into two equal halves and then they are combined in a sorted manner. It then continuously splits the array in half until it cannot be further divided. This means that if the array becomes empty or has only one element left, the dividing will stop. If the array has multiple elements, we split the array into halves and recursively invoke the merge sort on each of the halves. Finally, when both the halves are sorted, the merge operation is applied. Merge operation is the process of taking two smaller sorted arrays and combining them to eventually make a larger one.

Algorithm:\
```
step 1: start
step 2: declare array and left, right, mid variable 
step 3: perform merge function.
        mergesort(array,left,right)
        mergesort (array, left, right)
        if left > right
        return
        mid= (left+right)/2
        mergesort(array, left, mid)
        mergesort(array, mid+1, right)
        merge(array, left, mid, right)
step 4: Stop
```

The Drawbacks of Merge Sort:
Slower comparative to the other sort algorithms for smaller tasks.
The merge sort algorithm requires an additional memory space of 0(n) for the temporary array.
It goes through the whole process even if the array is sorted.


9. Generators - Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. What is the use case?

Generators are good for evaluating large sets of data, in particular calculations involving loops, where you are unsure if you’ll need to use all the results. It is also useful to use a generator if you don’t want to allocate memory for all results at the same time. Generators return a list’s values one-by-one and the function is paused before the next item is requested.
Another use for generators is to replace callback functions with iteration. In some situations you want a function to occasionally report back to the caller, to give an update, especially if the function is doing a lot. The generator approach is that the work-function (now a generator) will update whenever it wants to report something. The caller, instead of writing a separate callback and passing that to the function, does all the reporting work in a 'for' loop which contains the generator.
Here is a code example using fibonacci function vs generator:

```
def fibon(n):
a = b = 1
result = []
for i in xrange(n):
	result.append(a)
	a, b = b, a + b
return result
def fibon(n):
a = b = 1
for i in xrange(n):
	yield a
	a, b = b, a + b
```
Where if n is a really big number a generator would evaluate each value at a time.

10. Decorators - A page for useful (or potentially abusive?) decorator ideas. What is the return type of the decorator?
