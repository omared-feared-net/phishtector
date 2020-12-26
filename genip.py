import random, socket, struct
socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

