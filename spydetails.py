# Import Date and time
from datetime import datetime
class vchat:
# Constructor for initializing class
def __init__(self, name, salutation, age, rating):
self.name = name
self.salutation = salutation
self.age = age
self.rating = rating
self.is_online = True
self.chats = []
self.current_status_message = None
self.chats_avg = [0,0]
# Default user for Smart vchat uses
defaultuser = vchat('mahima saxena', 'Ms.', 20, 4.7)
#
friend_one = vchat('himani joshi', 'Ms.', 22, 4.9)
friend_two = vchat('harshi saxena', 'Ms.', 18, 4.39)
friend_three = vchat('kiran Kaur', 'Ms.', 22, 3.95)
friend_four = vchat('vaibhav Srivastava', 'mr.', 25, 4.5)
friend_five = vchat('tanya bist', 'Ms.', 23, 4.95)
friends = [friend_one, friend_two, friend_three, friend_four, friend_five]
class ChatMessage:
def __init__(self, message, sent_by_me):
self.message = message
self.time = datetime.now()
self.sent_by_me = sent_by_me
# v_name = "mahima saxena"
# v_salutation = "Ms"
# v_age = 20
# v_rating = 4.5
# all details in the form of Dictonary
