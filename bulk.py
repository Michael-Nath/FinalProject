#! /usr/bin/python3
import cgi
import cgitb
# Note to Self: Make sure to convert any numbers back to it's respective comma form
cgitb.enable()
print('Content-type: text/html\n')
form = cgi.FieldStorage()
def main():
    empty = {}
    data = open("houses.csv", "r").read().split("\n")
    houses = data[1:]
    for i in houses:
        empty[i.split(",")[0]] = i.split(",")[1:]
    print("<html>")
    for key, value in empty.items():
        if form.getvalue("Locations") in value:
        print(key, value, "<br>")

    print("</html")
if form.getvalue("Press_me") == "Test":
    main()