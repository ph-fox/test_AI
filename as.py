import random, os, platform

directions = ['up','down','left','right']

def clean_console():
	if(platform.system() == 'Windows'):
		os.system('cls')
	else:
		os.system('clear')


def gen_path():
	clean_console()
	path_count = random.randint(1,4)
	current_path_list = []
	print("\n<========[Paths]=======>")
	for ways in range(path_count):
		path = random.choice(directions)
		if(path not in current_path_list):
			print(path)
			current_path_list.append(path)
		else:
			pass
	print(">========[Paths]=======<\n")
	return current_path_list


def out_path(paths):
	clean_console()
	print("\n<========[Paths]=======>")
	for path in paths:
		print(path)
	print(">========[Paths]=======<")

current_path_list = gen_path()
while True:
	#current_path_list = gen_path()
	select_path = input("Enter select path: ").lower()
	if(select_path in current_path_list):
		if(select_path == 'up'):
			print("\nGoing up!\n")
			current_path_list=gen_path()
		elif(select_path == 'down'):
			print("\nGoing down!\n")
			current_path_list=gen_path()
		elif(select_path == 'left'):
			print("\nGoing left!\n")
			current_path_list=gen_path()
		elif(select_path == 'right'):
			print("\nGoing right\n")
			current_path_list=gen_path()
	else:
		out_path(current_path_list)
		print('\n[-ERR-]:Selected path is not on the list!\n')

