#!/usr/bin/env python3
import operator

## Milk and Cookies: An Abstract Algebra
## ===========================================================================
##
## Our goal is to find an Algebra for:
##  ten * people * (milk + cookies) = two * people * meth
##
## Our numbers:
##  dead, people, milk, cookies, meth, two, ten
##
## Fortunately, 7 elements suggests that we can find an isomorphism to GF(7)
## and we won't have to deal with the polynomials of GF(p^k) extension fields
##
## Naturally, we'll assign "dead" <=> 0 as the additive inverse.
##
## We can also cancel "people" from the equation, yielding:
##  ten * (milk + cookies) = two * meth
##
## If we assign "two" and "ten" the naturaly way as 2 and 10 repectively,
## after modulus into the field GF(7), we get:
##   "two" <=> 2
##   "ten" <=> 3 (i.e. 3 = 10 mod 7)
##
## Solving for multiplicative-inverse of "ten", we have:
##   inv(ten) = inv(3) = 5  [since 3*5 = 15 == 1 (mod 7)]
##
## Solving for additive-inverse of "ten", we have:
##   neg(ten) = neg(3) = 4  [since 4 = -3 + 7 = -3 (mod 7)]
##
## Simplifying:
##   inv(ten) * ten * (milk + cookies) = inv(ten) * two * meth
##   milk + cookies = 5 * 2 * meth
##   milk + cookies = 10 * meth
##   milk + cookies = 3 * meth
##
##   Luckily 3 is an addivite group-generator for GF(7), so we possibly have all options available
##   for "meth", which makes perfect sense.
##
##   We need to now find a valid assignment given that we've already assigned these:
##     "dead" <=> 0
##     "two"  <=> 2
##     "ten"  <=> 3
##
##   The following are left: 1, 4, 5, 6
##
##   Assigning 6 to "meth" seems appropriate as it's some powerful stuff, alas that would require
##     milk + cookies = 4  [3 * 6 = 18 = 4 (mod 7)]
##
##   Unfortunately, we'd need 1 and 3 and we've alreayd assigned 3 to "ten"
##
##   Let's make a table of possibilities:
##
##     meth | 3 * meth |  milk   cookies
##       1  |     3    |    4       6
##       4  |     5    |    (not assignable with 1,5,6)
##       5  |     1    |    (not assignable with 1,4,6)
##       6  |     4    |    (not assignable with 1,4,5)
##
##   So, I guess meth is the multiplicative identity.
##
## Final assignment:
##   "dead"     <=>   0
##   "meth"     <=>   1
##   "two"      <=>   2
##   "ten"      <=>   3
##   "milk"     <=>   4
##   "people"   <=>   5
##   "cookies"  <=>   6
##
## Let's code a little calculator!

class Number:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        numbers[self.value] = self

    def __add__(self, other):
        return numbers[(self.value + other.value) % 7]


    def __mul__(self, other):
        return numbers[(self.value * other.value) % 7]

    def __str__(self):
        return self.name

numbers = [None for _ in range(7)]
dead    = Number("dead",    0)
meth    = Number("meth",    1)
two     = Number("two",     2)
ten     = Number("ten",     3)
milk    = Number("milk",    4)
people  = Number("people",  5)
cookies = Number("cookies", 6)

def operation_table(name, oper):
    hdr = '  %s     | ' % name + ''.join('%-10s' % num for num in numbers)

    print(hdr)
    print('-' * len(hdr))

    for m in numbers:
        print('%-7s | ' % m, end='')
        for n in numbers:
            print('%-10s' % oper(m, n), end='')
        print('')

def addition_table():  operation_table('+', operator.add)
def multiplication_table(): operation_table('*', operator.mul)

def interactive():
    print("===============================================================");
    print("Welcome to the milk and cookies calculator:");
    print("===============================================================");
    print("")
    print("Addition Table:")
    print("")
    addition_table()
    print("")
    print("Multiplication Table:")
    print("")
    multiplication_table()
    print("")
    print("")
    print("And now the most important question:");
    print("   ten * people * (milk + cookies) =?= two * people * meth");
    print("")
    print("Answer: %s" % (ten * people * (milk + cookies) == two * people * meth))
    print("");
    print("Enter any expression below to evaluate it:")

    while True:
        inp = input("> ")
        try:
            print(eval(inp))
        except Exception as ex:
            print(ex)
            continue

try:
    interactive()
except KeyboardInterrupt: pass
except EOFError: pass

print('')
