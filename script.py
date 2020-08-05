import smtplib,getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("""
     ________  ___ _____   _____                                           
/  ___|  \/  |/  ___| /  ___|                                          
\ `--.| .  . |\ `--.  \ `--. _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
 `--. \ |\/| | `--. \  `--. \ '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
/\__/ / |  | |/\__/ / /\__/ / |_) | (_| | | | | | | | | | | |  __/ |   
\____/\_|  |_/\____/  \____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                            | |                                        
                            |_|                                        

    * Before you begin make sure you create a throwaway gmail account to use with this script and make sure you turn on less secure apps on.
    or you can use your account gmail account at your own risk.
    * In order to find smsgateway and carrier of the target person you can use the following website (https://freecarrierlookup.com/)
    * in the number tab use the input like following number@smsgateway example: XXX-XXX-XXXX@tmomail.com
    * GMAIL Sending limit is 500 you can't send 500 messages using gmail smtp in one go.

    """)


your_email = input('Enter Your Email: ')
your_password = getpass.getpass('Enter Password: ')
target = input("Enter target's number with sms-gateway: ")
your_msg = input('Enter your message or gif link: ')
number = int(input('How many texts would you like to send: '))

def mail_server(email,sms_gateway,text):
    email = your_email
    pas =  your_password
    smtp = 'smtp.gmail.com'
    port = 587
    server = smtplib.SMTP(smtp,port)
    server.starttls()
    server.login(email,pas)
    server.sendmail(email,sms_gateway,text)
    server.quit()

def send_text(text):
    msg = MIMEMultipart()
    email = your_email
    sms_gateway = target
    msg['From'] = your_email
    msg['To'] = target
    msg['Subject'] = "SMS SPAMMER"
    body = your_msg
    msg.attach(MIMEText(body, 'plain'))
    sms = msg.as_string()
    mail_server(email,sms_gateway,sms)



for nums in range(0,number):
    send_text(your_msg)
    print(f'SENDING TEXT {nums}')
