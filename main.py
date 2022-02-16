from email import message
from socket import timeout
import time
from turtle import title
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(title='Open Vscode to finish off your practise projects', message='You have to practise to get better and better and better and better and better and better ...', timeout=10)
        time.sleep(60*60)


#  You can add an icon as well by simply writing in notification.notify (app_icon = "The icons directory")

