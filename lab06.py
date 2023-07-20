def encode(password):
    encoded = ""
    for num in password:
        encoded_num = str(int(num) + 3)
        if len(encoded_num) > 1:
            encoded_num = encoded_num[-1]
        encoded += encoded_num
    return encodeddef encode(password):
    for num in password:
        encoded = ""
        encoded_num = int(num) + 3
        if len(encoded_num) > 1:
            encoded_num = encoded_num[-1]
        encoded += encoded_num
    print("Your password has been encoded and stored.")

def main():
    proceed = True
    while proceed:
        print("Menu")
        print("-------------")
        print("1. Encode \n2. Decode  \n3. Quit")
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            passkey = input("Please enter your password to encode: ")
            key_encoded = encode(passkey)
            print("Your password has been encoded and stored.")
            print()
            if menu option == 2:
                decoded_key = decode(key_encoded)
                print(f"The encoded password is {key_encoded}, and the original password is {decoded_key}.")
            if menu_option == 3:
                proceed = False



if __name__ == '__main__':
    main()
