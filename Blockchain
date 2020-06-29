"""

На основе кода, размещенного в файле blockchain.py, реализовать корутину (генератор), позволяющий с помощью метода send(), возвращать новый блок. Кроме механизма возврата нового блока требуется создать механизм, позволяющий вернуть историю сгенерированных блоков. 

"""

import random
from hashlib import sha3_512
import binascii

genesis_block = bytearray([0 for i in range(0, 64)])
baseblock = genesis_block


def randomblock(limit):
    for i in range(0, limit):
        ml = sha3_512()
        ml.update(str(random.randint(0, 1e18)).encode("iso-8859-1"))
        yield bytearray(ml.hexdigest().encode("iso-8859-1"))


def signedblock(baseblock, limit):
    for block in randomblock(limit):
        block_data = baseblock + block
        digest = sha3_512()
        digest.update(block_data)
        baseblock = digest.digest()
        yield block_data + digest.digest()


limit = 5
blocks = [block for block in signedblock(genesis_block, limit)]
assert len(blocks) == limit
for block in blocks:
    print("link=" + binascii.hexlify(block[0:64]).decode("iso-8859-1"))
    print("data=" + block[64:192].decode("iso-8859-1"))
    print("digest=" + binascii.hexlify(block[192:256]).decode("iso-8859-1"))
    print("==========================")
    assert (len(block) == 256)  # 64 (reference) + 128 (data) + 64 (hash)
