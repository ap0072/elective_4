# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.



def nth_happy_number(n):
	l=[]
	num=0
	while((len(l))<n):
		if	(is_happy(num))==True:
			l.append(num)
		num=num+1
	return	l[-1]

def pdi_function(number, base: int = 10):
    """Perfect digital invariant function."""
    total = 0
    while number > 0:
        total += pow(number % base, 2)
        number = number // base
    return total

def is_happy(number: int) -> bool:
    """Determine if the specified number is a happy number."""
    seen_numbers = set()
    while number > 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = pdi_function(number)
    return number == 1

assert(nth_happy_number(1) == 1)
assert(nth_happy_number(2) == 7)
assert(nth_happy_number(3) == 10)
assert(nth_happy_number(4) == 13)
assert(nth_happy_number(5) == 19)
assert(nth_happy_number(6) == 23)
assert(nth_happy_number(7) == 28)
assert(nth_happy_number(8) == 31)
print("All	test	cases	passed!")
