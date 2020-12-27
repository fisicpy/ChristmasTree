from colorama import init, Back, Fore
import random, time
colors = ["red", "yellow", "magenta", "white"]
init()
tree = [[" ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " "],
		[" ", " ", " ", " ", " ", " ", " ", "#", "*", "#", " ", " ", " ", " ", " ", " ", " "],
		[" ", " ", " ", " ", " ", " ", "#", "#", "#", "#", "#", " ", " ", " ", " ", " ", " "],
		[" ", " ", " ", " ", " ", "#", "*", "#", "#", "#", "#", "#", " ", " ", " ", " ", " "],
		[" ", " ", " ", " ", "#", "#", "#", "#", "#", "*", "#", "#", "#", " ", " ", " ", " "],
		[" ", " ", " ", "#", "#", "*", "#", "#", "#", "#", "#", "#", "*", "#", " ", " ", " "],
		[" ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "],
		[" ", "#", "#", "*", "#", "#", "#", "#", "#", "#", "*", "#", "#", "#", "#", "#", " "],
		["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "*", "#", "#", "#"],
		[" ", " ", " ", " ", " ", " ", " ", " ", "█", " ", " ", " ", " ", " ", " ", " ", " "]]
foliage = []
while True:
	print("\033[H\033[J" + Back.BLACK, Fore.WHITE)
	for i in tree:
		for j in i:
			if j == "█":
				foliage.append(f"{Fore.RED}█")
			elif j == "#":
				foliage.append(f"{Fore.GREEN}█")
			elif j == "*":			
				color = random.choice(colors)
				if color == "red":
					foliage.append(f"{Fore.RED}█")	
				elif color == "yellow":
					foliage.append(f"{Fore.YELLOW}█")
				elif color == "magenta":
					foliage.append(f"{Fore.MAGENTA}█")
				elif color == "white":
					foliage.append(f"{Fore.WHITE}█")
			else:
				foliage.append(j)
		print("".join(foliage))
		foliage = []
	time.sleep(0.4)
