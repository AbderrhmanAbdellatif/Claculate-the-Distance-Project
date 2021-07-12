    
import requests
import json
import math
import logging
import datetime
logger = logging.getLogger('myApp')
def rad(x):
    return  x*math.pi/180
def create_log_file():
    hdlr = logging.FileHandler(r'result.log'.format(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S_%f')))
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)
def getDistance(p1,p2):
    # ref :https://www.movable-type.co.uk/scripts/latlong.html
    logger.info('Get Dictance of two location')
    p2['lat']=float(p2['lat'])
    p1['lat']=float(p1['lat'])
    p2['lng']=float(p2['lng'])
    p1['lng']=float(p1['lng'])
    
    R = 6378137 #Earth’s mean radius in meter
    dLat = rad(p2['lat'] - p1['lat'])
    dLong = rad(p2['lng'] - p1['lng'])
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(rad(p1['lat'])) * math.cos(rad(p2['lat'])) * math.sin(dLong / 2) * math.sin(dLong / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    logger.info('returns the distance in meter')
    return d #returns the distance in meter
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))
def calculate_distance(location_two_input):
    create_log_file()
    try:
        location_one=requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=5046db4f-4d5e-4d18-815e-5035e71f317e&geocode=MKAD+Moscow,Russian+Federation&lang=en_US&format=json')#Third Ring Road ,Moscow, Russian Federation
        logger.info('input information of location one is : MKAD Moscow, Russian Federation')
        logger.info('input the seconde Address')
        location_two=requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=5046db4f-4d5e-4d18-815e-5035e71f317e&geocode='+listToString(location_two_input.replace(' ','+').split(',')[::-1])+'&lang=en_US&format=json') # the seconde aderss
        input_tow=listToString(location_two_input)
        logger.info('if the specified address is located inside the MKAD')
        if 'Moscow' in input_tow: #if the specified address is located inside the MKAD
              return 'location does not need to calculate '
        else:
            json_object = json.loads(location_one.text)# take the first location as json
            p1_lat=json_object['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[0]
            p1_lng=json_object['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[1]
            logger.info('take the point of first location')
            json_object = json.loads(location_two.text)#take the second location as json
            p2_lat=json_object['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[0]
            p2_lng=json_object['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[1]
            logger.info('take the point of second location')
            dic_point_one={'lat':p1_lat,'lng':p1_lng}
            dic_point_two={'lat':p2_lat,'lng':p2_lng}
            
            logger.info('take the point of first location is :('+ dic_point_one['lat'] + ' , '+dic_point_one['lng']+')')
            logger.info('take the point of second location is :('+ dic_point_two['lat'] + ' , '+dic_point_two['lng']+')')
            logger.info('the distance between  two location is '+ str(getDistance(dic_point_one,dic_point_two) * 0.001)+" KM")
    except Exception as e:
                logger.error(e)
                print(e)
                return "Please input valid location"
    return str(getDistance(dic_point_one,dic_point_two) * 0.001)+" KM"
