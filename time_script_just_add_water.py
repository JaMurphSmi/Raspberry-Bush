import os

todays_date="20180405"
todays_time="12:48:00"

os.system("for I in 1 2 3 4; do ssh pi@p$I.local sudo date +%Y%m%d --set='$todays_date'; ssh pi@p$I.local sudo date +%H%M%S --set='$todays_time'; done")