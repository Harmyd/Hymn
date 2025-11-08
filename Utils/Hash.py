from passlib.context import CryptContext

password_context=CryptContext(schemes=['bcrypt'], deprecated="auto")

class Hash():
    def hash_password(self,password):
        return password_context.hash(password)
    def verify_hash(self,password,hashed_password):
        return password_context.verify(password,hashed_password)