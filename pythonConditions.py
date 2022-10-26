
print('\n\n')


print('\n\n')


'''



counter=1

while counter<=3:
	print(counter)
	counter+=1

print('Loop complete')


active=True
countdown=3

while active==True:
	if countdown==0:
		countdown= 'Go!'
		active=False
	else:
		print(countdown)
		countdown-=1

print(countdown)

counter=3

while counter>=0:
	print(counter)
	counter-=1

invited=['Agent1','Agent2','Agent3', 'Agent4']

while 'Agent3' in invited:
	invited.remove('Agent3')
	print(invited)

invited.append('Agent3')
print(invited)


attended=[]
while invited:
	current_agent=invited.pop()
	print(current_agent+ 'attended the meeting.')
	attended.append(current_agent)

print('Attended list : ' + str(attended))



------------------------------------
agent_m = {
		'name':'m',
		'distro':'Ubuntu',
		'drink':'Lemonade'
	}

agent_n = {
		'name':'n',
		'distro':'Mint',
		'drink':'Tea'
	}

agent_o = {
		'name':'o',
		'distro':'Fedora',
		'drink':'Coffee'
	}

agent_p = {
		'name':'p',
		'distro':'Arch',
		'drink':'Wiskey'
	}


agents=[agent_m,agent_n,agent_o,agent_p]

for agent in agents:
	for key, value in agent.items():
		print(key.title()+ ' : ' + value)
	print('\n')



--------------------------------
fav_linux_distros=['Mint', 'Debian', 'ubuntu', 'Fedora', 'Arch']

print(fav_linux_distros,'\n')

print(fav_linux_distros[0],'\n')

print(fav_linux_distros[1],'\n')

for distro in  fav_linux_distros:
	print(distro)

	print('This is a funny situation : ',distro,'\n')
	
	print('here is another line','\n')

print('finished!!!!!!')

for counter in range(1,6):
	print(counter)
print('Finish Counter!!')

total=10
sub_total=3
x=total-sub_total

for i in range(0,x+1):
	print(i,'Hello','\n')
for j in range(0,x):
	print(j,'bye','\n')

fav_distro={
	'q':'Mint',
	'j':'Kali',
	'm':'Ubuntu',
	's':'Elementry'
	}

for agent, distro in fav_distro.items():
	print('Agent ' + agent.upper() + ' : ' +distro,'\n')

print(fav_distro)


-----------------------------------
coffee_available= False
drink_available='coffee'
coffee_needed=4
coffee_count='4'
drink_list=['coffee','Tea','Lemonade']

if coffee_available==True :
	print("Agent Majid will have Coffee ! ",'\n')


if drink_available.upper()=='coffee' :
	print("Agent Majid will have 2 Coffees ! ",'\n')


if coffee_needed==4 :
	print("Agent Majid will have 4 Coffees ! ",'\n')


if coffee_needed>=int(coffee_count) :
	print("Agent Majid will have 8 Coffees ! ",'\n')

if 'coffee' in drink_list :
	print('coffee is in the list','\n')

if 'orange' not in drink_list:
	print('There is no Orange juice in the list','\n')

print('This is between Lines','\n\n')

#coffee_available=False

if coffee_available==False:
	if 'Tea' in drink_list:
		print('In na Kooft Bokhor','\n')


if coffee_available==True and 'Tea' in drink_list:
		print('Kooft Nakhor, Tea Bokhor !','\n')
elif coffee_available == True :
		print('here is Lemonade !','\n')
else:

		print('Kooft Bokhor!','\n')

print('bye agent M')







'''
