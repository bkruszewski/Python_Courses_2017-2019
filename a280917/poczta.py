import smtplib
from a280917 import secrets

adresat = secrets.login
nadawca = secrets.login
haslo = secrets.haslo

#tworze silnik mailera

mailer = smtplib.SMTP("smtp.gmail.com", 587)
# witam sie z serwerem/ lacze sie
mailer.ehlo()
#szyfruje polaczenie
mailer.starttls()
#loguje sie
mailer.login(nadawca, haslo)

temat = "Subject: Hello from Bolek\n"
wiadomosc = "To jest wiadomosc"
tresc = temat + wiadomosc

#wysylam
mailer.sendmail(nadawca, adresat, tresc)
print("Wyslano maila")

mailer.close()