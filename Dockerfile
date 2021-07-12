# init a base image (Alpine is small Linux distro)
FROM python:3.6.1-alpine
# define the present working directory
WORKDIR /Flask-Web-App-Tutorial-main
# copy the contents into the working dir
ADD . /Flask-Web-App-Tutorial-main
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
CMD ["python","main.py"]