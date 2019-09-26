n = input()
cards = []
for i in range(int(n)):
	cards.append(input().split())

for i in ['S', 'H', 'C', 'D']:
	for j in range(1, 14):
		if [i, str(j)] not in cards:
			print(i, j)
