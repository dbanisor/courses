''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.
Here are the steps you can take to automate this process:
    Use the smtplib library to connect to the email server and send the emails.
    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.
    Use the os library to access the report files_to_upload that need to be sent.
    Use a for loop to iterate through the list of recipients and send the email and attachment.
    Use the schedule library to schedule the script to run daily at a specific time.
    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''
import pathlib
import smtplib
from email.message import EmailMessage
import os
import schedule
import time
import datetime as dt
import mimetypes

log_file = r'C:\Users\Denis\PycharmProjects\Kreativstorm training\session_3\session_3_tema\log_file.txt'
now = dt.datetime.now()

#--------------------------------------------UPDATE LOG FILE--------------------------------------------#
def update_log_file(*args):
    with open(log_file, 'a') as file:
        for arg in args:
            file.writelines(f'{now} --------- {arg}\n')

#-----------------------------------------------USER LOGIN-----------------------------------------------#
def send_email(to_user):
    sender = 'denise.banisor@outlook.com'
    sender_pass = os.environ.get('MYEMAIL')

#--------------------------------------------------EMAIL-------------------------------------------------#
    message = EmailMessage()
    message['From'] = sender
    message['To'] = to_user
    message['Subject'] = 'Hello!'
    body = """Your report is enclosed.
    
    Have a good day!"""
    message.set_content(body)

#----------------------------------------------ATTACHMENT-----------------------------------------------#
    attach_path = r'C:\Users\Denis\PycharmProjects\Kreativstorm training\session_3\session_3_tema\Untitled form(1-5000) (1).xlsx'
    attach_name = os.path.basename(attach_path)
    mime_type, _ = mimetypes.guess_type(attach_name)
    mime_type, mime_subtype = mime_type.split('/', 1)

    try:
        with open(attach_path, 'rb') as file:
            message.add_attachment(
                file.read(),
                maintype=mime_type,
                subtype=mime_subtype,
                filename=attach_name
            )
    except Exception as exc:
        message = f'ERROR. This error occured while trying to find the attachement:\n\t\t{exc}\n\n'
        update_log_file(message)

#----------------------------------------------SEND EMAIL-----------------------------------------------#
    try:
        mail_server = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        mail_server.starttls()
        mail_server.login(sender, sender_pass)
        mail_server.send_message(message)
    except Exception as exc_2:
        message = f'ERROR. This error occured while trying to find the attachement:\n\t\t{exc_2}\n\n'
        update_log_file(message)
    else:
        mail_server.quit()
        message = f'Report sent successufully to: {to_user}'
        update_log_file(message)

#-------------------------------------ITERATING THROUGH USERS------------------------------------------#
def run_app():

    receivers = ['preda.deniseramona@gmail.com', 'denise.banisor@gmail.com']

    for user in receivers:
        send_email(user)

#--------------------------------------------SCHEDULER------------------------------------------------#
schedule.every().day.at('22:20').do(run_app)


while True:
    schedule.run_pending()
    time.sleep(1)