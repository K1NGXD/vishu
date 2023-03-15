from urllib import response
import mechanize
import os
import datetime
import sys
from time import sleep
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def sp(stri):
    for letter in stri:
        print(letter, end = "")
        sys.stdout.flush()
        sleep(0.03)

def login():
    browser.open(url)
    browser.select_form(nr = 0)
    browser.form['email'] = USERNAME
    browser.form['pass'] = PASSWORD
    r = browser.submit()
    f = open("login.html", "wb")
    f.write(r.read())
    f.close()
    browser.select_form(nr = 0)
    print("\033[1;33;40m", end = "")
    sp("\nEnter the 2 factor code by google authenticator :\n")
    print("\033[1;37;40m")
    apr = str(input())
    try:
        browser.form['approvals_code'] = apr
    except mechanize._form_controls.ControlNotFoundError:
        print("Wrong password or some shit, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    browser.select_form(nr = 0)
    try:
        browser.form['name_action_selected'] = ['save_device']
    except mechanize._form_controls.ControlNotFoundError:
        print("Some shit gone down, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    f = open("full_login_" + str(USERNAME) + ".html", "wb")
    f.write(r.read())
    f.close()

def findtextchat(curl):
    r = browser.open(curl)
    x = browser.title()
    if x == "Review recent login":
        print("\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.")
        exit(1)
    if x == "Login approval needed":
        print("\nYour account is stuck on verification\nPlease do it and then re run the program.")
        exit(1)
    if x == "Epsilon":
        print("\nbhai tera khud gya.ja unlock kar")
        exit(1)

def sendtextconvo(comment):
    try:
        browser.select_form(nr = 1)
    except mechanize._mechanize.FormNotFoundError:
        print("oh shit somthing worng on your account plz")
        exit(1)
    try:
        browser.form['body'] = comment
    except mechanize._form_controls.ControlNotFoundError:
        print("hey bro something worong plz first you can login your account on mbaisc fb thanku any any problem then you contact vishu rajput")
        exit(1)
    r = browser.submit()
    e = datetime.datetime.now()
    print("\033[1;32;40m", end = "")
    print (e.strftime("%d/%m/%Y   %I:%M:%S %p"))
    print(">>", line, "\n")

print("\033[1;33;40m", end = "")
sp("\nEnter your email :\n")
print()
print("\033[1;37;40m")
USERNAME = str(input())
print("\033[1;33;40m", end = "")
sp("\nEnter your password :\n")
print("\033[1;37;40m")
PASSWORD = str(input())
login()
print("\033[1;34;40m", end = "")
sp("Enter Convo or ib:\n")
print("\033[1;37;40m")
cid = str(input())
curl = 'https://m.facebook.com/messages/t/' + str(cid)

print("\033[1;34;40m", end = "")
sp("file dal de bhai notepade wali :")
print("\033[1;37;40m")
np = str(input())
f = open(np, 'r')
lines = f.readlines()
f.close()
print("\033[1;33;40m", end = "")
sp("Enter the time delay in seconds :\n")
print("\033[1;37;40m")
t = int(input())

clear()

count = 0
while True:
    for line in lines:
        if len(line) > 3:
            if count != 0:
                sleep(t)
            findtextchat(curl)
            sendtextconvo(line)
            count += 1
            if count % 10 == 0:
                sleep(1)
                clear()
                print("\033[0;37;41m\n")
                
