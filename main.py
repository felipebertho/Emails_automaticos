import yagmail
import os
import time

sender = 'fhbertho@gmail.com'
receiver = 'felipebertho@icloud.com'

subject = "This is a Test"

contents = "Here is the content"

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)

print("E-mail sent!")