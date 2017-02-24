def raw_to_power(somelist):
	powers = []
	sentence = ""
	j = 0
	for i in sorted(set(somelist)):
		powers.append(somelist.count(i))
	while j < len(powers):
		sentence += "%d^%d "%(sorted(list(set(somelist)))[j],powers[j])
		j += 1
	return sentence




def prime_factor(num):
	some = []
	i = 2
	while i in range(2,num+1):
		if num % i == 0:
			some.append(i)
			num = num//i
		elif num == 1:
			break
		else:
			i += 1

	return raw_to_power(some)




while True:
	number = int(input("Type a number to see prime factors of it(0 to quit): "))
	if number == 0:
		break
	else:
		print(prime_factor(number))