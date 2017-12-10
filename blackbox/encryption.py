import gnupg
import config

gpg = gnupg.GPG()


def encrypt():
    with open(config.COMPRESSED_FILE_PATH, 'rb') as input_file:
        status = gpg.encrypt(input_file.read(),
                             config.get_option('keyid', 'General'),
                             output=config.ENCRYPTED_FILE_PATH)
    if status.ok:
        return True
    return False
