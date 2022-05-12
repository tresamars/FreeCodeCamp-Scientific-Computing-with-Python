# FreeCodeCamp-Scientific-Computing-with-Python

My solutions to the 5 projects required in the Scientific Computing with Python course from freeCodeCamp.
All passed the automated test suits provided by the course.

Arithmetic formatter:
	A function that receives a list of strings that are arithmetic problems and returns the problems arranged 	vertically and side-by-side. The function optionally takes a second argument. When the second argument 	is set to `True`, the answers are be displayed.

Time calculator:
	A function named `add_time` that takes in two required parameters and one optional parameter:
	- a start time in the 12-hour clock format (ending in AM or PM) 
	- a duration time that indicates the number of hours and minutes
	- (optional) a starting day of the week, case insensitive
	The function adds the duration time to the start time and returns the result.
	If the result are the next day, it shows `(next day)` after the time. If the result is more than one day later, it shows `(n days later)` after the time, where "n" is the number of days later.
	If the function is given the optional starting day of the week parameter, then the output displays the day of the week of the result. 

Budget app:
	- Created a `Category` class in `budget.py`. It instantiates objects based on different budget categories. When objects are created, they are passed in the name of the category. The class has an instance variable called `ledger` that is a list. When printed the class shows a neat overview of the ledger and the total.
	The class contains the following methods:
	deposit, withdraw, get_balance, transfer, check_funds
	- Created a function create_spend_chart, which takes a list of categories as an argument and returns a string that is a bar chart showing percentage spent per category.

Polygon area calculator:
	- Created a Rectangle class and a Square class, where the Square class is a subclass of Rectangle. Rectangle is initialised with `width` and `height` attributes, whereas Square takes only one attribute with is passed as both 	‘width’ and ‘height’.
	Both contain the following methods:
	set_width, set_height, get_area, get_perimeter, get_diagonal, get_picture, get_amount_inside

Probability calculator:
	Program to determine the approximate probability of drawing certain balls randomly from a hat. 
	- Created a `Hat` class, that takes a variable number of arguments that specify the number of balls of each color that are in the hat. This class contains a draw method with randomly draws balls from the hat and returns them as a list of strings.
	- Created an `experiment` function, which takes a hat object, the expected number and colours of balls, the number of balls drawn per experiment, and the number of experiments. It returns the probability of drawing (at least) the expected number and colours of balls for the number of experiments performed.

