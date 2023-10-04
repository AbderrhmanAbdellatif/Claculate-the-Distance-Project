# Calculate the Distance from Moscow's Ring Road

Find the distance from Moscow's Ring Road (MKAD) to a specified address using Flask and Yandex API.

## Problem Statement:

Develop a Flask Blueprint that calculates the distance from Moscow's Ring Road (MKAD) to any specified address. If the given address lies within the MKAD, there's no need to calculate the distance. Results of the distance computation are recorded in a `.log` file.

## Description:

This application employs the Yandex Map API to obtain coordinates of the input location. The core functionality is in the `getDistance` function, which utilizes the 'haversine' formula. This formula computes the great-circle distance between two points, providing an 'as-the-crow-flies' measurement. This measurement is given in meters and can be converted to kilometers.

## Platform:

1. Visual Studio Code
2. Yandex Browser
3. Flask Framework
4. Jupyter

## Materials:

1. Yandex Map API Key
2. Python 3.9

## How to Run the Application:

1. Clone the repository:
   ```bash
   git clone https://github.com/AbderrhmanAbdellatif/Calculate-the-Distance-Project.git
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute the application:
   ```bash
   python main.py
   ```

4. Open a browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

5. Enter the desired location to determine its distance from Moscow's Ring Road.

## Reference:

- [Yandex Geocoder Documentation](https://yandex.ru/dev/maps/geocoder/doc/desc/concepts/about.html)
- [Haversine Formula Explanation](https://www.movable-type.co.uk/scripts/latlong.html)

## Images:

![Main Image](https://github.com/AbderrhmanAbdellatif/Calculate-the-Distance-Project/blob/main/Main.jfif)

Note: Always remember to keep your API keys confidential to ensure your application's security and prevent unexpected costs.
