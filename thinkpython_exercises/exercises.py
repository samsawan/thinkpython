# go through the exercises in this book, it's quite good

# 3.3
def right_justify(s):
	print(s.rjust(70 - len(s)))

# 3.4
def do_four(func, val):
	for i in range(4):
		func(val)

# 5.4
def is_triangle(a, b, c):
	return not(a > b + c or b > a + c or c > a + b)

def prompt_user_for_triangle():
	first = int(raw_input('first side? '))
	second = int(raw_input('second side? '))
	third = int(raw_input('third side? '))
	return is_triangle(first, second, third)

# 6.5
def ack_function(a, b):
	if a == 0:
		return b + 1
	elif a > 0 and b == 0:
		return ack_function(a - 1, 1)
	else:
		return ack_function(a - 1, ack_function(a, b - 1))

# 6.7. -> this is wrong!!! 
def is_power(a, b):
	if a == b:
		return True
	else:
		return divisible(a, b) and is_power(b, b / a)

def divisible(first, second):
	print first, second
	return first % second == 0