print('\n\n')

import random
list=['attack','defence','heal','fatalkill']
class random_maker():
	def random_move(list):
		random_choice=random.choice(list)
		print('random choice in class :', random_choice)
		return random_choice
	def random_attack_health():
		rand_attack=random.randrange(20)
		print('rand attack in class',rand_attack)
		return rand_attack
	def random_heal_health():
		rand_heal=random.randrange(20)
#		print('heal in class:',rand_heal)
		return rand_heal
class Hero():
	
	def weapon(damage):
		print('Weapon', damage)				

	def health_damage(health):
		if health==0:
			print('\t\tYou are dead !!!\n \t\tMonster Wins!!!')
		else:
			print('Your health is : ', health)


class Monster():
	
	def weapon(damage):
		print('Weapon', damage)				

	def health_damage(health):
		if health==0:
			print('\t\tMonster is dead !!!\n \t\tYou Won!!!')
		else:
			print('Monster health is : ', health)


Player_health=20
Monster_health=20
flag1=True
flagm=True

Hero.health_damage(Player_health)
Monster.health_damage(Monster_health)

attack_health_cost=random_maker.random_attack_health()
print('attack health cost',attack_health_cost)


next_move=random_maker.random_move(list)
print(next_move)

Do_heal=input('Do you want o heal your player? \nPress Y for Yes \n N for No')
Do_heal=Do_heal.lower()

if Do_heal=='y' and flag1==True:
	healp=random_maker.random_heal_health()
	print('You healed :',healp, 'points')
	flag1=False
else:
	healp=0




Hero.weapon(attack_health_cost)




print('Monster side\n')

attack_health_cost_monster=random_maker.random_attack_health()
print('attack health cost monster',attack_health_cost_monster)

next_move_monster=random_maker.random_move(list)
print(next_move_monster)

if flagm==True:
	healm=random_maker.random_heal_health()
	print('Monster healed:',healm,' points')
	flagm=False

else:
	healm=0

Monster.weapon(attack_health_cost)



Player_health=Player_health-attack_health_cost_monster+healp
if Player_health > 20:
	Player_health=20

print('player health',Player_health)

#heal_monster=random_maker.random_heal_health()
#print('monster healed',heal_monster)


Monster_health=Monster_health-attack_health_cost+healm
if Monster_health > 20:
	Monster_health=20

print('Monster health',Monster_health)


print('\n\n')


'''


class Agent():
	name =''
	hot_drink=''
	def speak(self,speech):
		print(self.name+ ' says: " '+speech+' "')

	def drink(self):
		print(self.name+' drinks a cup of '+self.hot_drink+' .')

agent_q=Agent()

agent_q.name='Agent Q'
agent_q.speak('Hi, I am Agent Q!')
agent_q.hot_drink='Tea'
agent_q.drink()


agent_m=Agent()

agent_m.name='Agent M'
agent_m.speak("Hi, I am Agent M!How are you doing? ")
agent_m.hot_drink='Coffee'
agent_m.drink()

agent_n=Agent()

agent_n.name='Agent N'
agent_n.speak("Hi, I am Agent N! I am fine ! ")
agent_n.hot_drink='Latte'
agent_n.drink()

'''
