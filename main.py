import os

def fibonacci(num):
	if num < 0:
		print("Incorrect input")
		return None
	elif num == 0:
		return 0
	elif num < 3:
		return 1
	else:
		return fibonacci(num-1) + fibonacci(num-2)

def factorial(num):
	if num < 0:
		return None
	elif num < 2:
		return 1
	else:
		return num * factorial(num-1)

def main():
	num = int(os.environ['NUM'])
	print(f"{num}! = {factorial(num)}")
	print(f"n-th Fibonacci number is {fibonacci(num)}")

if __name__ == '__main__':
	main()