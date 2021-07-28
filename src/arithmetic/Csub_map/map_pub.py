import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:46142")

while True:
    message = "{\"x\": 33, \"y\": 33, \"heading\": 99}"
    print(message)
    socket.send_string(str(message))
    time.sleep(1)
