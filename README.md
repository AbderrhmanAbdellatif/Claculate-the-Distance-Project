# Problem statement:

Develop a Flask Blueprint to find the distance from the Moscow's Ring Road to the specified address. The address is passed to the application in an HTTP request, if the specified address is located inside the MKAD, the distance does not need to be calculated. Add the result to the .log file.

# Description 
Used yandex map key to get pointer of the input location and after that develop function called getDistance that use the ‘haversine’ formula to calculate the great-circle distance between two points – that is, the shortest distance over the earth’s surface – giving a ‘as-the-crow-flies’ distance between the points (ignoring any hills they fly over, of course!). Than this function gives result as meter and it is converted to km.

# Platform 
1- visual Studio code 
<br>
2- Yandex browser
<br>
3- Flask Framework
<br>
4- Jupyter

# Materials
1- Yandex map key
<br>
2- python 3.9

# How to Run the application
 1- git clone https://github.com/AbderrhmanAbdellatif/Claculate-the-Distance-Project.git
 <br>
 2- pip install -r requirements.txt
 <br>
 3- run python main.py
 <br>
 4- Press http://127.0.0.1:5000/ to browser 
 <br>
 5- input/put 2nd location 
 
 
 
 



# Reference

 https://yandex.ru/dev/maps/geocoder/doc/desc/concepts/about.html
 <br>
 https://www.movable-type.co.uk/scripts/latlong.html
 
 
 
 # images 
 ![main](https://github.com/AbderrhmanAbdellatif/Claculate-the-Distance-Project/blob/main/Main.jfif)

 
 
 
 
