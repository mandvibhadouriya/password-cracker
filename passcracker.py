import hashlib
flag = 0
pass_hash = input("Enter a hash value : ")
pass_file = input("File name of words : ")

try:
    Read_pass = open(pass_file,"r")
except:
    print("File didn't match")
    quit()

for word in Read_pass:
    utf = word.encode('utf-8')
    md5 = hashlib.md5(utf.strip()).hexdigest()
    if md5 == pass_hash:
        print("Password matched")
        print("Password id ", word)
        flag =1
        break
if flag == 0:
    print("Password doesn't matched")