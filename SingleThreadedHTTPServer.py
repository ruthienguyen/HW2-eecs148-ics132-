#import socket module
from socket import *

# create an IPv4 TCP socket
#Fill in start  
serverSocket = socket(AF_INET,SOCK_STREAM)   
#Fill in end

# Prepare a sever socket
serverSocket.bind(("localhost", 6789))

# Listen for connections from client
#Fill in start     
serverSocket.listen(5)
#Fill in end

while True:
    # Establish the connection
    print ("Ready to serve...")
    (connectionSocket, addr) = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)#Fill in start     #Fill in end
        message_split = message.split()
        if len(message_split) <= 1:
            # Small connection from browser - ignore
            connectionSocket.close()
            continue
            
        filename = message_split[1]
        f = open(filename[1:], "rb")
        outputdata = f.read()
        
        # Send one HTTP header line into socket
        #Fill in start 
        header = 'HTTP/1.1 200 OK\r\n' 
        header += '\r\n'
        connectionSocket.send(header.encode())
        #connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        #Fill in end
        
        # Send the content of the requested file to the client
        #Fill in start   
        connectionSocket.send(outputdata)  
        #Fill in end
        
        # Close client socket
        #Fill in start    
        connectionSocket.close() 
        #Fill in end        
    except IOError:
        # Send response message for file not found
        #Fill in start 
        connectionSocket.send("404: Not Found".encode())    
        #Fill in end
        
        # Close client socket
        #Fill in start   
        connectionSocket.close()  
        #Fill in end
    except KeyboardInterrupt:
        # User pressed Ctrl+C, exit gracefully
        break
        
# Close server connection
serverSocket.close()
