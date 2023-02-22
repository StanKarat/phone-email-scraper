#! python3

import re, pyperclip


#create regex for phone numbers
phoneRegex = re.compile(r'''
# 123-456-7890, 456-7890, (123) 456-7890, 456-7890, 456-7890 ext 12345, ext. 12345, x12345

((
((\d\d\d)|(\(\d\d\d)))?  #area code 
(\s|-)                   #first separator
\d\d\d                   # first 3 digits
-                        #separator
\d\d\d\d                 #last 4 digits
(((ext(\.)?\s|x)         #extention word part
(\d{2,5}))?              #extention number-part
))


''',re.VERBOSE)



# Create regex for emails
emailRegex = re.compile(r'''

# dummyemail.+_haha@notgoogle.com

[a-zA-Z0-9_.+]+    #name part
@    # @ symbol
[a-zA-Z0-9_.+]+    # domain name part

''', re.VERBOSE)



# get the text off the clipboard
text = pyperclip.paste()

# extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allphonenumbers = []
for phonenumber in extractedPhone:
    allphonenumbers.append(phonenumber[0])

#copy the exctracted email/phone to the clipboard
results = '\n'.join(allphonenumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
