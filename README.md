<h4 align="center">


![](https://github.com/TopazAvraham/IntroductionToCS-University-C-programming/blob/master/Screenshots/32.png?raw=true)

</h4>

<h4 align="center">Implementation of server code code which acts similar to HTTP server!</h4>

<p align="center">
  <a href="##Introduction">Introduction</a> •
  <a href="#Screenshots">Implementation</a> •
   <a href="#Screenshots">Visualization & Screenshots</a> •
  <a href="#Installation">Installation</a> •
  <a href="#Author">Author</a> •
  <a href="#Support">Support</a> 

</p>

<p align="center">
  <img width="600" height="500" src="Images/12.gif">
</p>


## Introduction

This server code is the product of computer-networks course assignment, which I took in the 1st semester of my 2nd year at BIU university. <br>  
I implemeted an HTTP server on top of TCP, which handles requests from client's browsers to see specific files that sits on the server folder.
<br>After request from client & handling from server is complete, the client can see the result in his browser.



💥 Client request to see specific file like HTML, JPG, etc. using his browser.

💥 Server handles the request from the client.

💥 The client can see the result on his browser' screen.


## Implementation

In the folder of the repository, there is a server code and a files folder. The server functions as a file storage HTTP server which allows clients to coonect, 
and request files that are inside the files folder.

The files folder contains html pages, jpg photos, etc. <br>

If a client requests a file that in not in the files folder, HTTP 404 error will occur. <br>

After running the server code on the terminal with argument that will be the port server, client can connect with this server, <br>
and ask for pages and files 
that are inside the files folder and they will see it in their browser.
    

## Visualization & Screenshots
 
### Visualization
<br>
  
<img width="500" height="400" src="https://github.com/TopazAvraham/IntroductionToCS-University-C-programming/blob/master/Screenshots/http.png?raw=true"> <br>


### Screenshots

  <img width="1000" height="500" src="https://github.com/TopazAvraham/IntroductionToCS-University-C-programming/blob/master/Screenshots/40.png?raw=true">

  <img width="1000" height="500" src="https://github.com/TopazAvraham/IntroductionToCS-University-C-programming/blob/master/Screenshots/41.png?raw=true">


## Installation - How To Run Code
<b>

1. Clone this repo by creating a specific folder in your computer, open terminal in this folder and run this command:
    ```
    git clone https://github.com/TopazAvraham/HTTP-server-using-TCP-Sockets
    ```
    Alternatively, you can just download all the files from this repo to your computer, and save them all in that specific folder

2. Open “terminal” in this specific folder.<br>
	
3. Run this command in one terminal to run the server code:
	```
    python3 server.py (para1)
    ```
	
	where para1 = port number that the server will listen to.
  <br>
  
5. Open any browser you want: Google Chrome, FireFox, Edge, Safari, etc.
  
6. write in the search bar (url) the following format:
	
    ```
    http://[Server IP]:[Server port][Path]
    ```
  
and enter the server IP, Port, and path accordingly.
	
7. Press enter and enjoy the results.
	

</b>	

## Built With

- Python
- TCP Sockets

<br />

## Author

**Topaz Avraham**

- [Profile](https://github.com/TopazAvraham?tab=repositories )
- [Email](mailto:topazavraham9@gmail.com?subject=Hi "Hi!")
- [LinkedIn](https://www.linkedin.com/in/topaz-avraham-68b340208/ "Welcome")

## 🤝 Support

Contributions, issues, and feature requests are welcome!

Give a ⭐️ if you like this project!
