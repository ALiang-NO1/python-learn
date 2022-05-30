string = 'global'
def outer():
    string = 'outer'
    def inner():
        # string = 'inner'
        print(string)
    inner()
outer()