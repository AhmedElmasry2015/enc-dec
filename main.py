import encryption 

def user_interface():
    print('hello there. it is a nice program \n write whatever you want and guess what ? \n we encrytpt the file')
    x=input('            chosse your operation \n 1:encrption file  \n 2:decrption file')
    print(x)
    if x == '1':
        file_name=encryption.user_input.text_name()
        data=encryption.file_mainpulation.read_file(file_name)
        encryption.file_mainpulation.delete_file(file_name)
        enc_data=encryption.enc_dec.encryption(data,'')
        encryption.file_mainpulation.write_file(enc_data,file_name)
    elif x == '2':
        file_name=encryption.user_input.text_name()
        data=encryption.file_mainpulation.read_file(file_name)
        encryption.file_mainpulation.delete_file(file_name)
        enc_data=encryption.enc_dec.decryption(data,'')
        encryption.file_mainpulation.write_file(enc_data,file_name)
    else:
        print('wrong value the program will terminate')

user_interface()
        
   
                
