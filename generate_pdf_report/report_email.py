#!/usr/bin/env python3

import reports
import emails
import os
from datetime import date

BASEPATH_TEXT_DES = os.path.split(os.getcwd())[0] + "/assets/txtfiles/"
list_text_files = os.listdir(BASEPATH_TEXT_DES)

report = []


def process_data(data):
    for item in data:
        report.append("title: {}<br/>name: {}\n".format(item[0], item[1]))
    return report


text_data = []
for text_file in list_text_files:
    with open(BASEPATH_TEXT_DES + text_file, 'r') as f:
        text_data.append([line.strip() for line in f.readlines()])
        f.close()

if __name__ == "__main__":
    summary = process_data(text_data)

    # Generate a paragraph that contains the necessary summary
    paragraph = "<br/><br/>".join(summary)

    # Generate the PDF report
    title = "Processed Update on {}\n".format(date.today().strftime("%B %d, %Y"))
    attachment = os.path.split(os.getcwd())[0] + "/assets/processed.pdf"

    reports.generate_report(attachment, title, paragraph)

    # Send the email
    subject = "Upload Completed - Online Articles"
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "All Articles are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
