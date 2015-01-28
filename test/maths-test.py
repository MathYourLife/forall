
from forall.maths import Addition, Number, SingleDigit, make

a = Addition()
# a.args[0] += 3
# print(a[0])
# a[0] = a[1]
# print(a.args)

# b = SingleDigit(Number())
# for n in b:
#     print(n)

# for _ in range(1000):
#     print(b.random())

print(SingleDigit(Number()))
print(type(2))

a[0] = SingleDigit(Number()).random()
a[1] = SingleDigit(Number()).random()

print(a.expression())
print(a.equation())
