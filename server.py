from socket import socket, AF_INET,SOCK_STREAM
import sys

#the function gets a client socket and gets a message from him,procceses it and returns a tuple of the file name
#and the connection type.
def getRequestFromClient(client_socket):
    data = client_socket.recv(1000)

    #after getting the message, if it's empty we raise and EMPTY exception that refers to empty messages
    if not data:raise Exception("EMPTY")

    #else the message is printed and we look for the fields of the user request in the data
    request_string=data.decode()
    print(request_string)

    #split the message by lines
    lines_arr=request_string.split("\r\n")

    #get the file request from the second place after a ' ' in the first line
    file_name=lines_arr[0].split()[1]

    #get the connection type line from the third line in the request
    connection_type=lines_arr[2]

    #split the line by ' '
    lister = connection_type.split()

    #get the second place (where the connection type will actually be)
    real_connection = lister[1]

    #return the tuple of the (file_name, connection_type)
    return file_name, real_connection

#this function gets the request from the client and returns the file directory.
def getFileDir(file_name):

    #if the client requested '/' we return index.html
    if file_name == "/":
        file_name ="index.html"

    #if the client requested redirect we raise "301" exception
    if file_name == "/redirect":
        raise Exception("301")

    #else we add the "files/" prefix and return the file dir
    file_dir="files/"+file_name
    return file_dir

#the function gets the file directory, the client socket and the connection type and sends a message to the client
def sendFileToClient(file_dir,client_socket,connection_type):
    try:
        #open and read file
        file = open(file_dir)
        message_content=str(file.read())
        file.close()

        #if there was no exception from the file we will send the message that says the file exist and send the file
        message="HTTP/1.1 200 OK/r/nConnection: "+connection_type+"\r\nContent-Length: "+str(len(message_content.encode()))+"\r\n\r\n"+message_content    
        client_socket.send(message.encode())

    #if the file was not found we raise "404" exception.
    except FileNotFoundError as e:
        raise Exception("404")
def sendImageToClient(file_dir,client_socket,connection_type):
    try:

        #opening the file the client requested as bytes
        file = open(file_dir,"rb")
        
        #read the file
        f = file.read()

        #b is an array in which each element is a byte in the file opened
        b = bytearray(f)
        
        #send the client the message which contains the image
        message=b"HTTP/1.1 200 OK/r/nConnection: "+connection_type.encode()+b"\r\nContent-Length: "+str(len(b)).encode()+b"\r\n\r\n"+b
        client_socket.send(message)

        #closing the file
        file.close()
    #if the file the client requested is not is the folder
    except FileNotFoundError as e:
        raise Exception("404")

#create a host TCP socket
server = socket(AF_INET, SOCK_STREAM)

#bind the port based on the argumets recieved in commend line
port = int(sys.argv[1])
server.bind(('', port))
server.listen(5)
while True:
    #create a designated client socket for each new client the host accepts
    client_socket, client_address = server.accept()
    
    #set the timeout for 1 second- if timeout occured, it means the client hasn't sent a request for over 1 second
    client_socket.settimeout(1.0)
    while True:
        try:
            #get request from client
            file_name, connection_type = getRequestFromClient(client_socket)

            #get the path to the file requested
            file_dir=getFileDir(file_name)
            
            #get the file type- html, jpg, ico etc.
            file_type=file_name.split('.')[-1]
            if file_type=="ico" or file_type=="jpg":
                sendImageToClient(file_dir,client_socket,connection_type)
            else:
                sendFileToClient(file_dir,client_socket,connection_type)

        #if the client hasn't sent a request for over a second, close the coket and exit loop to wait for new clients   
        except TimeoutError as te:
            client_socket.close()
            break
        except Exception as e:
            #if the file the client asked was not found
            if str(e)=="404":
                client_socket.send(b"HTTP/1.1 404 Not Found\r\nConnection: close\r\n\r\n")
                client_socket.close()
                break
            #if the client requested redirect
            elif str(e)=="301":
                #send the client the lovation to redirect to - result.html, and close the designated client socket created
                client_socket.send(b"HTTP/1.1 301 Moved Permanently\r\nConnection: close\r\nLocation: /result.html\r\n\r\n") 
                client_socket.close()
                break
            #if the client sent an empty message, close the designated client socket and exit loop to wait for new clients
            elif str(e)=="EMPTY":
                client_socket.close()
                break
            else:
                client_socket.close()
                break
                
        #If connection type is closed we need to close the client socket and exit the loop to wait for new clients    
        if connection_type == "close":
            client_socket.close()
            break
       