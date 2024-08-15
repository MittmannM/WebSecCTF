from Crypto.Cipher import AES
import hashlib


p = 3212680853
g = 2
a = 632
b = 806
g_c = 1999514834
IV = "dcba12b632d2cbfc96a628d9628ff17a"
ciphertext = "3e955b5f8486824bd90b75bc49ec26d645046b10c17c70b8017ee97b648e2f273c3aef5dd91152b25485a8b3f5283b25ed63064ef870fa08325194b3c7bb95e1e248533458cfc5d36d8538f13c17604b6b6c71ac13026eb30233c54ec813192094901c0ecdeffa9bf35cf8224f52f5409fa80013568767db47a446db1c79b336628c003ce597a1c5f48c308f76cbd386"

shared_secret = pow(g_c, a*b, p)
key = hashlib.sha256(f"{shared_secret}".encode()).digest()

IV_bytes = bytes.fromhex(IV)
ciphertext_bytes = bytes.fromhex(ciphertext)

cipher = AES.new(key, AES.MODE_CBC, IV_bytes)
plaintext = cipher.decrypt(ciphertext_bytes)

print(plaintext[68:138].decode("utf-8"))
