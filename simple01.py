from datetime import datetime

cronFile = open("Cron.txt", "a+")
cronFile.write("Cron is called at: " + str(datetime.now()) + "\r\n")
cronFile.close()