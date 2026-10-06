"""CR-05 source: wrapper that hides RSA behind sign_payload() / verify_payload()."""
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

from .constants import DEFAULT_KEY_SIZE

_key = None


def _get_key():
    global _key
    if _key is None:
        _key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return _key


def sign_payload(data: bytes) -> bytes:
    return _get_key().sign(data, padding.PKCS1v15(), hashes.SHA256())


def verify_payload(data: bytes, signature: bytes) -> None:
    _get_key().public_key().verify(signature, data, padding.PKCS1v15(), hashes.SHA256())


def export_public_pem() -> bytes:
    return _get_key().public_key().public_bytes(
        serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)


__all__ = ["sign_payload", "verify_payload", "export_public_pem", "DEFAULT_KEY_SIZE"]
