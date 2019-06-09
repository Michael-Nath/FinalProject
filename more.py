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
    info = io.open("more.html", "r", encoding='utf-8')
    read_info = info.read()
    read = file.read().split("\n")
    file.close()
    info.close()
    joined = (" ").join(read)
    house = form.getvalue("house")
    read_info += "<div class='info'>" + joined[joined.find(house) + len(house):joined.rfind(house)] + "</div>"
    read_info += "</div> </html>"
    print(read_info)

if form.getvalue("submit") == "See More!":
    more()