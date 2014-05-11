import smtplib
import subprocess
import string

p = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)

MSG = p.stdout.read()
FROM = "guru-python-sysadmin@server.com"
TO = "ivan.jimenezster@gmail.com"
SUBJECT = "Nightly Disk Usage Report"

msg = string.join(("From: %s" % FROM, "To %s" % TO, "Subject: %s" % SUBJECT, "", MSG), "\r\n")
server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()
server.ehlo()

server.login("ivan.jimenezster","")
server.sendmail("ivan.jimenezster@gmail.com", "ivan.jimenezster@gmail.com", msg)
server.quit()