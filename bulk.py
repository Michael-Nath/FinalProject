#! /usr/bin/python3
# all python code is possible because of Michael Nath
import cgi
import cgitb

cgitb.enable()
print('Content-type: text/html\n')
form = cgi.FieldStorage()

def dict_intersect(list1, list2, list3, list4):
    all_words = list1 + list2 + list3 + list4
    intersects = []
    for i in all_words:
        if all_words.count(i) == 4 and i not in intersects:
            intersects.append(i)
    return intersects

def main():
    Location = []
    Type = []
    Beds = []
    Baths = []
    answers = [form.getvalue("Locations"), form.getvalue("Type"), form.getvalue("Beds"), form.getvalue("Baths")]
    filters = ["Location", "Price", "Type", "Beds", "Baths", "Sq Ft", "Image Link"]
    anys = []
    every = []
    true_answers = []
    results = open("results.html", "r").read()
    for i in range(len(answers)):
        anys.append(answers[i] if answers[i] == "Any" else true_answers.append(answers[i]))

    empty = {}


    data = open("Sheet1.csv", "r").read().split("\n")


    data = data[1:]
    for i in data:
        empty[i.split(",")[0]] = i.split(",")[1:]

    for key, value in empty.items():
        every.append([key, value])
    print("<html>")
    if true_answers == []:
        for key, value in empty.items():
            results += "<div class='grid-item'>" + key + " <img src='%s' alt='Smiley face' height='250px' width='300px'> <br>" % (value[-1]) + " Location: %s <br> Price: %s <br> Type: %s <br> Beds: %s <br> Baths: %s <br> SQFT: %s" % (value[0], value[1], value[2], value[3], value[4], value[5]) + " <br> <br>"
            results += "<form method='get' action='more.py'> <input type='hidden' id='house' name='house' value='%s'> <input type='submit' name='submit' value='See More!'></form> </div>" % key
        results += "</div> </body> </html>"
    else:
        def helper(List, answer, typ):
            for key, value in empty.items():
                if type(answer) == list:
                    if any(x == value[filters.index(typ)] for x in answer):
                        List.append([key, value])
                else:
                    if value[filters.index(typ)] == answer:
                        List.append([key, value])

    if form.getvalue("Locations") != "Any":
        helper(Location, form.getvalue("Locations"), "Location")
    else:
        Location = every
    if form.getvalue("Type") != "Any":
        helper(Type, form.getvalue("Type"), "Type")
    else:
        Type = every
    if form.getvalue("Beds") != "Any":
        helper(Beds, form.getvalue("Beds"), "Beds")
    else:
        Beds = every
    if form.getvalue("Baths") != "Any":
        helper(Baths, form.getvalue("Baths"), "Baths")
    else:
        Baths = every

    intersected = dict_intersect(Location, Type, Beds, Baths)
    if any(x == None for x in answers):
        results += "<div class='failure'> You have forgotten to enter in a filter (or filters)!!! Go back and make sure none of the filters say 'Select Your Option' </div>"

    elif intersected == [] and true_answers != []:
        results += "<div class='failure'> You are either highly unrealistic or terribily realistic... Please go back and refine your filters. </div>"
    else:
        if true_answers != []:
            for i in intersected:
                results += "<div class='grid-item'> " + i[0] + " <br> <img src='%s' alt='Smiley face' height='250px' width='300px'> <br>" % (i[1][-1]) + " Location: %s <br> Price: %s <br> Type: %s <br> Beds: %s <br> Baths: %s <br> SQFT: %s" % (i[1][0], i[1][1], i[1][2], i[1][3], i[1][4], i[1][5]) + "<br> <br>"
                results += "<form method='get' action='more.py'> <input type='hidden' id='house1' name='house' value='%s'> <input type='submit' name='submit' value='See More!'></form> </div>" % i[0]
            results += "</div> </body> </html>"

    print(results)


if form.getvalue("Press_me") == "Search!":
    main()
