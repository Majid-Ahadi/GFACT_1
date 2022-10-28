print('\n\n')
	print('\n\n')


'''


#rock paper sissors

for flag in range(100):	


# import random
	import random
 
# prints a random value from the list
	list = ['rock', 'paper', 'sissors']

	def pick_random(list):
		return random.choice(list)


	cpu_move=pick_random(list)
#print(cpu_move)

	def user_move(user_move):

		user_move=input(' If you want to exit press x !! \n Do you like to play Rock, Paper, Sissors ???\nThen enter your choice :  ')

		user_move=user_move.lower()
#	print(user_move)
		return user_move

	def winner(user_move,cpu_move):
#	print('you are in winner')
#	print(user_move,cpu_move)

		if (user_move==cpu_move):
			print('\nEqual')


		elif (user_move=='sissors' and cpu_move=='rock') or  (user_move=='rock' and cpu_move=='paper') or (user_move=='paper' and cpu_move=='sissors') :
			print( '\nCPU Wins!!!!')


		else:
			print('\nYou Won !!!!')



	user_move=user_move(user_move)



	if user_move=='rock' or  user_move=='paper' or  user_move=='sissors':
		print('you are in')

		x=winner(user_move,cpu_move)
	elif user_move=='x':
		flag=False
		exit(-1)
	else:

		print('Wrong move !!!\n Type Again !!\n')

# prints a random item from the string
#string = "striver"
#print(random.choice(string))



--------------------------
import sys

arguments= sys.argv

print(arguments)


import random
import sys

def pick_random(list):
	return random.choice(list)


def get_code(list, num_words):
	#num_words='1'
	if num_words.isdigit() == False:
		return 'Error incorect argument provided'



	num_words= int(num_words)
	code_name=''

	for x in range(1,num_words+1):
		word= pick_random(list)
		code_name+=word+' ' 


	return code_name.rstrip()


word_list=['Aura','avalanch','ilya','majid','niloo','rosa','parsa', 'ali','somy']


word_to_pick= sys.argv[0]

code_name=get_code(word_list,word_to_pick)

print(code_name)


---------------------------
username = input('Hello, what is your name? ')

print('Hi,'+ username +'. Nice to meet you!')

user_coffee=int(input('Hello, How many coffee do you want ?'))

if user_coffee <=2:
	print('you will have : ', user_coffee, 'Coffee')
else:
	print('are you sure you want : ', user_coffee,'???')

'''
