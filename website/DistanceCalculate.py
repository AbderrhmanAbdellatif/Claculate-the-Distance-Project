from flask import Blueprint, render_template, request
from distance import calculate_distance
DistanceCalculate = Blueprint('DistanceCalculate', __name__)

@DistanceCalculate.route('/distance', methods=['GET', 'POST'])
def distance_calculate():
    distance =' '
    if request.method == 'POST':
        location_two = request.form.get('location_two')
        if location_two == None:
            distance = calculate_distance(str('Istanbul'))
        else:
            distance = calculate_distance(str(location_two))

    return render_template("distance.html", data=distance)

