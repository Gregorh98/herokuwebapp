import hashlib


def hash_password(password):
    password_bytes = password.encode("utf-8")
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password_bytes)
    hashed_password = sha256_hash.hexdigest()
    return hashed_password


def check_password(input_password, stored_hash):
    input_hash = hash_password(input_password)
    return input_hash == stored_hash
