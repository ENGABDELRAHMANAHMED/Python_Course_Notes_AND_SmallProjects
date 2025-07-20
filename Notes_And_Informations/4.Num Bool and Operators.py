##############
# Numbers
##############

#Integer

print(type(100))
print(type(-110))

#float

print(type(100.12354))
print(type(-110.5468))

#Complex

myComplexnumber = 5 + 6j 
print(type(myComplexnumber))
print("The real number is {}".format(int(myComplexnumber.real)))
print("The imaginary number is {}".format(int(myComplexnumber.imag)))

# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10+9j)
print(int((10+9j).real))
print(int((10+9j).imag))

#To get the random value

import random

print(random.randrange(0,10))  # Random integer between 0 and 10


##############
# Boolean
##############

# To Give True Value

print(bool("Osama"))
print(bool(100))
print(bool(100.95))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))
print(bool((1, 2, 3, 4, 5)))
print(bool({1, 2, 3, 4, 5}))
print(bool({"name": "Osama", "age": 38}))

# To Give False Value

print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(False))
print(bool(()))
print(bool({}))
print(bool(None))



####################
# Operators
####################

'''
Arithmetic Operators    => addition(+)           => x + y
                        => subtraction(-)        => x - y
                        => multiplication(*)     => x * y
                        => division(/)           => x / y    
                        => modulus(%)            => x % y
                        => exponentiation(**)    => x ** y
                        => floor division(//)    => x // y 

Assignment Operators    => assignment(=)                        => x = y          
                        => addition assignment(+=)              => x += y
                        => subtraction assignment(-=)           => x -= y
                        => multiplication assignment(*=)        => x *= y
                        => division assignment(/=)              => x /= y
                        => modulus assignment(%=)               => x %= y
                        => exponentiation assignment(**=)       => x **= y
                        => floor division assignment(//=)       => x //= y             
                        => bitwise AND assignment(&=)           => x &= y
                        => bitwise OR assignment(|=)            => x |= y
                        => bitwise XOR assignment(^=)           => x ^= y
                        => bitwise left shift assignment(<<=)   => x <<= y
                        => bitwise right shift assignment(>>=)  => x >>= y
                        => bitwise NOT assignment(~=)           => x ~= y
                        => walrus operator (:=)                 => x := y

Comparison Operators    => equal(==)                            => x == y 
                        => not equal(!=)                        => x != y
                        => greater than(>)                      => x > y
                        => less than(<)                         => x < y
                        => greater than or equal to(>=)         => x >= y
                        => less than or equal to(<=)            => x <= y

Logical Operators       => and                                  => x and y
                        => or                                   => x or y
                        => not                                  => not x    

Bitwise Operators       => bitwise AND(&)                       => x & y
                        => bitwise OR(|)                        => x | y
                        => bitwise XOR(^)                       => x ^ y
                        => bitwise NOT(~)                       => ~x
                        => bitwise left shift(<<)               => x << y
                        => bitwise right shift(>>)              => x >> y

Identity Operators      => is                                   => x is y
                        => is not                               => x is not y

Membership Operators    => in                                   => x in y
                        => not in                               => x not in y


                        
### Operator Precedence :-


             1. Parentheses ()             
             2. Exponentiation **
             3. Unary plus and minus and bitwise NOT ( +x , -x , ~x )
             4. Multiplication, division, floor division, and modulus (*, /, //, %)           
             5. Addition and subtraction (+, -)
             6. Bitwise shift operators (<<, >>)   
             7. Bitwise AND (&)
             8. Bitwise XOR (^)
             9. Bitwise OR (|)
             10. Comparison operators (==, !=, <, <=, >, >=)
             11. Identity operators (is, is not)
             12. Membership operators (in, not in)
             13. Logical operators (and, or, not)
             14. Assignment operators (=, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, <<=, >>=)
             15. Walrus operator (:=)


'''
