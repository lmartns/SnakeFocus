from plyer import notification
from playsound import playsound

def notify(message, sound_file):
    notification.notify(
        title='Pomodoro Timer',
        message=message,
        timeout=10
    )
    playsound(sound_file)
