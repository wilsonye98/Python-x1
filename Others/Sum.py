def sum(str):
	arr = str.split(' ')
	total = 0
	for num in arr:
		total += int(num)
	return total

print(sum("5 6 3 6 4 4 5 6 6 5 3"))