#! /usr/bin/python3
import cgi
import cgitb
# Note to Self: Make sure to convert any numbers back to it's respective comma form
cgitb.enable()
print('Content-type: text/html\n')
form = cgi.FieldStorage()
def main():
    answers = [form.getvalue("Locations"), form.getvalue("Type"), form.getvalue("Beds"), form.getvalue("Baths")]
    anys = []
    true_answers = []
    checked = False
    for i in range(len(answers)):
        anys.append(answers[i] if answers[i] == "Any" else true_answers.append(answers[i]))

    empty = {}
    data = open("Sheet1.csv", "r").read().split("\n")
    data = data[1:]
    for i in data:
        empty[i.split(",")[0]] = i.split(",")[1:]

    print("<html>")
    print(answers)

    if true_answers == []:
        for key, value in empty.items():
            print(key, value, "<br>")
            checked = True
    else:
        for key, value in empty.items():
            if all(x in value for x in true_answers):
                print(key, value, "<br>")
                checked = True

    if checked == False:
        print("You are either highly unrealistic or terribily realistic... Please go back and refine your filters. ")

    print("</html")

if form.getvalue("Press_me") == "Test":
    main()
