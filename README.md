# smartchatappfrom smart_details import chatapp,chatmessages,defaultuser,friends


from steganography.steganography importsteganography

from date_time import datetime
from colored import fg,bg,attr

import easygui


easygui.messagebox("<:-------------------------------------------:>/n<:---------hello:>/n welcome to spy chat lets get started")
easygui.messagebox("now you can chat with your friends \n all your chats are encrypted")
STATUS_MESSAGE=['Bussy','sleeping','at work','studing','movie']
import csv

def load_friends():
    with open ('friend.csv','rb')as friend_data:
        reader = csv.read(friend_data)

        for row in reader:
            vchat=vchat(row[0],row[1],row[2],row[3])
            friend.append(vchat)


def start_chat(defaultuser):
    show_menu=True
    current_status_message=None
    while show_menu== True:
        print"%s%s\n you can be able to perform follong tasks using this chat app" %(fg(41,bg(161))

        menu_choice='1:status update   \n   2:add a friend \n 3:select a friend    \n 4:send  a secret messege  \n 5:read a secret messege   \n  6:read chat from a user  \n 7:close app  %s%s'%attr(0)

        menu_choice=raw_input(menu_choices+"enter your choice from the above list ")


        if menu_choice>0:

            menu_choice=int(menu_choices)
            if menu_choice ==1:
                print 'you wanted to update a status'
                current_status_messege=add_status(current_status_message)


            elif menu_choice == 2:
                print'you wanted to add a friend'
                number_of_friend=add_friend()
                print'you are connected with %d people through this app which are \n'%(number_of_friends)




    elif menu_choice== 3:
        print'you wanted to select a friend'
        select_friend


    elif menu_choice==4:
        print'you wanted to send a secrete message'
        send_secrete_messege()



    elif menu_choice==5:
        print'you wanted to read a message'
        read_secrete_message()



    elif menu_choice==6:
        print'you wanted to read a chat'



    elif menu_choice==7:
        print'you wanted to close the app'
        close_app = "are you sure?(y/n)"
        close_app=raw_input(close_app)


        if close.upper=='y':
            show_menu==False
            exit()
    else:
        print"\t Select the Valid option from the list"




def add_status(current_status_message)
    update_status_message=None

    if defaultuser.current_status_message != None:
        print'your current status is '+defaultuser.current_status_message +"\n"

    else:
        print'you do not have any status message currently \n'


    default = raw_input("\n do you want to add from old status (y/n)")
    if default.upper()== "n":
        new_status_message = raw_input("write a new message:")
        if len(new_status_message)>0:
            STATUS_MESSAGE.append(new_status_message)



            update_status_message=new_status_message
            print"now your status is:'"+update_status_message+" '\n"
            defaultuser.current_status_message = update_status_message
        else:
            print'please enter a valid status'
        elif default.upper()="y" :
        item_position = 1



        for message in STATUS_MESSAGE:
            print str(item_position)+"."+str(message)

            item_position=item_position+1
            message_selection = int(raw_input("\nchose from the above status:"))

            if len(STATUS_MESSAGE)>=message_selection:
                updated_status_message = STATUS_MESSAGE[message_selection-1]
            else:
                print'PRESS y or n only'
                if updated_status_message:
                    print'now your status is'+" "+update_status_message+'\n'
                    defaultuser.current_status_message=updated_status_message
                else:
                    print "you do not have any current status"




def add_friend():
    new_friend={
        'name':''
        'salutation':''
        'age':0,
        'rating':0.0


    }
    new_friend.name=raw_input('enter your friends name:')
    new_friend.salutation=raw_input('what we can call you:Mr/Miss')
    new_friend['name']=new_friend['salutation']+' '+new_friend['name']
    new_friend['age']=input('your age'+' '+new_friend['name'])
    new_friend['rating']=input('give your rating')


    if len(new_friend.name)>0 and (new_friend.age)>12 and (new_friend.rating)>=1

        friend.append(new_friend)
        print'new firnd"%s"age "%d"  of rating "%.2f"  add into friend list.'%(new_friend.name,new_friend.age,new_friend.rating)

    else:
        print'invalid entry!!\n we can not add a friend with these details'
        return len(friends)
    def select_friend():
        def view_friend():
            item_number = 0


            for friend in friends:
                print"%d.%s age %d rating %0.2f is online"%(item_number+1),friend.name,friend.age,friend.rating)


                item_number = item_number+1

                view_friend()
                friend_choice=raw_input("select a friend from friend list:/t")
                friend_choice_position= int (friend_choice)-1

                return friend_choice_position


def send_message():
    friend_choice=select_friend()
    original_image=raw_input('which image file the secrete message is to be hiden?(enter image file name without any extension)')

text = raw_input("Type Your Secure Message Now: \t")
Secured_image = raw_input("Enter Name (without extension .jpg) For Newly Generated Secure Message File : \t")

output_path = Secured_image + '.jpg'
Steganography.encode(original_image, output_path, text)

temp = text.split(' ')

special = ['SOS', 'sos' 'Help', 'help', 'HELP', 'Save', 'SAVE', 'save']
for any in special:
if any in temp:
temp[temp.index(any)] = ' Please Help Me. i am In Denger. Contact me as soon as Possible'

text = str.join(' ', temp)

new_chat = {
"message": text,
"time": datetime.now(),
"sent_by_me": True
}
friends[friend_choice].chats.append(new_chat)
print '\n\tYour secret message is ready! in File " %s "' %output_path

def read_message():
sender = select_friend()
output_path = raw_input("\nEnter the Secure Image File Name (without any extension Like .jpg) To Read Your Secure Message: \t")+".jpg"
try:
secret_text = Steganography.decode(output_path)
except ValueError:
print "\tNo Any Secret Message In This Image. Please Try Another Image File \n"
read_message()

print 'The Secret message For You "'+ secret_text +' ".'

print'----------------------lets get started------------------------------------'

question = "\nContinue as " + defaultuser.salutation + " " + defaultuser.name + "(Y/N)? \t"
existing = raw_input(question)

if existing.upper() == 'Y':

defaultuser.name= defaultuser.salutation + ' ' + defaultuser.name
print "\nWelcome " + defaultuser.name + ". Glad to have you back with us."
AskForPassword = defaultuser.name + " Please Enter your password: \t"
password = raw_input(AskForPassword)

if password == "" :

print "\nAuthentication Complete. Welcome %s Age: %d and Rating of: %.1f Proud to have you onboard." % (defaultuser.name, defaultuser.age, defaultuser.rating)
print "Now You Can Start Chat with your Friends."

start_chat(defaultuser)

else:
print "\n\t Please Enter Correct password. and Try again"
easygui.msgbox("Please Enter Correct password", 'password Issue', ("Close"))

elif existing.upper() == "N":


newuser = vchat('','',0,0.0)

newuser.name = raw_input("\nYou must tell me your Smart Name First: \t")

if len(newuser.name) > 0:

newuser.salutation = raw_input("Should I call you (Mr. or Ms.) ? \t")

newuser.name = newuser.salutation + ' ' + newuser.name
print "Alright " + newuser.name + ". I\'d like to know a little bit more about you before we proceed..."

newuser.age = input("What is your age? \t")

if newuser.age > 12 and newuser.age < 50:

newuser.rating = input("What is your Smart Rating? \t")
if newuser.rating > 4.5 :
print 'Great ace!'
elif newuser.rating > 3.5 and newuser.rating <= 4.5 :
print 'You are one of the good ones.'
elif newuser.rating > 2.5 and newuser.rating <= 3.5 :
print 'You can always do better'
else:
print 'We can always use somebody to help in the office.'
newuser.is_online = True

print "\nAuthentication Complete. Welcome %s Age: %d and Rating of: %.1f Proud to have you onboard." % (newuser.name, newuser.age, newuser.rating)
print "\t Now You Can Start Chat with your Friends."

start_chat(newuser)

else:
print "\t Sorry you are not of the correct age to be a Smart VChat User"

else:
print "\t A Smart User needs to have a valid name. Try again please."

else:
print "\t Please Select Only (Y/N) and Try Again"
