#import socket module
from socket import *
from threading import * 


class ClientThread(Thread): 
    def _init_(self,ip,port): 
        Thread._init_(self)
        self.ip = ip
        self.port = port
        print ("New server socket thread started for " + ip + ":" + str(port) )

    def run(self):
        while True :
          
            try:
                message = connectionSocket.recv(1048) 
                print ("Server received data: ", message)
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


# create an IPv4 TCP socket
#Fill in start  
serverSocket = socket(AF_INET,SOCK_STREAM)   
#Fill in end

serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

# Prepare a sever socket
serverSocket.bind(("localhost", 6789))
threads = [] 

# Listen for connections from client
#Fill in start     
serverSocket.listen(5)
#Fill in end

while True:
    # Establish the connection
    print ("Multithreaded: Ready to serve...")
    (connectionSocket, addr) = serverSocket.accept()
    newthread = ClientThread() 
    newthread.start()
    threads.append(newthread) 

for t in threads: 
    t.join()
        
# Close server connection
serverSocket.close()
