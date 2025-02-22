'''
Your users' passwords were all stolen in the Yahoo! hack,
 and it turns out they have been lax in creating secure passwords. 
 Create a function that checks their new password (passed as a string) 
 to make sure it meets the following requirements:

    Between 8 - 20 characters
    Contains only the following characters (and at least one character from each category):
    uppercase letters,
    lowercase letters,
    digits,
    special characters from !@#$%^&*?

Return "valid" if passed or "not valid" otherwise.

'''

# Hello

def check_pass(password_str: str) -> bool:
    # return len(password_str) > 8 and len(password_str) < 20
    # return 8 < len(password_str) < 20
    if len(password_str) < 8 or len(password_str) > 20:
        return False
    
    # has_upper = False
    # has_lower = False
    # has_digit = False
    # has_special = False
    has_upper = has_lower = has_digit = has_special = False
    
    for symbol in password_str:
        if symbol.isupper():
            has_upper = True
        
        if symbol.islower():
            has_lower = True

        if symbol.isdigit():
            has_digit = True

        # if symbol == '!' or symbol == '@'
        if symbol in '!@#$%^&*?':
        # if symbol in ['!', '@']
            has_special = True
        
        if not symbol.isupper() or not symbol.islower() or not symbol.isdigit() or not (symbol in '!@#$%^&*?'):
            return False

    return has_upper and has_lower and has_digit and has_special
    
def check_password(password_str: str) -> str:
    # if check_pass(password_str):
    #     return 'valid'
    # return 'not valid'

    return 'valid' if check_pass(password_str) else 'not valid'
    # check_pass(password_str) ? 'valid' : 'not valid'

# print('!' in '!@#$%^&*?')

# assert check_pass("A!!!!!!!") == False
# assert check_pass("Aaaaaaa7@") == True # Valid
# assert check_pass("Aaaaaaa71") == False
# assert check_pass("Aaaaaaa!@") == False
# assert check_pass("Aa!7") == False


# assert check_password("Aaaaaaa7@") == 'valid'

';fh1%-zcBDH7I'
assert check_pass(';fh1%-zcBDH7I') == False
