import smtplib, ssl

port = 1025  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL('localhost', port, context=context) as server:
    server.login("my@gmail.com", password)
    # TODO: Send email here
