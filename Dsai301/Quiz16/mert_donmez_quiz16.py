#Mert Donmez
#2016203039

def Ccipher(string, shift):
    
    result = ""
    shift = shift % 26
    for char in string:
       
        if ord(char) <= 90 and ord(char) >= 65:
            if (ord(char) + shift) <= 90:
                shifted_char = chr((ord(char) + shift))
            else:
                shifted_char = chr((ord(char) + shift - 26))
            result += shifted_char
        
        elif ord(char) <= 122 and ord(char) >= 97:
            if (ord(char) + shift) <= 122:
                shifted_char = chr((ord(char) + shift))
            else:
                shifted_char = chr((ord(char) + shift - 26))
            result += shifted_char
          
        else:
            result += char
            
    return result

print(Ccipher("!YELLow.", 31))