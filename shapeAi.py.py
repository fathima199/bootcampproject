
import hashlib
m = hashlib.md5()
text = 'hello world'
m.update(text.encode('utf-8'))
print(m.hexdigest())

#USING VARIOUS ALGORITHMS
#using SHA1
hash_object = hashlib.sha1(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)
#using SHA224
hash_object = hashlib.sha224(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)
#using SHA256
ash_object = hashlib.sha256(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)