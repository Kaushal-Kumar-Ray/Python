#We can perform concatenation to join two or more separate strings.
str4 = "Captain"
str5 = "America"
str6 = str4 + " " + str5
print(str6)

#We make the use of format() method. The format() methods places the arguments within the
# string wherever the placeholders are specified.
quantity = 2 
fruit = "Apples"
cost = 120.0
statement = "I want to buy {2} dozen {0} for {1}$"
print(statement.format(fruit,cost,quantity))