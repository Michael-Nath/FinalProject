#! usr/bin/python3
import cgi
import cgitb
# Note to Self: Make sure to convert any numbers back to it's respective comma form
cgittb.enable()
print('Content-type: text/html\n')
def main():
    empty = {}
    data = open("houses.csv", "r").read().split("\n")
    houses = data[1:]
    for i in houses:
        empty[i.split(",")[0]] = i.split(",")[1:]
    for key, value in empty.items():
        print(key, value)