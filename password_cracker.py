import hashlib


def crack_sha1_hash(hash, use_salts=False):
    with open('top-10000-passwords.txt', 'r') as passwordFile:
        for password in passwordFile:
            password = password.strip()
            if use_salts:
                with open('known-salts.txt', 'r') as saltFile:
                    for salt in saltFile:
                        salt = salt.strip()
                        newPassword = salt + password
                        newPassword2 = password + salt
                        newHash = hashlib.sha1()
                        newHash.update(newPassword.encode('ASCII'))
                        if newHash.hexdigest() == hash:
                            return password.strip()
                        else:
                            newHash2 = hashlib.sha1()
                            newHash2.update(newPassword2.encode('ASCII'))
                            if newHash2.hexdigest() == hash:
                                return password.strip()

            else:
                newHash = hashlib.sha1()
                newHash.update(password.encode('ASCII'))
                if newHash.hexdigest() == hash:
                    return password.strip()
    return 'PASSWORD NOT IN DATABASE'
