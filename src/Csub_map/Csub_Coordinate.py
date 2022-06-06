from threading import *
import zmq
import pickle
import time
import struct
import coloredlogs
import logging
import os
from queue import Queue
import matplotlib.pyplot as plt
import numpy as np
import binascii

# q=Queue(maxsize=0)

coloredlogs.install(level='DEBUG', fmt='[%(pathname)s:%(lineno)d @ %(asctime)s.%(msecs)03d] %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = r"./"
# log_name = log_path + rq + '.log'
log_name = '202107218888.log'
fh = logging.FileHandler(log_name, mode='w')
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)


class SUB:
    def __init__(self):
        self.pre_time = 0
        self.x = []
        self.y = []
        self.rfid = []
        self.r_x = []
        self.r_y = []
        self.counter = 0
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        port = 46142
        # port = 46372
        # self.socket.connect("tcp://localhost:%d" % port)
        self.socket.connect("tcp://192.168.137.3:%d" % port)
        # self.socket.connect("tcp://192.168.52.30:%d" % port)
        # self.socket.connect("tcp://192.168.50.217:%d" % port)
        # self.socket.connect("tcp://192.168.50.217:%d" % port)
        print("port: ", port)
        logger.info([2, 3, 4])
        self.socket.subscribe("")
        # self.socket.setsockopt_string(zmq.SUBSCRIBE, "")
        th = Thread(target=self.run)
        # th.setDaemon(True)
        th.start()

        # th2 = Thread(target=self.draw)
        # # th2.setDaemon(True)
        # th2.start()
        # self.sub = Subscriber('self_coordinate', self.load_data)

    def run(self):
        while True:
            sg = self.socket.recv()
            msg = self.socket.recv()
            self.counter += 1
            msg = binascii.b2a_hex(msg).decode()
            msg = bytearray.fromhex(msg)
            cache_data = struct.unpack('3f', msg)
            Cx, Cy, Cyaw = cache_data
            if self.counter > 3:
                self.x.append(Cx)
                self.y.append(Cy)
                self.counter = 0
            logger.info([Cx, Cy, Cyaw])
            print([Cx, Cy, Cyaw])
            # if msg["rfid"] != 0 and ((time.time() - self.pre_time ) > 1.5 or self.pre_time == 0):
            # if msg["rfid"] != 0:
            #     self.pre_time = time.time()
            #     logger.error(["!!!!RIFD!!!!",msg])
            #     self.rfid.append(msg["rfid"])
            #     self.r_x.append(msg["X"])
            #     self.r_y.append(msg["Y"])
            # logger.info("111111111111111")
            time.sleep(0.01)

    def draw(self):
        while True:
            plt.cla()
            plt.gcf().canvas.mpl_connect('key_release_event',
                                         lambda event: [exit(0) if event.key == 'escape' else None])
            plt.axis("equal")
            plt.plot(self.x, self.y)
            # plt.scatter(self.r_x, self.r_y,s=20, c="red")
            plt.pause(0.01)


if __name__ == '__main__':
    a = SUB()
    a.draw()
    # SUB()
    # Draw()
    # b = Draw()
    # b.start()


