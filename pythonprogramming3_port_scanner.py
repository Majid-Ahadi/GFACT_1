print('\n\n')
import socket

print('Please enter an IP address to scan. ')
target= input('> ')

print('*'*40)
print('* Scanning: ' + target + ' *')
print('*' * 40)

for port in range(1, 1025):
	s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result= s.connect_ex((target,port))
	if result==0:
		print("Port: "+str(port)+" Open")
	s.close()








print('\n\n')
