# LogStream
Logstream is a barebones implementation of reading server-side logs in real-time and serving them to the connected clients using sockets.

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
- Find the container name using `docker ps` ![docker ps output](https://postimg.cc/ZBjnq2QL)
<img src="https://postimg.cc/ZBjnq2QL">

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)