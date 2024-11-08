# Please write a program to compress and decompress the
# string "hello world!hello world!hello world!hello world!".

import zlib

def compress(str):
    data = str.encode('utf-8')
    return zlib.compress(data)

def decompress(data):
    return zlib.decompress(data)

compressed = compress('hello world!hello world!hello world!hello world!')
print(compressed)

decompressed = decompress(compressed)
print(decompressed)