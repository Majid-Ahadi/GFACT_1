
print('\n\n')

#list
case_stats=[21,12,8]

print('Total cases : '+str(case_stats[0]),'\n')

print('Solved cases : '+str(case_stats[1]),'\n')

print('Unsolved cases : '+str(case_stats[2]),'\n')

#Dictionary

case_stats={'Total': 21,'Solved':{'June':13,'july': 18},'Unsolved' : 8}

print('Case Stats : ',case_stats,'\n','Total : ', str(case_stats['Total']),
'\n','Dictionary Solved jun : ',str(case_stats['Solved']['June']),'\n',
'Dictionary Solved july ((case_stats[Solved][july]) : ',
str(case_stats['Solved']['july']),'\n')

#modify Dic


case_stats={'Total': 21,'Solved':{'June':13,'july': 18},'Unsolved' : 8}

print(case_stats,'\n\n')

case_stats['Total']=12

print('Temp Total',case_stats['Total'],'\n\n')

case_stats['Solved']['June']=1356

case_stats['Total']=case_stats['Total']+1

case_stats['Total']+=1

print('Case Stats : ',case_stats,'\n','Total : ', str(case_stats['Total']),
'\n','Dictionary Solved jun : ',str(case_stats['Solved']['June']),'\n',
'Dictionary Solved july ((case_stats[Solved][july]) : ',
str(case_stats['Solved']['july']),'\n')

del case_stats['Solved']

print(case_stats,'\n')

print('\n\n')

'''

----------------------------
misc=['purple',99,3.14,False,['apple','orange','pear']]

print('misc: ',misc,'\n')

print('0: ',misc[0],'\n','1: ',misc[1],'\n','2: ',misc[2],'\n','3: ',
misc[3],'\n','4: ',misc[4],'\n','4-0: ',misc[4][0],'\n','4-1: ',misc[4][1])

misc[0]='Changed misc'
print('changed : ', '\n\n\n',misc)

fave_linux_distros=['Mint', 'Debian', 'Ubuntu' , 'Manjaro' , 'Fedora' ,
 'Arch']

print('\n\nNot sorted : ',fave_linux_distros,'\n\n')
fave_linux_distros.sort()

print('sorted : ',fave_linux_distros)

fave_linux_distros.reverse()

print('reversed : ',fave_linux_distros)

fave_linux_distros.append('Linux Core')

print('\n\nappended : ',fave_linux_distros)

fave_linux_distros.insert(0,'Ubuntu Server')

print('\n\ninserted : ',fave_linux_distros)

visited=fave_linux_distros.pop()
print('\n\n','Visited: ',visited)


visited=fave_linux_distros.pop(1)
print('\n\n','Visited pop 1 : ',visited)

fave_linux_distros.remove('Mint')

print('\n\n',fave_linux_distros)





-----------------------------
fave_linux_distros=['Mint', 'Debian', 'Ubuntu' , 'Manjaro' , 'Fedora' ,
 'Arch']

print (fave_linux_distros,'\n') 

print (fave_linux_distros[0],'\n')

print (fave_linux_distros[1],'\n')

print (fave_linux_distros[2],'\n\n\n')

#print (fave_linux_distros[7],'\n')

print ("-1",fave_linux_distros[-1],'\n')

print ("-2",fave_linux_distros[-2],'\n\n\n\n')

top_fave_distro=fave_linux_distros[0]

print("Majid`s favorit distro is : ", top_fave_distro.upper(),"!\n\n")

print(len(fave_linux_distros),'\n\n')

--------------------------------
pocket_money='5'
coffee_price= '3.50'

totalint= int(pocket_money)+ float(coffee_price)


--------------------
flag= None
flagisthere=bool(flag)
print('\n',"Total int : ",totalint,'\n',"flag : ",flagisthere,'\n')

--------------
solved_cases=14
print ("Majid has cloased "  + format(solved_cases) + " cases this week!")

---------------------
Multi=888888*77
Devide=9999/2
Round=round(42.123456,3)
Minus=1.99-3000188
Minus2=55-1088
charchange="1"*77
charascii=str(3)
print (Multi,'\n',Devide,'\n',Round,'\n',Minus,'\n',Minus2,'\n',charchange,
'\n',charascii)

-----------------
phrase="Hello Alex"
print('\n',phrase,'\n',"Replace: ",phrase.replace("Hello", "Goodbye"),'\n'
, phrase.upper(),'\n',phrase.lower(),'\n', phrase.title(),'\n',
phrase.capitalize(),'\n',phrase.swapcase(),'\n')

--------------------------
phrase1= "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p"
print(phrase1,'\n')
print(phrase1.split('-'),'\n')


phrase2= "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p"
print(phrase2,'\n',phrase2.split('h'),'\n')

-------------------
phrase="Hello World!"
print("Just count L : ",phrase.count("l"),'\n')

print("Count whole : ",phrase.count(""),'\n')


print("Print 0-5 : " ,phrase[0:5] ,'\n')

---------------------
email='   Majid@gmil.com   '
print(email+ '\n'+'"'+email.lstrip()+'"\n"' + email.rstrip()+'"\n"'+email.strip()+'"')


print("Hello, World!")

user_text= "Majid was here!"

print(user_text)

user_text = "have you seen  Majid??"

print(user_text)


--------------------
solved_cases=42

variable_1 = '42'
variable_2 = 42
variable_3 = 4.2
variable_4 = True
print(type(variable_1))
print(type(variable_2))
print(type(variable_3))
print(type(variable_4))


-----------------
myString = "for Freat Justice"
myInt = 1337
myFloat=13.37
mybool=False
print(myString,myInt,myFloat,mybool)
print(type(myString))

---------------
Firstname="Majid"
Lastname="Ahadi"
Fullname=Firstname+ ' '+Lastname
print('\n',Firstname,'\n',Lastname,"\n","Full Name: \t",Fullname)

'''
