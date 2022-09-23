# Tuple
SECURE = (('s', '$'), ('and', '&'), ('a', '@'), ('i', '!'), ('I', '|'),
          ('h', '#'), ('o', '0'), ('z', '2'), ('S', '5'), ('c', '<'), ('7', '?'))


# Replace alphabets
def securePassword(password):
    for a, b in SECURE:
        password = password.replace(a, b)
    return password


# Main program
if __name__ == "__main__":
    password = input("Enter your password: ")
    password = securePassword(password)
    print("Your secure password is: " + password)
