# 5.3 fermats last theorem
def user_fermat():
	a = int(raw_input('first number: '))
	b = int(raw_input('second number: '))
	c = int(raw_input('third number: '))
	n = int(raw_input('raised to (make it greater than 2): '))
	check_fermat(a,b,c,n)

def check_fermat(a,b,c,n):
	if(n > 2 and a**n + b**n == c**n):
		print("Holy smokes, Fermat was wrong!")
	else:
		print("No that doesn't work")

# 5.4
def is_triangle(a, b, c):
        return not(a > b + c or b > a + c or c > a + b)

def prompt_user_for_triangle():
        first = int(raw_input('first side? '))
        second = int(raw_input('second side? '))
        third = int(raw_input('third side? '))
        return is_triangle(first, second, third)
