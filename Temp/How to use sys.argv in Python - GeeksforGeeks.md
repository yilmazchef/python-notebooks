[Command line arguments](https://www.geeksforgeeks.org/python-set-6-arguments/) are those values that are passed during calling of program along with the calling statement. Thus, the first element of the array `sys.argv()` is the name of the program itself. `sys.argv()` is an array for [command line arguments](https://www.geeksforgeeks.org/python-set-6-arguments/) in Python. To employ this module named “`sys`” is used. `sys.argv` is similar to an array and the values are also retrieved like Python array.

**The sys module**

The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

**Examples:**

`import` `sys`

`print``(``"This is the name of the program:"``, sys.argv[``0``])`

`print``(``"Argument List:"``,` `str``(sys.argv))`

**Output:**

![sys.argv](https://media.geeksforgeeks.org/wp-content/uploads/20191213134403/Screenshot-1662.png)

The above program has been saved by the name “com.py” and thus has to be called in the following in command prompt

**Functions that can be used with sys.argv**

-   **len()-** function is used to count the number of arguments passed to the command line. Since the iteration starts with 0, it also counts the name of the program as one argument. If one just wants to deal with other inputs they can use (len(sys.argv)-1).
-   **str()-** this function is used to present the array as a string array. Makes displaying the command line array easier and better.

**Example:**

`import` `sys`

`print``(``"This is the name of the program:"``,`

       `sys.argv[``0``])`

`print``(``"Number of elements including the name of the program:"``,`

       `len``(sys.argv))`

`print``(``"Number of elements excluding the name of the program:"``,`

      `(``len``(sys.argv)``-``1``))`

`print``(``"Argument List:"``,`

       `str``(sys.argv))`

**Output:**

![sys.argv](https://media.geeksforgeeks.org/wp-content/uploads/20191213134433/Screenshot-1671.png)

The following program performs addition using inputs given during runtime:

`import` `sys`

`add` `=` `0.0`

`n` `=` `len``(sys.argv)`

`for` `i` `in` `range``(``1``, n):`

    `add` `+``=` `float``(sys.argv[i])`

`print` `(``"the sum is :"``, add)`

**Output:**

![sys.argv](https://media.geeksforgeeks.org/wp-content/uploads/20191213141028/Screenshot-1692.png)