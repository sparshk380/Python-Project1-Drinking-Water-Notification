import time
from plyer import notification
if __name__ == "__main__":
    notification.notify(
        title = "Please Drink Water",
        message = "The National Academics of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is about 15.5 cups (3.7 litres) of fluids for men. About 11.5 cups (2.7 litres) of fluids for women.",
        # app_icon="D:\\WorkSpace\\Python\\icon.png",
        timeout=5
    )
