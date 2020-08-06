'''
random chore assignment emailer

take a list of email adddresses and random chores that need to be done
randomly assign chores to people

'''

import smtlib, random, time

# user information
user_email = 'yourEmailAddress@yourEmailHost.com'
user_pw = 'ALIENSAREREAL'

# list of email addresses
emails = ['email_1@emailHost.com', 'email_2@emailHost.com',
          'email_3@emailHost.com', 'email_4@emailHost.com']

# function to assign chores

def assignChores():
    chores = ['Wash dishes', 'Mop floor', 'Feed cat',
              'Clean toilet', 'Mow lawn', 'Clean kitchen']
    
    for email in emails:
        randomChore = random.choice(chores)
        email_dictionary[email] = randomChore
        chores.remove(randomChore)
        
    for email in email_dictionary:
        message = str('Subj: Your random chore is \n' + email_dictionary[email])
        print(email.ljust(27) + 'is assigned: ' + email_dictionary[email].rjust(23))
        stmpObj.sendmail(user_email, email, message)
     
# empty dictionary to collect emails with chores
email_dictionary = {}

# logging into smtp server - !!! your settings may differ !!!
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(user_email, user_pw)

# calling function to send mail every week
for i in range(7):
    assignChores()
    time.sleep(864000) # sleep for 24 hours

# log out
smtpObj.quit()

   





