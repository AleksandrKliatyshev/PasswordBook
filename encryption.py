from cryptography.fernet import Fernet
import base64
import hashlib
import json

class Encryption:
    def __init__(self, master_password):
        key = hashlib.sha256(master_password.encode()).digest()
        self.cipher = Fernet(base64.urlsafe_b64encode(key))
    
    def encrypt_data(self, data):
        json_str = json.dumps(data)
        return self.cipher.encrypt(json_str.encode()).decode()
    
    def decrypt_data(self, encrypted_data):
        decrypted = self.cipher.decrypt(encrypted_data.encode())
        return json.loads(decrypted)