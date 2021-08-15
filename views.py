from flask import Flask, Response, request
import requests
from func import getEvent
from func import getEvent, getLinkEvent, getEmojiEvent
import time

TOKEN = "1931714918:AAEM7ih6Lp_gX01vsHQPYKPsVvxUKh0rFgY"
EVENT = ""
TELEGRAM_INIT_WEBHOOK_UR = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://80ef18d18240.ngrok.io/message"
requests.get(TELEGRAM_INIT_WEBHOOK_UR)
app = Flask(__name__)


@app.route("/message", methods=["POST"])
def handle_message() -> Response:
    """
    get the massage from the user and return a response
    :return: response
    """
    chat_id = request.get_json()["message"]["chat"]["id"]
    if(request.get_json()["message"]["text"] == "/start"):
        myrequest("היי!!\n אם נכנסת לכאן, מסתבר שמגיע לאחד המכרים שלך מזל טוב!\n צדקנו?? בוא נמשיך...לחבר שלך יש יום הולדת? הבנדוד מתחתן?? נמאס לך לחפור באינטרנט למציאת ברכת איחולים מתאימה? נמאס לך לכתת רגליים למציאת מתנה שתשמח אותו? הגעת למקום הנכון!!\nשתף אותנו בסוג האירוע המבוקש, ונארגן עבורך 'ערכה' מתאימה הכוללת ברכה, קישור לאתר מתנות הקשורות לאירוע שם תוכל למצוא מתנה מתאימה, ורשימת אימוג'ים המתאימים לסוג האירוע, אותם תוכל לשלב בברכה או סתם לשלוח לחבר....\nיאלהה לעבודה...תהנהה!!!\n(נא להכניס סוג אירוע: יום הולדת/חתונה/לידה/יציאה לפנסיה", chat_id)
    global EVENT
    if (request.get_json()["message"]["text"] == "לא"):
        myrequest("אנחנו מתנצלים על אי הנעימות\nהבוטי שלנו מציע מגוון רב של ברכות, עד שהלקוח מרוצה!\nאז בוא ננסה שוב!", chat_id)
        myrequest(getEvent(EVENT), chat_id)
        myrequest("האם אהבת את הברכה שהצענו לך?\nנא לענות בכן ולא.", chat_id)
    elif (request.get_json()["message"]["text"] == "כן"):
      myrequest("איזה כיף!!\nכעת נצרף לך קישור לאתר מתנות "+EVENT+" ורשימת אימוג'ים מגניבים שמתאימים ל"+EVENT, chat_id)
      myrequest(getLinkEvent(EVENT), chat_id)
      myrequest(getEmojiEvent(EVENT), chat_id)
      myrequest("יאלה..לך תפנק במתנה שווה!\nאל תהיה קמצן...\n נשמח לראות אותך שוב איתנו בעוד המון אירועים\n  שיהיה במזל טוב!!\n ", chat_id)
    elif (request.get_json()["message"]["text"] != "/start")and(request.get_json()["message"]["text"] != "לא")and(request.get_json()["message"]["text"] != "כן"):
     EVENT = request.get_json()["message"]["text"]  # get event
     myrequest(getEvent(EVENT),chat_id)#print bless
     if (getEvent(EVENT)!="מצטערים מאד! לא הצלחנו למצוא ברכה מתאימה לאירוע המבוקש"):
      myrequest("האם אהבת את הברכה שהצענו לך?\nנא לענות בכן ולא", chat_id)


    #event =request.de_json(request.get_json(force=True))
    #myrequest(event,chat_id)
    #while (event=="no"):
    #myrequest(getEvent(event), chat_id)
    #text="אני שמח שאהבת את הברכה!!\n כעת נשלח לך קישור לאתר מתנות המתאימות לאירוע שבחרת"

    return Response("Success")

def myrequest(text,chat_id):
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}")

