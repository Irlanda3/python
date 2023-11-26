Activity: Use Python syntax
Introduction
In this lab, you will practice Python syntax by creating variables, checking the data types of variables, creating precise variable names, and completing data conversions.

For this activity, imagine you're a data professional analyzing the users that log in to purchase tickets at a movie theater. You'll save the theater's unique identification code to a variable, study the number of tickets sold, and the data types you'll be working with.

Throughout this lab, you will practice assigning variables, viewing the values saved to the variables, and checking their data types.

Tips for completing this lab
As you navigate this lab, keep the following tips in mind:

### YOUR CODE HERE ### indicates where you should write code. Be sure to replace this with your own code before running the code cell.
Feel free to open the hints for additional guidance as you work on each task.
To enter your answer to a question, double-click the markdown cell to edit. Be sure to replace the "[Double-click to enter your responses here.]" with your own answer.
You can save your work manually by clicking File and then Save in the menu bar at the top of the notebook.
You can download your work locally by clicking File and then Download and then specifying your preferred file format in the menu bar at the top of the notebook.
Task 1: Assign the theater ID to a variable
In your work as an analyst, imagine you are considering sales at a specific theater and you want to save the theater's unique identification, which is "b79cn10k", to a variable. By doing this, you'll be able to access the ID easily if you need it later. In the following code cell:

Assign the theater's unique identification to a variable named theater_id.

Display the contents of the theater_id variable.

Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.

# 1.
​
​
theater_id = "b79cn10k"
# 2.
​
​
print(theater_id)
​
b79cn10k
Hint 1
Hint 2
Hint 3
Task 2: Create a ticket type variable
As you continue your work, you're provided a list of the different types of tickets sold by the theater: "Senior", "Adult", and "Youth". In this task, focus on the "Adult" ticket type.

Create a variable called ticket_type and assign it a value of "Adult".
Display the contents of the ticket_type variable.
# 1.
ticket_type = "Adult"
​
​
# 2.
print(ticket_type)
​
Adult
Hint 1
Hint 2
Hint 3
Task 3: Save the number of adult tickets to a variable and check the data type
Now that you've recorded the types of tickets being sold, it's time to record the number of adult tickets sold so far.

Create a variable called adult_tickets_sold that represents the current number of "adult" tickets sold and assign it a value of 59.0.

Check the data type of adult_tickets_sold.

# 1.
adult_tickets_sold = 59.0
​
​
# 2.
print(adult_tickets_sold)
​
59.0
Hint 1
Hint 2
Hint 3
Task 4: Convert data types and print the result
The data you work with as a data professional often needs to be converted to different data types. In this case, the number of tickets sold should be recorded as integers and not floats.

Convert the data saved in the adult_tickets_sold variable from a float to an integer. Reassign the result back to the adult_tickets_sold variable.

Check the data type of adult_tickets_sold.

# 1.
adult_tickets_sold = int(adult_tickets_sold)
print(type(adult_tickets_sold))
​
# 2.
adult_tickets_sold = float(adult_tickets_sold)
print(type(adult_tickets_sold))
​
<class 'int'>
<class 'float'>
Hint 1
Hint 2
Hint 3
Conclusion
What are your key takeaways from this lab?

There are many useful operators in Python that help you work with variables.
The = assignment operator allows you to assign or reassign a specific value to a variable.
The print() function in Python allows you to display information.
It can take in a value directly or a variable that stores a value.
The type() function in Python helps you to determine the data type of an object.
If you pass in a variable to type(), it will output the data type of the value stored in the variable.
Python is able to convert some data types from one to another.
Using the int() function on a variable that stores data as a float will convert the data from a floating point number to an integer.
Congratulations! You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
