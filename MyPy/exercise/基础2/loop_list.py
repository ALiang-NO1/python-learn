unprinted_designs = ['iphone', 'robotpedant', 'dodecahodron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Print_model: " + current_design + ".")
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_models)
