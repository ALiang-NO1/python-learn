from audioop import avg
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)
record = ('guan', 'guan@toppr.net', '1506907XXXX', '18653154XXX')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)