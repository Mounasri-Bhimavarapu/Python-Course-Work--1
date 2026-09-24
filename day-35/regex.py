'''import re 

pattern = r'[0-9]'
text = 'degnan2026'

res = re.match(pattern,text)                     # check first element matches with pattern or not.

print(res.group() if res else "pattern not matched")'''

#----------------------------------------------------------------------

'''import re 

pattern = r'[0-9]'
text = 'degnan2026'                  # checks entire text for pattern.

res = re.search(pattern,text)

print(res.group() if res else "pattern not matched") '''

#---------------------------------------------------------------------------

'''import re 

pattern = r'[0-9]'
text = 'degnan2026'             # gives all the elements that are in in the text which are included in the pattern in LIST form

res = re.findall(pattern,text)

print(res)'''

#----------------------------------------------------------------------------

'''import re 

pattern = r'[0-9]'
text = 'degnan2026'
                                  # gives all values in pattern along eith their index,
                                
res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())'''

#---------------------------------------------------------------

'''import re

pattern  = r'[0-9]{10}'
text = '1234520262'
res = re.fullmatch(pattern,text)            #whole text should match with the pattern.

print(res.group()if res else "pattern not matched")'''

# -----------------------------------------------------------------------------

'''import re

pattern = r'[@,:;_&]'
text = 'java,python@c:flask_mysql&django'

res = re.split(pattern,text)

print(res)'''

#-------------------------------------------------------------------------------

'''import re

pattern = r'[aeiou0-9]'
text = 'java 20 pythonc 10 flask 70 mysql 68 django'

res = re.sub(pattern,"*",text)

print(res)'''

#--------------------------------------------------------------------------

'''import re

pattern = r'h.t'
text = 'hat hood wood loom hit hot '  # checks wheather text starts and ends with the given pattern or not.

res = re.findall(pattern,text)

print(res)'''

# ----------------------------------------------------------------------------------


'''import re

pattern = r'^[a-z]'
text = 'Hat hot wood hand loom'
                                                 # checks weather a pattern is starting with the pattern or not
res = re.findall(pattern,text)

print(res)'''

#----------------------------------------------------------------------------------------------------

'''import re

pattern = r'[a-z]$'
text = 'Hat hot wood hand lood'
                                                 # checks weather a pattern is ending with the pattern or not
res = re.findall(pattern,text)

print(res)'''

#--------------------------------------------------------------------------------------------------

'''import re

pattern = r'ab*'
text = 'a ab abbb abbbbb aaabbbbb aaaaaab'
                                                 # checks weather text have 0/1 pattern match.
res = re.findall(pattern,text)

print(res)'''

#------------------------------------------------------------------------------------------------------

'''import re

pattern = r'^(91|0)'
text = '0987654321'
                                                  # checks weather text have atleast 1 or more pattern match.

res = re.findall(pattern,text)

print(res)'''

#----------------------------------------------------------------------------------------------------------------

'''import re

pattern = r'[A-Za-z0-9]'
text = 'qwerty876dfghjklCVBNM'
                              # no proper sequence need to be followed it just get the values matched within the pattern
res = re.findall(pattern,text)

print(res)'''

 #------------------------------------------------------------------------------------

'''import re

pattern = r'[ae]'
text = 'sdfghaecvbniofg'
                                                  # text should match with exact pattern given.

res = re.findall(pattern,text)

print(res)'''

#----------------------------------------------------------------------------------------------------

'''import re

pattern = r'[0-9]{2}'
text = 'sdfghaecvb56vbn78ndf98niofg'
                                                  # {}used for length.

res = re.findall(pattern,text)

print(res)'''

#-------------------------------------------------------------------------------------------------------

'''import re

pattern = r
text = 'sdfg haecv b358077 6n @iofg'
                                                  # small w  all letters and digits.
                                                  # d gives only digits
res = re.findall(pattern,text)                    # D GIVES ONLY LETTERS
                                                   #S gives other than small s 
                                                   #s gives spaces
print(res) '''                                        # W gives  spaces and special characters


#-------------------------------------------------------------------------------------------------

'''import re

name = input("Enter the name:")
pattern = r'^[A-Za-z]{2,25}( [a-zA-Z]{2,25})+$'

                                                  # text should match with exact pattern given.
res = re.fullmatch(pattern,name)

print( "Valid Name" if res else "Invalid Name")'''

#---------------------------------------------------------------------------------------------

'''import re

email = input("Enter the email:")
pattern = r'^[A-Za-z._0-9]+@[a-zA-Z._0-9]+\.[A-Za-z]{2,}$'

                                                  # text should match with exact pattern given.
res = re.fullmatch(pattern,email)

print( "Valid email" if res else "Invalid email") '''

#-------------------------------------------------------------------------------------------

'''import re

phone = input("Enter the phone:")
pattern = r'^[6-9]\d{9}'

res = re.fullmatch(pattern,phone)

print( "Valid phone" if res else "Invalid phone")'''

#----------------------------------------------------------------------------------------

'''import re

pan = input("Enter the pan:")
pattern = r'^[A-Z]{6}\d{4}[A-Z]{1}'

                                                  # text should match with exact pattern given.
res = re.fullmatch(pattern,pan)

print( "Valid pan" if res else "Invalid pan") '''


'''import re
password =input("Enter the password:")
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%&*?])[A-Za-z\d@$!%&*?]{8,}$'
res= re.fullmatch(pattern,password)

print("Valid password" if res else "Invalid password")'''

import re
username =input("enter the user name:")
pattern = pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[_])[A-Za-z\d_]+$'

res = re.fullmatch(pattern , username)
print("valid name" if res else "Invalid name")













                                                


