import string 
import random

def password_generator():
# defining what the password will include
    num_length = int(input("Enter an integer: "))
    if num_length < 8:
        print("Not Valid Length. Password length should be at least 8 characters")
        return None
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    num = string.digits
    special_char = string.punctuation
        
    chars_per_category = num_length // 4
    remaining_chars = num_length % 4
    #adding the characters 
    password_char = random.sample(lowercase, chars_per_category) + random.sample(uppercase, chars_per_category) + random.sample(num, chars_per_category) + random.sample(special_char, chars_per_category + remaining_chars)
    #shuffling        
    random.shuffle(password_char) 
    #generating the random password
    password = ''.join(password_char)
    return password
if __name__ == "__main__":
    pwd = password_generator()
    print ("Generated Password: ", pwd)
