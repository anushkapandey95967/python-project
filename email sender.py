from email.message import EmailMessage
import ssl
import smtplib

email_sender='anushkapandeypwn@gmail.com'
email_password='bdnq rgxl gpdd iruv'

email_receiver='kenijo9164@seosnaps.com'

subject='project completion remainder'
body="""with due regards i want to say that please completeyour project till 16 march and 
submit it on time  """

em = EmailMessage()
em['FROM']=email_sender
em['TO']=email_receiver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())