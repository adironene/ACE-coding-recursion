def count_part(n, m):
	 if n == 0:
		 return 1
	 elif n < 0:
		 return 0
	 elif m == 0:
		 return 0
	 else:
		 with_m = count_part(n - m, m)
		 wo_m = count_part(n, m - 1)
		 return with_m + wo_m


def main():
	num = count_part(3,2)
	print(num)

if __name__ == '__main__':main()
