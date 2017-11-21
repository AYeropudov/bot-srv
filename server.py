import logging
from websocket_server import WebsocketServer

logging.basicConfig(filename="./logfile.txt")
stderrLogger=logging.StreamHandler()
stderrLogger.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
logging.getLogger().addHandler(stderrLogger)
logs = logging.getLogger()


def new_client_connected(client, server):
    logs.debug('test')


server = WebsocketServer(12345, host='127.0.0.1', loglevel=logging.INFO)
server.set_fn_new_client(new_client_connected)
server.run_forever()
