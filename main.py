
from microbit import *

import random
import speech

set_volume(255)

nice_words = [
    "You are so smart!",
    "Great job!",
    "Well done!",
    "Amazing!",
    "Brilliant!",
    "Fantastic!",
    "Excellent!",
    "Wonderful!",
    "Awesome!",
    "Nice work!",
    "Keep it up!",
    "You did it!",
    "Great thinking!",
    "Good idea!",
    "I believe in you!",
    "You can do it!",
    "Never give up!",
    "Keep learning!",
    "Keep smiling!",
    "You're doing great!",
    "Stay positive!",
    "You're improving every day!",
    "You're awesome!",
    "Have a wonderful day!",
    "You make people smile!",
    "You're a great person!",
    "Keep shining!",
    "You are appreciated!",
    "You are creative!",
    "You are talented!",
    "Be proud of yourself!",
    "You deserve a cookie!",
    "You're a genius!",
    "Gold star for you!",
    "High five!",
    "You're a superstar!",
    "Keep being amazing!",
    "The Yes Machine approves!"
]

too_many_questions = [
    "Too many questions!",
    "Please slow down!",
    "One question at a time!",
    "My brain is overheating!",
    "Question overload!",
    "Give me a break!",
    "Too fast, too many!",
    "I need coffee ☕",
    "Error: too many questions detected!",
    "Please stop asking so much!",
    "I'm thinking... wait... too many!",
    "Calm down with the questions!",
    "System cannot handle this many questions!",
    "Rebooting brain...",
    "Question limit reached!",
    "Try again later!",
    "I can only answer so much!",
    "Whoa! Slow down!",
    "You are asking too much!",
    "Processing... processing... STOP!",
    "Too many questions, please relax!",
    "Ask one thing at a time!",
    "My circuits are confused!",
    "Be nice to the micro:bit 😭"
]
while True:
    if button_a.was_pressed():

        
        if random.randint(0, 1) == 0:
            speech.say(random.choice(nice_words))
        else:
            speech.say(random.choice(too_many_questions))
        