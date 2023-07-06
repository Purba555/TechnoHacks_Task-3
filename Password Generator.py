import random                   
def generate_password(len):  
    "This function accepts a parameter 'len' and returns a randomly generated password"   
     
    list_of_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"  
    selected_character = random.sample(list_of_characters, len)    
    pass_str = "".join(selected_character)      
    return pass_str  
  
# main function  
if __name__ == "__main__":     
    len = int(input("Enter the length of your Password: "))     
    pass_str = generate_password(len)    
    print("Randomly generated Password is:", pass_str) 
