import smtplib
import mimetypes
import email
import email.mime.application
import os
import random
from os import walk

def findAttachment():
	# return random attachment from the given directory
	print "Looking for attachment. . ."

	attachments = os.getcwd() + "/photos"
	f = []

	for (dirpath, dirnames, filenames) in walk(attachments):
		f.extend(filenames)
		break

	fileName = random.choice(f)

	print "Choosen attachment: " + fileName

	return fileName


def sendMail():
	# send mail rofl
	print "Sending mail to gf. . ."

	gf = "" # careful
	me = "" # careful

	server = smtplib.SMTP("smtp.gmail.com:587")
	server.ehlo()
	server.starttls()
	server.login(me, "") # careful


	msg = email.mime.Multipart.MIMEMultipart()
	msg["Subject"] = "ivanica-motivator: Motivacija za dobro jutro"
	msg["From"] = me
	msg["To"] = gf

	body = email.mime.Text.MIMEText("""
		You got this.

		:*
	""")
	msg.attach(body)

	# attachment
	attachmentName = findAttachment()
	fp = open("photos/" + attachmentName, "rb")
	att = email.mime.application.MIMEApplication(fp.read(), _subtype = "jpg")
	fp.close()

	att.add_header("Content-Disposition","attachment", filename = attachmentName)
	msg.attach(att)
	server.sendmail(me, gf, msg.as_string())

	# delete file from folder
	os.remove(os.getcwd() + "/photos/" + attachmentName)

	server.quit()

	print "Success!"


def main():
	print "Starting script. . ."
	sendMail()

main()