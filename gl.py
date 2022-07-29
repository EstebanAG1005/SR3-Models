# SR2 Lines
# Graficas por computadora 
# Esteban Aldana Guerra 20591

import struct


# 1 byte
def char(c):
    return struct.pack('=c', c.encode('ascii'))

# 2 bytes
def word(c):
    return struct.pack('=h', c)

# 4 bytes 
def dword(c):
    return struct.pack('=l', c)


# funcion de color
def color(r, g, b):
    return bytes([b, g, r])



