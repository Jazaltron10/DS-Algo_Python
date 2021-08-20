# **Data Structures** 
A data structure is a data storage format. it is the collection of values and the 
format they are stored in, the relationships between the values in the collection as
well as the operations applied on the data stored in the structure 


>## **Arrays** 
+    Analogy a collection of train carts 
+ They can be homogeneous(java, C++) or heterogeneous(Python) structures
+ The fundamental concept of arrays are their **indexes**
+ They are used for every operations on the array, By operations i mean: 
+ Accessing, Updating, inserting and Deleting 
+ It is a contiguous data structure
+ This means that the array is stored in blocks of memory that are right 
  beside each other with no gaps  
+ most programming languages uses a 0 index

>## **Operations on Data Structures**
+ Access and read values 
+ Search for an arbitrary value
+ Insert values at any point into the structure
+ Delete values in the structure

>## **Insert  operations**
+ adding at the beginning of the list 
+ list resizing growth pattern in python is 
+ 0,4,8,16.25,35,46...
+ When resize is triggered space required increases as memory allocation increases
+ You can add at the end of the list 
+ You can combine 2 arrays to form a new one 
+ Inserting at the top moves or shifts every element in the array to the right 
+ While Deleting from the top moves or shifts every element in the array to the left 
 

        numbers = []
        numbers.append(2)
        print(numbers)
        
        also 
        numbers = []
        numbers.extend([4,5,6])
        print(numbers)               # gives you =>[4, 5, 6]
       

>## **Building a Linked List** 
+ Why do we build a data structure 
+ each data structure solves a specific problem
+ A linked list is a linear data structure where each element in the list is contained in a separate object called a node.<br> 
  
        A node models two pieces of information, an individual item of the data we want to store and a reference to the next node in the list 

+ first node is called the head 
+ last node is called the tail, this denotes the end of the list  
+ every node in the list points to the next node on the list except the tail node which points to nothing 
+ Nodes are what are called Self Referential Objects
+ **Self Referential Objects** means the definition of a node includes the node itself 
+ Singly and Doubly Linked list are the implementations that exists.
+ Singly linked list points only to the next node on the list 
+ Doubly linked list points to both the next as well as the previous node on the list
+ Going from one node to the next is what is called **list traversal**

>## **Syntax**


      >>> l = LinkedList()
      >>> N1 = Node(10)
      >>> l.head = N1
      >>> l.size()
      1  


    $ python -i Linked_List.py
    >>> l = LinkedList() 
    >>> l.add(1)
    >>> l.add(2)
    >>> l.add(3)
    >>> l.add(4)
    >>> l.add(-5)
    >>> l
    [Head: -5]-> [4]-> [3]-> [2]-> [Tails: 1]
    >>>


>## **Searching**
    
    >>> l = LinkedList()   
    >>> l.add(23)
    >>> l.add(96)
    >>> l.add(98)
    >>> l.add(546)
    >>> l.add(623)
    >>> n = l.search(2) 
    >>> n
    >>> n = l.search(23)
    >>> n
    <Node data: 23>
    >>> l
    [Head: 623]-> [546]-> [98]-> [96]-> [Tails: 23]
    >>>



**found = false** is the same as **not found = true** 


   

























