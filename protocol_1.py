"""
Alice -> Bob  : 8979f7ec6eaa48d6fbd37cf065f122890e828f76c2b9edf1896e0cd26b3e0650435acaae4e414bd6be7143bf1950c38c55d96a9e45ff43f680602f5af41a690763d46c34360f4fc362a6e8a8d13b732458c65e
Bob   -> Alice: 7c7387a1b4a7374bb87a7f5ebfdad9cefda25d9e6b453cac9074265ba606857be4b8128749d7fd67bb8ba2a9a6d5eecd5108cd2c7d990d6e3d35d094dfb26e56a7c59d08dfaf37b4db0b1802308849f2af8f11
Alice -> Bob  : 34863b088bcdd4ce4ac1be47bf315f98184a8b2f4212bad158d9a819d2e11f9c4bd4e00cb9713fa929c3e15f2ef5375f01f33f8c54c4ca8bd5871a13a6c43d8c27f750a264e3d282d2e97ff4cee8dad3567f73
The secret key was successfully exchanged.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Alice -> Bob  : a8e33f3634a3d00b661ae2803645cd918f0f1ca3b48d04c12cb6f6d14b90caf2b3546d51e1b4dd7160755f07de24456d704bec5f0ecee14c0e9db782de245bb0aab4fef0e21cc190121bff0c400faf66ee5a41
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

enc_k_e = 0x8979f7ec6eaa48d6fbd37cf065f122890e828f76c2b9edf1896e0cd26b3e0650435acaae4e414bd6be7143bf1950c38c55d96a9e45ff43f680602f5af41a690763d46c34360f4fc362a6e8a8d13b732458c65e
enc_enc_k_e_x = 0x7c7387a1b4a7374bb87a7f5ebfdad9cefda25d9e6b453cac9074265ba606857be4b8128749d7fd67bb8ba2a9a6d5eecd5108cd2c7d990d6e3d35d094dfb26e56a7c59d08dfaf37b4db0b1802308849f2af8f11
enc_k_x = 0x34863b088bcdd4ce4ac1be47bf315f98184a8b2f4212bad158d9a819d2e11f9c4bd4e00cb9713fa929c3e15f2ef5375f01f33f8c54c4ca8bd5871a13a6c43d8c27f750a264e3d282d2e97ff4cee8dad3567f73
msg = 0xa8e33f3634a3d00b661ae2803645cd918f0f1ca3b48d04c12cb6f6d14b90caf2b3546d51e1b4dd7160755f07de24456d704bec5f0ecee14c0e9db782de245bb0aab4fef0e21cc190121bff0c400faf66ee5a41


def xor_hex_str(h1, h2):
    return h1 ^ h2


def convert_to_readable(hex_int: int):
    hex_str = hex(hex_int)
    if hex_str.startswith('0x'):
        hex_str = hex_str[2:]
    return "".join([chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2)])


x = xor_hex_str(enc_k_e, enc_enc_k_e_x)
key = xor_hex_str(x, enc_k_x)
dec_msg = xor_hex_str(key, msg)
readable_msg = convert_to_readable(dec_msg)
print(readable_msg)
