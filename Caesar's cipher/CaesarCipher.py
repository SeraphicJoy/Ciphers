def caesar_encrypt(string, key):
    s2 = ""
    for symbol in string:
        if symbol.isalpha():
            base = ord('A') if symbol.isupper() else ord('a')
            newsymbol = chr((ord(symbol) - base + key) % 26 + base)
            s2 += newsymbol
        else:
            s2 += symbol
    return s2
def caesar_decrypt(string, key):
    return caesar_encrypt(string, -key)

if __name__ == "__main__":
    string = input("Enter string: ")
    key = int(input("Enter key: "))

    print("Result:", caesar_encrypt(string,key))

