
####incomplete
from plyer import notification #importing notification class from plyer module
import time
while (True):
    notification.notify (title= "INTERNSHIP", message= " The deadline for Internship application ends tonight",
                         app_icon="icon.ico", timeout="10") #calling notify method of notification class
    time.sleep(10)