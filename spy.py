
from smart_details import vchat,chatmessages,defaultuser,friends


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


def add_status(current_status_message):
    if current_status_message!=None:
        print'your current status is'+current_status_message+'\n'
    else:
        print'you dont have any status'
    default=raw_input('do you want to select from old status(y/n)?\n')

    if default.upper()=='N':
        new_status_message=raw_input('what do you want to set as your status?')
        if len(new_status_message)>0:
            updated_status_message=new_status_message
            STATUS_MESSAGE.append(updated_status_message)

    elif(default.upper()=='Y'):
        item_position==1
        for message in STATUS_MESSAGE
            print str(item_position)+"  "+message
            print item_position==item_position + 1
        message_selection=input('\nchoose from above')
        STATUS_MESSAGE[current_status_message+1]

if response == "Y":
    # start app
    print'welcome'+spy_salutation+spy_name+str(spy_age)
    start_chat(spy_name,spy_age,spy_rating)
else:
    spy_name = raw_input ('welcome to spy chat tell me your name')

    if len(spy_name)>0:
        print 'welcome'+spy_name+'_glad to see u'
        spy_salutation = raw_input('can i call u Mister or Miss?:')
        spy_name = spy_salutation +"  "+ spy_name
        print 'alright'" "+" "+spy_name+'_lets know more about you before we proceed'
        spy_age=0
        spy_rating=0.0
        spy_age = input ('your age?:')
        if(spy_age<12 and spy_age>60):
            print'invalid age'
        else:
            spy_rating=input('give spy rating')
            if(spy_rating>3.5 and spy_rating<4,7):
                print'work hard'
            elif(spy_rating>=4.7 and spy_rating<=5):
                print'you are awesome'
                print'authentiation complete' + ' welcome' + '_name_' + spy_name + '_age_' + str(spy_age) + '_rating_' + str(spy_rating) + '_glade to have you here'



    else:
        print'spy name cannot be empty try again please'


    spy_is_online = True

start_chat(spy_name,spy_age,spy_rating)



