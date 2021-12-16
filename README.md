# 326_Final
Final Project for INST326

Documentation (please name your file README.md or README.pdf), including
An explanation of the purpose of each file in your repository
Clear instructions on how to run your program from the command line
Clear instructions on how to use your program and/or interpret the output of the program, as applicable
Attribution: in order to evaluate whether each member has made a substantial, original contribution to the project, please clearly and unambiguously indicate who is the primary author of each major function/method. You do not need to attribute minor program components, such as an if __name__ == "__main__": statement.
An annotated bibliography of all sources you used to develop your project. For each source, explain how you used the source.

currency_converter.py: 
This file is the primary code file, it contains all of the classes and methods that makes our code run. It is a simulation of a premier travel/flight membership program that allows members to travel anywhere for 200 dollars from Dunder airport. It calculates thier balance on their prepaid travel card for how much they have left in the currency of the place they are visiting for their trip so that they can make purchases. To view the API used to get live exchange rates, you can use the URL: http://data.fixer.io/api/latest?access_key=a702f302693756a5c8c44b988f472fc6

people.txt: 
This is a text file that contains the data on each of our example members including the type of membership, their balance, and their intended destination country's currency. 

To run our code from the command line, simply type in python3 currency_converter.py people.txt "_Name of person in people.txt file_"

The interpretation of our program is pretty simple, it outlines the person, their destination in terms of its currency, their beginning balance, and how much they have left both in USD, and the currency of the country they are visiting.

Snigdha: 
I took charge of the currency conversion aspect of the program. I created the converter method, and integrated it into the __init__ method of the Currency_Shop class. I also helped to create the main function and integrated the currency conversion into the output of the program. The source code used in the converter method of the Currency_Shop class is derived from https://www.geeksforgeeks.org/currency-converter-in-python/ which creates class and uses input from the user to provide output. In our program's case, we did not need to take input on where the user would want to convert to, or what currency they are converting from, since all of the members are from the US, so I eliminated an input as well as an extra argument in the converter method. 

Abby: 
I worked mainly on the Person class aspect of the project. First, I did the membership_list function which gives a discount to the customer depending on their membership status. Next, I did the buy_ticket method which calculates the new price of the customer's plane ticket, also dependant on their membership status. I also added a __repr__ magic method to return the Person object representation in string format.

Zoey: 
I worked on the __init__ methods in both the Person class and the Currency_Shop class, which assigns attributes and in the Currency_Shop class it reads a txt file, as well as the get_person method in the Currency_Shop, which instantiates a person. I also added the parse_args method and if __name__ == "__main__" method.

Citations: 
 Currency converter in python. GeeksforGeeks. (2019, December 12). Retrieved November 15, 2021, from https://www.geeksforgeeks.org/currency-converter-in-python/. 
