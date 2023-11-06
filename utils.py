from nacl.public import PrivateKey, Box, PublicKey
from nacl.encoding import Base64Encoder

def key_to_str(key):
  encoded_key = key.encode(encoder=Base64Encoder)
  str_key = encoded_key.decode('utf-8')
  assert key.encode(encoder=Base64Encoder) == str_key.encode()
  return str_key

def str_to_private_key(str_key):
  key = PrivateKey(str_key, encoder=Base64Encoder)
  return key

def str_to_public_key(str_key):
    key = PublicKey(str_key, encoder=Base64Encoder)
    return key

def save_key_to_file(key, filename):
    str_key = key_to_str(key)
    with open(filename, "w") as file:
        file.write(str_key)

def create_keys_and_files(filename):
    key = PrivateKey.generate()
    save_key_to_file(key, filename  + ".key")
    save_key_to_file(key.public_key, filename + ".pub.key")

def load_key_from_file(filename, type):
    with open(filename, "r") as file:
        str_key = file.read()
    if type == "private":
        key = str_to_private_key(str_key)
    elif type == "public":
        key = str_to_public_key(str_key)
    else:
        raise ValueError("type must be 'private' or 'public'")
    return key
    
def decrypt_response_content(encrypted_content, study_private_key, server_public_key):
    """Decrypts the response """
    decrypt_box = Box(study_private_key, server_public_key)
    decrypted_content = decrypt_box.decrypt(encrypted_content)
    return decrypted_content
  
def decrypt_data_file(filename, study_private_key, server_public_key, enc_file_extension=".enc"):
    """ Decrypts a data file """
    with open(filename, "rb") as file:
        encrypted_content = file.read()
    decrypted_content = decrypt_response_content(encrypted_content, study_private_key, server_public_key)
    write_filename = filename.replace(enc_file_extension, "")
    with open(write_filename, "wb") as file:
        file.write(decrypted_content)
