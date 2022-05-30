responses = {}
polling_active = True
while polling_active:
    name = input("What's your name?\n")
    response = input("Which mountain would you like to climb someday?\n")
    responses[name] = response
    repeat = input("Would you like me to let another person respond?(yes/no)\n")
    if repeat == 'no':
        polling_active = False
print("\n---poll Results---")
for name, response in responses.items():
    print(name+" would like to climb "+response+".")
