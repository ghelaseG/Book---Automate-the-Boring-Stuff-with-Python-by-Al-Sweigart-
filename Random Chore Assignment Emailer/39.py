#python3! - Write a program that takes a list of people’s email addresses and a list
#of chores that need to be done and randomly assigns chores to people.

import smtplib
import random
import time

userEmail = 'youreemailaddres@email.com' #change your email and password here
userPw = 'yourpassword'

emails = ['email1@yahoo.com', #list of emails addresses - edit
          'email2@yahoo.com',
          'email3@gmail.com',
          'email4@gmail.com']

def assignment():
    chores = ['Wash the dishes', #function to assign chores and email them
              'Mop the floor',   #to email addresses in the list
              'Walk the dog',
              'Feed the cat',
              'Clean toilet',
              'Mow the lawn',
              'Clean the kitchen']
    for email in emails: #create a for loop that assigns a random chore to the individual
        random_chore = random.choice(chores)
        email_dict[email] = random_chore
        chores.remove(random_chore)
    for email in email_dict: #send the email using smtp and your variables
        message = str('Subject: Your random chore is....\n' + email_dict[email])
        print(email.ljust(27) + ' is assigned: ' + email_dict[email].rjust(23))
        smtp_obj.sendmail(userEmail, email, message)

email_dict = {} #empty dictionary to collect emails with chores

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)  # login into the SMTP server -
smtp_obj.ehlo()                                 # Note:your settings may be different
smtp_obj.starttls()                             # depending on the email you use.
smtp_obj.login(userEmail, userPw)

for i in range(7): #calling the function to send the email every week
    assignment() #the program will sleep for 24 hours and run through a loop for 7 days
    time.sleep(86400)

smtp_obj.quit #logging out of SMTP server
