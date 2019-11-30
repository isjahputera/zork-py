import items

def Play_Zork():
	loop = 4
	print("---------------------------------------------------------")
	print("Welcome to Zork - The Unofficial Python Version.")

	while True:
		# First Input Loop
		while loop == 4:
			if loop == 4:
				print("---------------------------------------------------------")
				print("You are standing in an open field west of a white house, with a boarded front door.")
				print("You can see a small lake to the north.")
				print("(A secret path leads southwest into the forest.)")
				print("There is a Small Mailbox.")
				second = input("What do you do? ")

			if second.lower() == ("take mailbox"):
				print("---------------------------------------------------------")
				print("It is securely anchored.")
			elif second.lower() == ("open mailbox"):
				print("---------------------------------------------------------")
				print("Opening the small mailbox reveals a leaflet.")
			elif second.lower() == ("go north"):
				loop = 1
			elif second.lower() == ("open door"):
				print("---------------------------------------------------------")
				print("The door cannot be opened.")
			elif second.lower() == ("take boards"):
				print("---------------------------------------------------------")
				print("The boards are securely fastened.")
			elif second.lower() == ("look at house"):
				print("---------------------------------------------------------")
				print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
			elif second.lower() == ("go southwest"):
				loop = 8
			elif second.lower() == ("read leaflet"):
				print("---------------------------------------------------------")
				print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
			elif second.lower() == ("kick the bucket"):
				print("---------------------------------------------------------")
				print("You die.")
				print("---------------------------------------------------------")
				dead_inp = input("Do you want to continue? Y/N ")
				if dead_inp.lower() == ("n"):
					exit()
				if dead_inp.lower() == ("y"):
					Play_Zork()
			else:
				print("---------------------------------------------------------")

		# North of House
		while loop == 1:
			if loop == 1:
				print("---------------------------------------------------------")
				print("You find yourself at the edge of a beautiful lake aside rolling hills.")
				print("A small pier juts out into the lake.")
				print("A fishing rod rests on the pier.")
				print("(You can see a white house in the distance to the south.)")
				north_house_inp = input("What do you do? ")

			if north_house_inp.lower() == ("go south"):
				loop = 4
			elif north_house_inp.lower() == ("swim"):
				print("---------------------------------------------------------")
				print("You don't have a change of clothes and you aren't here on vacation.")
			elif north_house_inp.lower() == ("fish"):
				print("---------------------------------------------------------")
				print("You spend some time fishing but nothing seems to bite.")
			elif north_house_inp.lower() == ("kick the bucket"):
				print("---------------------------------------------------------")
				print("You die.")
				print("---------------------------------------------------------")
				dead_inp = input("Do you want to continue? Y/N ")
				if dead_inp.lower() == ("n"):
					exit()
				if dead_inp.lower() == ("y"):
					Play_Zork()
			else:
				print("---------------------------------------------------------")

		# Southwest Loop
		while loop == 8:
			if loop == 8:
				print("---------------------------------------------------------")
				print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
				forest_inp = input("What do you do? ")

			if forest_inp.lower() == ("go west"):
				print("---------------------------------------------------------")
				print("You would need a machete to go further west.")
			elif forest_inp.lower() == ("go north"):
				print("---------------------------------------------------------")
				print("The forest becomes impenetrable to the North.")
			elif forest_inp.lower() == ("go south"):
				print("---------------------------------------------------------")
				print("Storm-tossed trees block your way.")
			elif forest_inp.lower() == ("go east"):
				loop = 9
			elif forest_inp.lower() == ("kick the bucket"):
				print("---------------------------------------------------------")
				print("You die.")
				print("---------------------------------------------------------")
				dead_inp = input("Do you want to continue? Y/N ")
				if dead_inp.lower() == ("n"):
					exit()
				if dead_inp.lower() == ("y"):
					Play_Zork()
			else:
				print("---------------------------------------------------------")
		

		# East Loop and Grating Input
		while loop == 9:
			if loop == 9:
				print("---------------------------------------------------------")
				print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
				print("There is an open grating, descending into darkness.")
				grating_inp = input("What do you do? ")

			if grating_inp.lower() == ("go south"):
				print("---------------------------------------------------------")
				print("You see a large ogre and turn around.")
			elif grating_inp.lower() == ("descend grating"):
				loop = 10
			elif grating_inp.lower() == ("kick the bucket"):
				print("---------------------------------------------------------")
				print("You die.")
				print("---------------------------------------------------------")
				dead_inp = input("Do you want to continue? Y/N ")
				if dead_inp.lower() == ("n"):
					exit()
				if dead_inp.lower() == ("y"):
					Play_Zork()
			else:
				print("---------------------------------------------------------")	


		# Grating Loop and Cave Input
		while loop == 10:
			if loop == 10:
				print("---------------------------------------------------------")
				print("You are in a tiny cave with a dark, forbidding staircase leading down.")
				print("There is a skeleton of a human male in one corner.")
				cave_inp = input("What do you do? ")

			if cave_inp.lower() == ("descend staircase"):
				loop = 11
			elif cave_inp.lower() == ("take skeleton"):
				print("---------------------------------------------------------")
				print("Why would you do that? Are you some sort of sicko?")
			elif cave_inp.lower() == ("smash skeleton"):
				print("---------------------------------------------------------")
				print("Sick person. Have some respect mate.")
			elif cave_inp.lower() == ("light up room"):
				print("---------------------------------------------------------")
				print("You would need a torch or lamp to do that.")
			elif cave_inp.lower() == ("break skeleton"):
				print("---------------------------------------------------------")
				print("I have two questions: Why and With What?")
			elif cave_inp.lower() == ("go down staircase"):
				loop = 11
			elif cave_inp.lower() == ("scale staircase"):
				loop = 11
			elif cave_inp.lower() == ("kick the bucket"):
				print("---------------------------------------------------------")
				print("You die.")
				print("---------------------------------------------------------")
				dead_inp = input("Do you want to continue? Y/N ")
				if dead_inp.lower() == ("n"):
					exit()
				if dead_inp.lower() == ("y"):
					Play_Zork()
			elif cave_inp.lower() == ("scale staircase"):
				loop = 11
			else:
				print("---------------------------------------------------------")


		# End of game
		while loop == 11:
			if loop == 11:
				print("---------------------------------------------------------")
				print("You have entered a mud-floored room.")
				print("Lying half buried in the mud is an old trunk, bulging with jewels.")
				last_inp = input("What do you do? ")

			if last_inp.lower() == ("open trunk"):
				print("---------------------------------------------------------")
				print("You have found the Jade Statue and have completed your quest!")
			elif last.inp.lower() == ("kick the bucket"):
				print("---------------------------------------------------------")
				print("You die.")
				print("---------------------------------------------------------")
				dead_inp = input("Do you want to continue? Y/N ")
				if dead_inp.lower() == ("n"):
					exit()
				if dead_inp.lower() == ("y"):
					Play_Zork()
			else:
				print("---------------------------------------------------------")
			
			# Exit loop at the end of game
			exit_inp = input("Do you want to continue? Y/N ")
			if exit_inp.lower() == ("n"):
				exit()
			if exit_inp.lower() == ("y"):
				Play_Zork()

def Play_Zork_Refactored():
	loop = 0
	user_is_alive = True
	while True:
		if loop == 0:
			loop = 4
			print("---------------------------------------------------------")
			print("Welcome to Zork - The Unofficial Python Version.")
			if not user_is_alive:
				print("Dead user has been resurrected! :)")
				user_is_alive = True
		if loop == 4:
			loop, user_is_alive = south()

		elif loop == 1:
			loop, user_is_alive = north()

		elif loop == 8:
			loop, user_is_alive = southwest()

		elif loop == 9:
			loop, user_is_alive = east()

		elif loop == 10:
			loop, user_is_alive = cave()

		elif loop == 11:
			loop, user_is_alive = treasure()

		elif loop == -1:
			break

		if user_is_alive:
			print("User is alive and well. :)")
		else:
			print("User has kicked the bucket. :(")

	exit()

def south():
	# First Input Loop
	return_value = 0
	user_is_alive = True
	mailbox_is_open = False
	while True:
		print("---------------------------------------------------------")
		print("You are standing in an open field west of a white house, with a boarded front door.")
		print("You can see a small lake to the north.")
		print("(A secret path leads southwest into the forest.)")
		print("There is a Small Mailbox.")
		second = input("What do you do? ")

		if second.lower() == ("take mailbox"):
			print("---------------------------------------------------------")
			print("It is securely anchored.")
		elif second.lower() == ("open mailbox"):
			print("---------------------------------------------------------")
			print("Opening the small mailbox reveals a leaflet.")
			mailbox_is_open = True
		elif second.lower() == ("go north"):
			return_value = 1
			break
		elif second.lower() == ("open door"):
			print("---------------------------------------------------------")
			print("The door cannot be opened.")
		elif second.lower() == ("take boards"):
			print("---------------------------------------------------------")
			print("The boards are securely fastened.")
		elif second.lower() == ("look at house"):
			print("---------------------------------------------------------")
			print(
				"The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
		elif second.lower() == ("go southwest"):
			return_value = 8
			break
		elif second.lower() == ("read leaflet"):
			print("---------------------------------------------------------")
			if mailbox_is_open:
				print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
			else:
				print("You have to open the mailbox first before you can read the leaflet inside the mailbox.")
		elif second.lower() == ("kick the bucket"):
			print("---------------------------------------------------------")
			print("You die.")
			user_is_alive = False
			print("---------------------------------------------------------")
			dead_inp = input("Do you want to continue? Y/N ")
			if dead_inp.lower() == ("n"):
				return_value = -1
			if dead_inp.lower() == ("y"):
				return_value = 0
			break
		else:
			print("---------------------------------------------------------")
	return return_value, user_is_alive

def north():
	# North of House
	return_value = 0
	user_is_alive = True
	while True:
		print("---------------------------------------------------------")
		print("You find yourself at the edge of a beautiful lake aside rolling hills.")
		print("A small pier juts out into the lake.")
		print("A fishing rod rests on the pier.")
		print("(You can see a white house in the distance to the south.)")
		north_house_inp = input("What do you do? ")

		if north_house_inp.lower() == ("go south"):
			return_value = 4
			break
		elif north_house_inp.lower() == ("swim"):
			print("---------------------------------------------------------")
			print("You don't have a change of clothes and you aren't here on vacation.")
		elif north_house_inp.lower() == ("fish"):
			print("---------------------------------------------------------")
			print("You spend some time fishing but nothing seems to bite.")
		elif north_house_inp.lower() == ("kick the bucket"):
			print("---------------------------------------------------------")
			print("You die.")
			user_is_alive = False
			print("---------------------------------------------------------")
			dead_inp = input("Do you want to continue? Y/N ")
			if dead_inp.lower() == ("n"):
				return_value = -1
			if dead_inp.lower() == ("y"):
				return_value = 0
			break
		else:
			print("---------------------------------------------------------")
	return return_value, user_is_alive

def southwest():
	return_value = 0
	user_is_alive = True
	while True:
		print("---------------------------------------------------------")
		print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
		forest_inp = input("What do you do? ")

		if forest_inp.lower() == ("go west"):
			print("---------------------------------------------------------")
			print("You would need a machete to go further west.")
		elif forest_inp.lower() == ("go north"):
			print("---------------------------------------------------------")
			print("The forest becomes impenetrable to the North.")
		elif forest_inp.lower() == ("go south"):
			print("---------------------------------------------------------")
			print("Storm-tossed trees block your way.")
		elif forest_inp.lower() == ("go east"):
			return_value = 9
			break
		elif forest_inp.lower() == ("kick the bucket"):
			print("---------------------------------------------------------")
			print("You die.")
			user_is_alive = False
			print("---------------------------------------------------------")
			dead_inp = input("Do you want to continue? Y/N ")
			if dead_inp.lower() == ("n"):
				return_value = -1
			if dead_inp.lower() == ("y"):
				return_value = 0
			break
		else:
			print("---------------------------------------------------------")
	return return_value, user_is_alive

def east():
	# East Loop and Grating Input
	return_value = 0
	user_is_alive = True
	while True:
		print("---------------------------------------------------------")
		print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
		print("There is an open grating, descending into darkness.")
		grating_inp = input("What do you do? ")

		if grating_inp.lower() == ("go south"):
			print("---------------------------------------------------------")
			print("You see a large ogre and turn around.")
		elif grating_inp.lower() == ("descend grating"):
			return_value = 10
			break
		elif grating_inp.lower() == ("kick the bucket"):
			print("---------------------------------------------------------")
			print("You die.")
			user_is_alive = False
			print("---------------------------------------------------------")
			dead_inp = input("Do you want to continue? Y/N ")
			if dead_inp.lower() == ("n"):
				return_value = -1
			if dead_inp.lower() == ("y"):
				return_value = 0
			break
		else:
			print("---------------------------------------------------------")
	return return_value, user_is_alive

def cave():
	# Grating Loop and Cave Input
	return_value = 0
	user_is_alive = True
	while True:
		print("---------------------------------------------------------")
		print("You are in a tiny cave with a dark, forbidding staircase leading down and another staircase going up.")
		print("There is a skeleton of a human male in one corner.")
		cave_inp = input("What do you do? ")

		if cave_inp.lower() in ["descend staircase", "go down staircase", "scale staircase"]:
			return_value = 11
			break
		elif cave_inp.lower() in ["ascend staircase", "go up staircase", "climb staircase"]:
			print("---------------------------------------------------------")
			print("OMG. You have unfortunately climbed up into a dark space where a Grue lives.")
			print("The Grue has eaten you alive!")
			user_is_alive = False
			dead_inp = input("Do you want to continue? Y/N ")
			if dead_inp.lower() == ("n"):
				return_value = -1
			if dead_inp.lower() == ("y"):
				return_value = 0
			break
		elif cave_inp.lower() == ("take skeleton"):
			print("---------------------------------------------------------")
			print("Why would you do that? Are you some sort of sicko?")
		elif cave_inp.lower() == ("smash skeleton"):
			print("---------------------------------------------------------")
			print("Sick person. Have some respect mate.")
		elif cave_inp.lower() == ("light up room"):
			print("---------------------------------------------------------")
			print("You would need a torch or lamp to do that.")
		elif cave_inp.lower() == ("break skeleton"):
			print("---------------------------------------------------------")
			print("I have two questions: Why and With What?")
		elif cave_inp.lower() == ("kick the bucket"):
			print("---------------------------------------------------------")
			print("You die.")
			user_is_alive = False
			print("---------------------------------------------------------")
			dead_inp = input("Do you want to continue? Y/N ")
			if dead_inp.lower() == ("n"):
				return_value = -1
			if dead_inp.lower() == ("y"):
				return_value = 0
			break
		else:
			print("---------------------------------------------------------")

	return return_value, user_is_alive

def treasure():
	# End of game
	return_value = 0
	user_is_alive = True
	while True:
		print("---------------------------------------------------------")
		print("You have entered a mud-floored room.")
		print("Lying half buried in the mud is an old trunk, bulging with jewels.")
		last_inp = input("What do you do? ")

		if last_inp.lower() == ("open trunk"):
			print("---------------------------------------------------------")
			print("You have found the Jade Statue and have completed your quest!")
			break
		elif last_inp.lower() == ("kick the bucket"):
			print("---------------------------------------------------------")
			print("You die.")
			user_is_alive = False
			print("---------------------------------------------------------")
			dead_inp = input("Do you want to continue? Y/N ")
			if dead_inp.lower() == ("n"):
				return_value = -1
			if dead_inp.lower() == ("y"):
				return_value = 0
			break
		else:
			print("---------------------------------------------------------")

	# Exit loop at the end of game
	exit_inp = input("Do you want to continue? Y/N ")
	if exit_inp.lower() == ("n"):
		return_value = -1
	if exit_inp.lower() == ("y"):
		return_value = 0

	return return_value, user_is_alive
