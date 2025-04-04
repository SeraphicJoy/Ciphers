def encrypt(key, cipher):

    num_rows = (len(cipher) + key - 1) // key

    table = ['' for _ in range(num_rows)]

    for i in range(len(cipher)):
        row = i // key
        table[row] += cipher[i]

    if len(table)>1:
        n = len(table[0]) - len(table[-1])
        for i in range(n):
            table[-1] += ' '

    inverted_table = [row[::-1] for row in table]

    encrypted_text = ''
    for col in range(key):
        for row in inverted_table:
            if col < len(row):
                encrypted_text += row[col]

    return encrypted_text

def decrypt(key, cipher):
    num_rows = (len(cipher) + key - 1) // key

    table = ['' for _ in range(num_rows)]

    index = 0
    for col in range(key):
        for row in range(num_rows):
            if index < len(cipher):
                table[row] += cipher[index]
                index += 1

    decrypted_table = [row[::-1] for row in table]

    decrypted_text = ''.join(decrypted_table).rstrip()

    return decrypted_text


if __name__ == "__main__":
    cipher = input("Enter string: ")
    key = int(input("Enter key: "))
    print("Encrypted string: ", encrypt(key, cipher))
    print("Decrypted string: ", decrypt(key, encrypt(key,cipher)))