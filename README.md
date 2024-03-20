# Python-week--1
# DAY 1: INTRODUCTION TO PYTHON
Installing python,jupyter notebook.
Python file: ipynb
Python data structures: with examples
-List=[2,4,6,8,10]
-Set={'a','b','c','d'}
-Tuple=((42,"Hello"),("Me",4))
-Dictionary=[{"name":"Lona","Age":40}]
Managed to test Jupyter and running the lines of code based on data structures.It is not important to put the elements of a set in order and in a list it's important.
Tuples cannot be modified when declared.Operators-instruction that perform operations on variables and values in python.Most familiar operator in python(Arithmetic operator for mathematics calculations:  +,*.
Boolean operators: OR, NOT, AND.
Python function is declared or defined as 'Def'.Conditional statements( if, elif & else)

# DAY 2 : CLASSES & OBJECTS
Class,instance,method/function.
After creating a class,there has to be a new instance of a class.
Init -it's important to initialize so that a method can take arguments.
      # Factorial
      -gives the number of possible arrangements of a set of items/length "n"
      E.G 4!= 4*3*2*1
      The factorial of 0 returns 1 , as it has 1 posssible arrangement/length
      If a factorial is negative(-) & a float ,it returns NONE.

# DAY 3 : Basic Data types
Classes are created to make it easier to re use the code.
Python has a built in funcion called TYPE...
== For comparing
* Number casting: changing one type to another.
  E.G num_1="100"
      num_2="200"
  num_1=int(num_1)
  num_2=int(num_2)
  print(num_1 + num_2)
# DAY 4
Abs(removes a negative sign of a number).
Each byte has 8 bits.
# Alternate numbers
int('101',2)
   =5
   (1*2^2) + (0*2^1) + (1*2^0)
  my_list= [5,7,8,6,9,12,21,50]
  even_list= [x for in my_list if x %2 ==0]
  add_list= [x for in my_list if x 2=! ==0]
  max_value=print(my_list.max())
  # List Slicing
  list[start index:end index:step]
  If the end index is not specified,it will print all the values.
  The end index is not printed but prints the value before the index.
  steps meaning skips a certain number of values.
  -APPEND used to add a certain value in a list
  -POP used to remove a certain item in a list.
  # default dictionary
  has to be imported from collections
  E.G defaultdic imported from collection packages
       # BASIC CONTROL FLOW
       for n in range (1,101):
    if n % 15 == 0 :
        print('Fizzbuzz')
    else:
        if n %3 == 0 :
            print('Fizz')
        else:
             if n %5 == 0 :
                 print('Buzz')
             else:
                  print(n) 
      Ternary operator syntax:
      [on_true] if [expression] else [on_false]
      IF THE EXPRESSION IS TRUE, IT WILL RETURN ON TRUE.
# DAY 5
Configured Git
commands to configure Git :
git config --global user.name "Anartty"
git config --global user.email "anathinartty87@gmail.com"

git config --global --list

  # Python-week--2
 # Basic Functions
NB:
. When using a keyword argument in Python, They must come after positional arguments
-First 2 arguments can't be changed
# Positional Arguments: used to pass in any number of variables & it should be before argument name.
Function can be called usng one or more arguments.
# KEYWORD ARGUMENT
POSITIONAL ARGUMENTS: - STORED AS A TUPLE
-KEYWORD ARGUMENT:- STORED AS A DICTIONARY
* It has a key & a value(so DIC is appropriate to store its values)
  VARIABLES & SCOPE
  Local functions-Method that allows us to access all variables with function
  * LAMBDA FUNCTION
  * No need to write 'return' function as it's already implified in Python
  * Sort Function- used to arrange items in order
  * Services are up- Determines if there will be anything returned or not.
      So, if it's true-it will return a response....if it's false it will not reurn any response.
  * .Random(Generates a float between 0 and 1
 -<0.5: 50 % chances
-0.25: 25% chances
  -0.1: 10%

