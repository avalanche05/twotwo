import uuid
import hashlib


def hash_password(password: str) -> str:
    salt = uuid.uuid4().hex
    return hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_match(hashed_password: str, user_password: str) -> bool:
    password, salt = hashed_password.split(':')
    return password == hashlib.sha512(salt.encode() + user_password.encode()).hexdigest()
