def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total*k, k+1
    return total


def main():
	num = fact_iter(3)
	print(num)

if __name__ == '__main__':main()

