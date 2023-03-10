# LogStream
Logstream is a barebones implementation of reading server-side logs in real-time and serving them to the connected clients using sockets.

## Architecture
[![Diagram.png](https://i.postimg.cc/FK56vYZ6/Diagram.png)](https://postimg.cc/7599MYj1)

## Installation/Setup
### Traditional way (Python+Flask on your machine)
`Requires Python installed on your machine`
- Clone this repository
- Initialise a virtualenv inside the project directory using `python3 -m venv .venv`
- Activate the virtualenv using `source .venv/bin/activate`
- Install all required libraries using `pip3 install -r requirements.txt`

### Using Docker
`Requires docker installed on your machine`
- Clone this repository
- Build a docker image from the dockerfile using `docker build --tag logstreamer-python . `
- Run docker in detached mode `docker run -d -p 5000:5000 logstreamer-python:latest` 


## Usage
### Traditional Way (Python+Flask)
- Run the `server.py` file using `python3 server.py` and you'll see flask starts serving the application on port 5000.
- Open http://localhost:5000 in as many tabs as you want. (Each tab acts as a client - multiple clients)
- Append new lines in `logs.txt`

### Using Docker
- Since the flask application is checking for any changes in the `logs.txt` - it's stored inside the running docker container. Hence we need to go inside the container and edit that file in order to see the changes
- Open http://localhost:5000 in your browser to act as a client
- Find the running container name using `docker ps`
[![image.png](https://i.postimg.cc/J0CkpWcS/image.png)](https://postimg.cc/ZBjnq2QL)
- Enter the container using `docker exec -it gallant_wilbur bash` where `gallant_wilbur` is the name of the container found using `docker ps`
- Edit the logs.txt using `nano` or `vim` and save it.
- You can check the browser which will reflect all new lines added the logs file.


## Demo
[![image.png](https://i.postimg.cc/mDpHGH4f/image.png)](https://postimg.cc/ftXLckkB)


## Technical Issues and Solutions
#### How to establish a connection between client and server ?
We have used websockets in this case. The server side opens a port for the clients to connect. Sockets are of two types - TCP and UDP. We have used TCP by default in Flask.
#### How to know that something is added to the file ?
We have started a background process in flask that keeps reading the `logs.txt` file. By storing the last known position (seek) we only watch the file for new lines added. 
#### How to make sure that only the newly added text is sent to the client ?
We are using seek and storing the last known EOF position. The background process only checks for new lines added from the last known position and only reads them and not the entire file.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)