 # Python-week--2
 # Basic Functions-DAY 1
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
  * .Random(Generates a float between 0 and 1)
 -<0.5: 50 % chances
-0.25: 25% chances
  -0.1: 10%
    
    # CLASSES & OBJECTS-DAY 2
    ANATOMY OF A CLASS
    * Every Dic in Python has a Get() method
    * Get method- makes it easier to define an algorith method.
    * STATIC can be changed
    * Get method- retrieves the value of the variable.
    * Decorator- special annotation for a function .
      # INHERITANCE
      -When one class inherits the attributes& methods of another class.
      # PARENT CLASS- when inherited from.
      # CHILD CLASS-new class that extends an existing class.
      -It is possible to add a new method to the new class.
      
      # ERROR & EXCEPTIONS- DAY 3
      _Exceptions are determined during run time.
      -Errors can't be retrieved.
      Division by Zero: Type of arithmetic error, type of exception & extends the base exception class.
      SYNTAX for TRY/EXCEPT: e.g
            try:
              1/0
            Except Exception as e:
              print(type(e))
      # Finally Statement
      -Always execute & get printed out
      -time.time will execute the current time & seonds
         TYPE ERROR
      E.G adding a string into an integer
      -Class CustomException extends Exceptions.

      # THREADS AND PROCESSES- DAY 4
      NB: pip install multiprocess
      - Have to import threading & time
        # MULTIPROCESSING
        -There is a file called 1000seconds.py
        * It calls time.sleep for thousand seconds
        * Import process from multiprocess in order to use it
        * Threads share the same space in memory.
          FORMATTING
          .2f(2 decimals)....E.G 98>>>98.00
          {}: Place holder
          Open function takes 2 parameters(filename, mode)
          # DIFFERENT MODES
          *r-read-shows an error if the file doesn't exist
          *a- Append- Creates the file if it doesn't exist
          * w-writes-Creates the file if it doesn't exist
          * x-create- shows an error if the file doesn't exist
          * t-for text
          * b-Binary (like images)
            NB: readline() for returning one line from a file
          # CSV FILE : 10_02_us.csv
          -JSON : Not a dictionary/python
                It's a string that is in JSON format
          -For JSON format to be turned into a dictionary- json has to be imported
          -COVERTING FROM JSON TO PYTHON
          * json.loads()
          -COVERTING FROM PYTHON TO JSON
          * json.dumps() 
          * Strip method: for removing white spaces before & after the string
          To accept multiple values or if the number of args is unkown, can add * before the parameter name
          -Append- index doesn't use the index
          -String is immutable
          
          
