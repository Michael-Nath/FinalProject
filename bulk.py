#! /usr/bin/python3
import cgi
import cgitb

# Note to Self: Make sure to convert any numbers back to it's respective comma form
cgitb.enable()
print('Content-type: text/html\n')
form = cgi.FieldStorage()

def intersection(lst1, lst2):
    if lst1 == []:
        if lst2 != []:
            return lst2
        else:
            return []
    if lst2 == []:
        if lst1 != []:
            return lst1
        else:
            return []

    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def main():
    Location = []
    Type = []
    Beds = []
    Baths = []
    answers = [form.getvalue("Locations"), form.getvalue("Type"), form.getvalue("Beds"), form.getvalue("Baths")]
    anys = []
    true_answers = []
    results = open("results.html", "r").read()
    for i in range(len(answers)):
        anys.append(answers[i] if answers[i] == "Any" else true_answers.append(answers[i]))

    empty = {}
    data = open("Sheet1.csv", "r").read().split("\n")
    data = data[1:]
    for i in data:
        empty[i.split(",")[0]] = i.split(",")[1:]

    print("<html>")
    if true_answers == []:
        for key, value in empty.items():
            results += "<div class='grid-item'>" + key +  " <img src='%s' alt='Smiley face' height='250px' width='300px'> <br> </div>" % (value[-1])
        results += "</div> </body> </html>"
    else:
        def helper(List, answer):
            for key, value in empty.items():
                if type(answer) == list:
                    if any(x in value for x in answer):
                        List.append([key, value])
                else:
                    if answer in value:
                        List.append([key, value])

    if form.getvalue("Locations") != "Any":
        helper(Location, form.getvalue("Locations"))
    if form.getvalue("Type") != "Any":
        helper(Type, form.getvalue("Type"))
    if form.getvalue("Beds") != "Any":
        helper(Beds, form.getvalue("Beds"))
    if form.getvalue("Baths") != "Any":
        helper(Baths, form.getvalue("Baths"))

    intersected = intersection(intersection(Location, Type),intersection(Beds, Baths))
    if intersected == [] and true_answers != []:
        print("You are either highly unrealistic or terribily realistic... Please go back and refine your filters. ")
    else:
        for i in intersected:
            results += "<div class='grid-item'> " + i[0] + " <br> <img src='%s' alt='Smiley face' height='250px' width='300px'> <br>" % (i[1][-1]) + " Location: %s <br> Price: %s <br> Type: %s <br> Beds: %s <br> Baths: %s <br> SQFT: %s" % (i[1][0], i[1][1], i[1][2], i[1][3], i[1][4], i[1][5]) + " <br> <br> </div>"
        results += "</div> </body> </html>"

    print(results)

if form.getvalue("Press_me") == "Test":
    main()
