#! /usr/bin/python3
import cgi
import cgitb
# Note to Self: Make sure to convert any numbers back to it's respective comma form
cgitb.enable()
print('Content-type: text/html\n')
form = cgi.FieldStorage()
def main():
    answers = [form.getvalue("Locations"), form.getvalue("Beds"), form.getvalue("Baths")]
    empty = {}
    data = open("Sheet1.csv", "r").read().split("\n")
    houses = data[1:]
    for i in houses:
        empty[i.split(",")[0]] = i.split(",")[1:]
    print("<html>")
    for key, value in empty.items():
        if all(x in value for x in answers):
            print(key, value, "<br>")
    print("</html")

if form.getvalue("Press_me") == "Test":
    main()
