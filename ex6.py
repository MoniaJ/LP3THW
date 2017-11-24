#I create a variable types_of_people
types_of_people = 10
#I create a variable x and I use variable types_of_people
#within it
x = f"There are {types_of_people} types of people."

#I create a variable binary
binary = "binary"
#I create a variable do_not
do_not = "don't"
#I create a variable y and use variables binary an do_not 
#within it
y = f"Those who know {binary} and those who {do_not}."

#I print variable x
print(x)
#I print variable y
print(y)

#I print a string including variable x
print(f"I said: {x}")
#I print a string including variable y
print(f"I also said: {y}")

#I create a variable hilarious
#hilarious = False
#I create a variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"

#I print joke_evaluation variable formated with 
hilarious variable
print(joke_evaluation.format(hilarious))

#I create a variable w
w = "This is the left side of..."
#I create a variable e
e = "a string with a right side."
#I print two string variables together
print(w + e)