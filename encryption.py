# what i want to do let us see
#1-someone will write to file whatever he wants
#2-program will read that file and we will encrpt the file
#3-delete the original file and keep the encrypted one
#4-decrypted the file to get the original one
#so let imiagine what is our functions

import os
class user_input:
    def text_name():
        name=input('Enter The File Name : ')
        return name

class file_mainpulation:
    def read_file(file_name):
        f=open(file_name+'.txt','r')
        data=f.read()
        f.close()
        return data
    def delete_file(file_name):
        os.remove(file_name+'.txt')
        print("File Removed!")
    def write_file(data,file_name):
        f=open(file_name+'.txt','w')
        f.write(data)

class enc_dec:
    def encryption(data,enc_data):
        for x in data:
            a=ord(x)+5
            b=chr(a)
            enc_data+=b
        return enc_data
    
    def decryption(data,dec_data):
        for x in data:
            a=ord(x)-5
            b=chr(a)
            dec_data+=b
        return dec_data


if __name__ == '__main__':
    print('that is a great module')
     

        
        


