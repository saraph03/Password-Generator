import string 
import random

def password_generator():
# defining what the password will include
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    num = string.digits
    special_char = string.punctuation
    #adding the characters 
    password_char = random.sample(lowercase, 2) + random.sample(uppercase, 2) + random.sample(num, 2) + random.sample(special_char, 2)
    #shuffling        
    random.shuffle(password_char) 
    #generating the random password
    password = ''.join(password_char)
    return password
if __name__ == "__main__":
    pwd = password_generator()
    print ("Generated Password: ", pwd)