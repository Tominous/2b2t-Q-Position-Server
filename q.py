import os
import time

#Copy path to your .minecraft folder in place of !here! below
mc_folder = r"!here!"

latest_log = mc_folder + r"\logs\latest.log"

os.startfile(r"C:\Apache24\bin\httpd.exe")

while True:
    with open(latest_log, "rb") as f:
        f.seek(-2, os.SEEK_END)     
        while f.read(1) != b"\n":
            f.seek(-2, os.SEEK_CUR)
        latest = f.readline()
        latest = str(latest)
        if 'CHAT' in latest:
            os.remove(r"C:\Apache24\htdocs\index.html")
            p = open("C:\Apache24\htdocs\index.html","w+")
            p.write("<meta http-equiv='refresh' content='10'><div style='text-align: center;'><h1>" + latest[32:-5] + "</h1></div>")
            p.close()
            print(latest[51:-5])
    time.sleep(0.5)
