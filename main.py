from Crypto.Cipher import AES
from Crypto import Random
import numpy as np
import math


def countByte(data):
    countedData = [0] * 256
    for k in data:
        countedData[k] += 1
    return countedData


def calculateSecrecy(key, cipher):
    countedKey = countByte(key)
    countedCipher = countByte(cipher)

    entropy = 0
    secrecy = 0

    for j in range(0, 256):
        p_k = 1.0 * countedKey[j] / len(key)
        p_c = 1.0 * countedCipher[j] / len(cipher)
        if (p_k > 0):
            entropy += p_k * np.log2(p_k)
            secrecy += -p_c * entropy

    return secrecy


def encryptAES(key, plaintext):
    cipher = AES.new(key)
    ciphertxt = cipher.encrypt(plaintext)
    return ciphertxt


def getResults(keysize, plaintextsize):
    key = Random.new().read(keysize)
    totalValue = 0

    for i in range(0, 100):
        plaintext = Random.new().read(plaintextsize)
        ciphertxt = encryptAES(key, plaintext)

        cipherbyte = np.fromstring(ciphertxt, dtype=np.uint8)
        keybyte = np.fromstring(key, dtype=np.uint8)
        totalValue += calculateSecrecy(keybyte, cipherbyte)

    avgValue = totalValue / 100
    return avgValue
