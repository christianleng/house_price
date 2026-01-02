import hashlib
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_hash(password: str) -> str:
    sha256_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return bcrypt_context.hash(sha256_hash)


password = "Password123!"
print(generate_hash(password))
