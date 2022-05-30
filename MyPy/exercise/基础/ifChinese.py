def fn(isChanese, family_name, name):
    if isChanese:
        print("Your name is {0} {1}.".format(family_name, name))
    else:
        print("Your name is {0} {1}.".format(name, family_name))
