import random
import main

def getEvent(event):
    if event not in main.blesses:
        return "מצטערים מאד! לא הצלחנו למצוא ברכה מתאימה לאירוע המבוקש"
    b=random.choice(main.blesses[event])
    return (b.bless)
def getLinkEvent(event):
    if event not in main.links:
        return "there is no blesses for this event"
    return random.choice(main.links[event])

def getEmojiEvent(event):
    if event not in main.emoji:
        return "there is no blesses for this event"
    r = random.sample(main.emoji[event], 3)
    return (r[0][:-1]+" "+ r[1][:-1]+" "+r[2][:-1])
