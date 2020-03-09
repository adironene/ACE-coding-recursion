def fact(n):
    """Calculates n!"""
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def main():
	num = fact(3)
	print(num)

if __name__ == '__main__':main()

