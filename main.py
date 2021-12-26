

import bitcoin
import requests


print("Started search...")

def runfor():
    for numbers in range(2222222, 3333333):
        private_key = numbers
        decode_private_key = bitcoin.decode_privkey(private_key)
        valid_private_key = 0 < decode_private_key < bitcoin.N
        wif_encode_private_key = bitcoin.encode_privkey(decode_private_key, "wif")
        public_key = bitcoin.fast_multiply(bitcoin.G, decode_private_key)
        adress = bitcoin.pubkey_to_address(public_key)
        r = requests.get("https://blockchain.info/q/getsentbyaddress/"+adress)


        if int(r.text) > 0:
                resultFile = open("result.txt", "w+")
                # print("Bitcoin Address is:", str(bitcoin.pubkey_to_address(public_key)))
                # print("Private Key is: ", str(wif_encode_private_key))
                # print("Balance is: ",str(r.text))
                print(wif_encode_private_key)
                resultFile.write(str(wif_encode_private_key) + "  wif private key  ")
                resultFile.write(str(bitcoin.pubkey_to_address(public_key)) + "  address public  ")
                resultFile.flush()
                resultFile.close()

try:
    runfor()
except Exception as ex:
    i =1