# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from ..algorithm import AsymmetricEncryptionAlgorithm
from ..transform import CryptoTransform


class _Rsa1_5Encryptor(CryptoTransform):
    def transform(self, data):
        return self._key.encrypt(data, padding.PKCS1v15())


class _Rsa1_5Decryptor(CryptoTransform):
    def transform(self, data):
        return self._key.decrypt(data, padding.PKCS1v15())


class Rsa1_5(AsymmetricEncryptionAlgorithm):  # pylint:disable=client-incorrect-naming-convention
    _name = "RSA1_5"

    def create_encryptor(self, key):
        return _Rsa1_5Encryptor(key)

    def create_decryptor(self, key):
        return _Rsa1_5Decryptor(key)


class _RsaOaepDecryptor(CryptoTransform):
    def __init__(self, key, hash_cls):
        self._hash_cls = hash_cls
        super(_RsaOaepDecryptor, self).__init__(key)

    def transform(self, data):
        oaep_padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=self._hash_cls()), algorithm=self._hash_cls(), label=None
        )
        return self._key.decrypt(data, oaep_padding)


class _RsaOaepEncryptor(CryptoTransform):
    def __init__(self, key, hash_cls):
        self._hash_cls = hash_cls
        super(_RsaOaepEncryptor, self).__init__(key)

    def transform(self, data):
        oaep_padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=self._hash_cls()), algorithm=self._hash_cls(), label=None
        )
        return self._key.encrypt(data, oaep_padding)


class RsaOaep(AsymmetricEncryptionAlgorithm):
    _name = "RSA-OAEP"

    def create_encryptor(self, key):
        return _RsaOaepEncryptor(key, hashes.SHA1)

    def create_decryptor(self, key):
        return _RsaOaepDecryptor(key, hashes.SHA1)


class RsaOaep256(AsymmetricEncryptionAlgorithm):
    _name = "RSA-OAEP-256"

    def create_encryptor(self, key):
        return _RsaOaepEncryptor(key, hashes.SHA256)

    def create_decryptor(self, key):
        return _RsaOaepDecryptor(key, hashes.SHA256)


Rsa1_5.register()
RsaOaep.register()
RsaOaep256.register()
