def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)



p1 = add_everything_up(123.456, 'строка')
p2 = add_everything_up('яблоко', 4215)
p3 = add_everything_up(123.456, 7)

print(p1)
print(p2)
print(p3)