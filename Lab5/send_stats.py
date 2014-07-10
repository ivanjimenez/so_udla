import smtplib
import subprocess
import string

p = subprocess.Popen("ls -l", shell=True, stdout=subprocess.PIPE)

fromaddr = 'fromuser@gmail.com'
toaddrs  = 'touser@gmail.com'
msg = p.stdout.read()


# Credentials (if needed)
username = 'punkappstudio'
password = 'abdc.3344'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
