import socket

HOST = 'localhost'
PORT = 8000        

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



client.connect((HOST,PORT))


print("Successfully connected to the server")



while 1:

    request = input("Enter the Request: ")
    client.send(request.encode())
                

    response = client.recv(1024).decode()
    print("The requested list by the user is: ")
    print(response)



client.close()


