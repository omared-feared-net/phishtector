import random, socket, struct
f = open("fakeipaddresses.txt", "w")
f.write(socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))))
f.close()


