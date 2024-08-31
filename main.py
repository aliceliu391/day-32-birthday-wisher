import pandas
import datetime as dt
import random
import smtplib


def write_new_letter():
    """Write a new, personalized email from one of the email templates"""
    with open(random.choice(email_templates)) as file:
        letter_template = file.read()
        complete_letter = letter_template.replace("[NAME]", str(name))
        return complete_letter


# Email Details
my_email = "your_email@gmail.com"
password = "your_password"

birthdays = pandas.read_csv("birthdays.csv")
birthday_data = pandas.DataFrame(birthdays)
email_templates = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
current_date = (dt.datetime.now().month, dt.datetime.now().day)

for (key, row) in birthday_data.iterrows():
    birthday = (row.month, row.day)
    name = row["name"]
    email = row.email

    # Send birthday email to someone if it is their birthday
    if current_date == birthday:
        new_letter = write_new_letter()
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # Makes connection secure
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: HAPPY BIRTHDAY!\n\n{new_letter}")
