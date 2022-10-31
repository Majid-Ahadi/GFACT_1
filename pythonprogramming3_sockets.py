print('\n\n')

flag=False
filename= input('What is the name of file that you to create?')
try:
	with open(filename, "x") as file:
        # Print the success message
		print("File has opened for reading.")
# Raise error if the file is opened before
except FileExistsError:
	print("File already exists.")
	flag=True


if flag==True:
	answer=input(f'If you want to add content to the {filename} press Y \n If you like to clear content and start from begining press N : ')	
	answer=answer.lower()
	if answer=='y':	
		with open(filename,'a') as file:
			
			text= input(f'What do you like to add to the {filename} ? ' )
			file.write(text)
			file.close()
			f=open(filename,'r')	
			content= f.read()
			print('\n\n\n Your file Content is : \n\n',content)
	else:
		with open(filename,'w') as file:
			text= input(f'What do you like to add to the {filename} ? ' )
			file.write(text)
			file.close()
			f=open(filename,'r')
			content= f.read()
			print('\n\n\n Your file Content is : \n\n',content)



else:
	with open(filename,'w') as file:
		text= input(f'What do you like to add to the {filename} ? ' )
		file.write(text)
		file.close()
		f=open(filename,'r')
		content= f.read()
		print('\n\n\n Your file Content is : \n\n',content)



print('\n\n')
