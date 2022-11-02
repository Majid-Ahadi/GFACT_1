
print('\n\n')


import socket
import _thread

def handler(client_sock, address):
	client_sock.send(b'Do you want to play a game?\n')
	data = client_sock.recv(1024)
	print(repr(address)+' said ' + data.decode())
	client_sock.close()
	print(repr(address)+ ' Connection ended. ' )



server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 1337))
server_socket.listen(10)
while True:
	print('Server listening for connections ... ')
	client_sock, address = server_socket.accept()
	print('Connection from: '+repr(address))

	_thread.start_new_thread(handler, (client_sock, address))





'''

# UDP Port
import socket

print('Open a terminal and type : nc -u 127.0.0.1 1337 \n')
client_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.bind(('0.0.0.0', 1337))

while True:

	data, addr=client_socket.recvfrom(1024)
	print(data)



---------------------------------------------------
import socket

print('Open a terminla and type "nc -nvlp 1337" in it')


client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1', 1337))

print('To end your chat type: End of Message \n')

with open("Chat.txt",'w') as file:
	file.close()

Chat='A'
while Chat!='end of message':
	Chat=input('Send : ')
	Chat=Chat.lower()
	with open("Chat.txt",'a') as file:
		file.write('Sent: '+Chat)
		file.write('\n')
		file.close()
	client_socket.send(b" \n" +Chat.encode()+ b" \n")
	received= client_socket.recv(1024)
	received=str(received)
	with open("Chat.txt",'a') as file:
		file.write('Received: '+received)
		file.write('\n')
		file.close()
	print('Received : ',received)


client_socket.close()

f=open("Chat.txt",'r')	
content= f.read()
print('\n\n\n Your file Content is : \n\n',content)






----------------------------------------------------
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


'''
print('\n\n')

