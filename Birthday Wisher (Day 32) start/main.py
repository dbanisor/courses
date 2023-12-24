# import smtplib
#
# my_email = "contnouy22@yahoo.com"
# password = "winskzundhnmfmrz"
#
# with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="contnoug22@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
#
import smtplib
import datetime as dt
import random

MY_EMAIL = "contnoug22@gmail.com"
MY_PASSWORD = "Beberech123"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )











