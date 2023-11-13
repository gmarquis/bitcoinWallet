from bitcoin import *
outfile = open('new-wallet.txt','w')
private_key = ""
print(private_key)
public_key = privtopub(private_key)
print(public_key)
address = pubtoaddr(public_key)
print('btc address: ' +address)
outfile.write('btc address: ' +address+ '\n')
outfile.write('btc public: ' +privtopub(private_key) + '\n')
outfile.write('btc hex private: ' +private_key + '\n')
outfile.close()