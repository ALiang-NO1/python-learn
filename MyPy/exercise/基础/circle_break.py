prompt = "\nPlease enter the name of a city you have visited."
prompt += "Enter 'quit' to end the program:"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd like to go to "+city.title()+"!")
