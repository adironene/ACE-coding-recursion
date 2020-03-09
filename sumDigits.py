def sum_digits(n):
		"""Calculates the sum of the digits n
		>>> sum_digits(8)
		8
		>>> sum_digits(18)
		9
		>>> sum_digits(2018)
		11
		"""
		if n < 10:
			return n
		else:
			all_but_last, last = n // 10, n % 10
			return sum_digits(all_but_last) + last

def main():
	num = sum_digits(3)
	print(num)

if __name__ == '__main__':main()

