"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:int, the numbers that user input
	:return:int, the largest number of n
	"""
	if n < 0:
		n = -n
	if n < 10:
		return n
	elif n == 0:
		return n
	else:
		if (n//10) % 10 > n % 10:
			return int(find_largest_digit(n//10))
		else:
			return int(find_largest_digit(((n//100)*100+(n % 10)*10)/10))


if __name__ == '__main__':
	main()
