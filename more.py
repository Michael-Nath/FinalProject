#! /usr/bin/python3
import cgi
import cgitb
import io
cgitb.enable()
print('Content-type: text/html\n')
form = cgi.FieldStorage()

def more():
    print("<html>")
    file = io.open('houses.txt', 'r', encoding='utf-8')
    read = file.read().split("\n")
    file.close()
    joined = ("").join(read).split("\n")
    house = form.getvalue("house")
    something = form.getvalue("text")
    print(something)
    print(house)
    print("hi")
    print("</html>")

if form.getvalue("submit") == "Submit!":
    more()