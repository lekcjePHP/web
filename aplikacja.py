import web 
from random import randint

plik = open("test.html", "r").read()
strony = web.template.render("templates/")

urls = ( 
        '/', 'index',
        '/kontakt', 'kontakt',
        )
"""
localhost/ -> index
localhost/kontakt -> kontakt
"""
class index:
    def GET(self):
        return plik


class kontakt:
    def GET(self):
        kontakty = ["rucho@as.pl", "zdzicho@as.pl", "wojtek@as.pl", "bacha@as.pl", "kacha@as.pl"]
        liczba = randint(0,4)
        liczba2 = randint(0,4)
        mail = kontakty[liczba]
        mail2 = kontakty[liczba2]
        return strony.contact(mail,mail2)

if __name__ == '__main__' :
    app = web.application(urls, globals())
    app.run()


