import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Hi (username), Time to be hydrated",
            message = "Drinking enough water each day is crucial for many reasons: to regulate body temperature, keep joints lubricated, prevent infections, deliver nutrients to cells, and keep organs functioning properly. Being well-hydrated also improves sleep quality, cognition, and mood.",
            app_icon = r"path for icon.ico",
            timeout = 60
        )
        time.sleep(1200)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
