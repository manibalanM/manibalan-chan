from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import speech
import imaplib

fromadd = "mmanibalan2@gmail.com"

def send():   
    speech.voice("To whom")
    a = speech.speech()
    print("done")
    speech.voice("mail")
    body = speech.speech()
    print("done")
    msg = MIMEMultipart()
    msg["From"] = fromadd
    msg["To"] = a
    msg["Subject"]="Senf by manibalan"
    msg.attach(MIMEText(body,"plain"))
    mail = msg.as_string()
    server = smtplib.SMTP("smtp.gmail.com","587")
    server.ehlo()
    server.starttls()
    server.login(fromadd,"findmeufuck")
    server.sendmail(fromadd,a,mail)
    server.quit()
   
def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com","993")
        mail.login(fromadd,'findmeufuck')
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print ('From : ' + email_from + '\n')
                    print ('Subject : ' + email_subject + '\n')

    except Exception as e:
        print (str(e))
if __name__ == "__main__":
    read_email_from_gmail()
