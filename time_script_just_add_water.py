import os
import urllib2

os.system("for I in 1 2 3 4; do ssh pi@p$I.local sudo date +%Y%m%d --set='$todays_date'; ssh pi@p$I.local sudo date +%H%M%S -s 12:48:00; done")