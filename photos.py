#! /usr/bin/python3
import cgi
import cgitb
cgitb.enable()
print('Content-type: text/html\n')
form = cgi.FieldStorage()

def photo():
    print("<html>")
    floor1 = ['1stfloor1.jpg', '1stfloor2.jpg', '1stfloor3.jpg', '1stfloor4.jpg']
    floor2 = ['2ndfloor1.jpg', '2ndfloor2.jpg', '2ndfloor3.jpg', '2ndfloor4.jpg', '2ndfloor5.jpg']
    floor3 = ['3rdfloor1.jpg', '3rdfloor2.jpg', '3rdfloor3.jpg']
    floor4 = ['4thfloor1.jpg', '4thfloor2.jpg', '4thfloor3.jpg', '4thfloor4.jpg', '4thfloor5.jpg']
    floor5 = ['5thfloor1.jpg', '5thfloor2.jpg', '5thfloor3.jpg']
    floor6 = ['6thfloor1.jpg', '6thfloor2.jpg']
    floor7 = ['7thfloor2.jpg', '7thfloor3.jpg', '7thfloor4.jpg']
    floor8 = ['8thfloor1.jpg', '8thfloor2.jpg']
    floor9 = ['9thfloor2.jpg', '9thfloor3.jpg', '9thfloor4.jpg','9thfloor5.jpg']
    floor10 = ['10thfloor1.jpg','10thfloor2.jpg','10thfloor3.jpg']
    vfloors = [floor1, floor2, floor3, floor4, floor5, floor6, floor7, floor8, floor9, floor10]
    sfloors = ["floor1", "floor2", "floor3", "floor4", "floor5", "floor6", "floor7", "floor8", "floor9", "floor10"]

    answer = form.getvalue("floor")
    file = open("photos.html", "r").read()
    for i in vfloors[sfloors.index(answer)]:
        file += "<div class='grid-item'> <br> <img onclick='onClick(this);' src='%s' alt='Smiley face' height='5%%' width='300px'> <br>" % i + "</div>"
    file += "</div> </html>"
    print(file)

if form.getvalue("submit") == 'View More':
    photo()
