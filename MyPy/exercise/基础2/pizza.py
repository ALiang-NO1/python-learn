def make_pizza(size, *toppings):
	"""概述要做的比萨饼"""
	print("make a "+str(size)+"inches pizza with the following toppings:")
	for topping in toppings:
		print("-"+topping)
