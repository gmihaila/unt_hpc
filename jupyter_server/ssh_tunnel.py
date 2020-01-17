from sshtunnel import SSHTunnelForwarder
import time
import sshtunnel

IP_ADDRESS_OR_HOSTNAME = "hpc-gateway.hpc.unt.edu"
USERNAME = "george"
PASSWORD = "george"
REMOTE_BIND_IP = "127.0.0.1"
REMOTE_BIND_PORT = 8888
LOCAL_BIND_PORT = 8888

server = sshtunnel.open_tunnel(
    IP_ADDRESS_OR_HOSTNAME,
    ssh_username=USERNAME,
    ssh_password=PASSWORD,
    remote_bind_address=(REMOTE_BIND_IP, REMOTE_BIND_PORT),
    local_bind_address=('0.0.0.0', LOCAL_BIND_PORT),
    debug_level='TRACE',
)

server.start()


print(server.local_bind_port)


time.sleep(30)
server.stop()
