print(type("Hello, world!"))
print(type(42))
print("Hello, world!")

print("--odd--")

def odd(n):
    print(n)
    return n % 2 !=0

print(odd(3))
print(odd(4))

print("--even--")
def even(n):
    print(n)
    return n % 2 == 0

print(even(3))
print(even(4))
