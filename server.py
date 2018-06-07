# coding:utf-8

ROOMBA_PORT = "/dev/ttyUSB0"

import logging
import json
from websocket_server import WebsocketServer

from robot import RoombaClient
roomba = RoombaClient(ROOMBA_PORT)

def new_client(client, server):
  server.send_message_to_all("Hey all, a new client has joined us")
  print("join")
  print(client)

def on_receive_message(client, server, message):
  json_dict = json.loads(message)
  type = json_dict['type']
  data = json_dict['data']
  print('type：{}'.format(type))
  print(data['x'])
  print(data['y'])
  roomba.moveToward(data['x'], data['y'])



  # server.send_message_to_all("Hey all, a new client has joined us")






server = WebsocketServer(3000, host='0.0.0.0', loglevel=logging.INFO)
server.set_fn_new_client(new_client)
server.set_fn_message_received(on_receive_message)
server.run_forever()
