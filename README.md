# Runtime Environment

## web service

- $ docker run --rm -u root -p 8080:8080 -p 50000:50000 -v /opt/jenkins:/var/jenkins_home -v $(which docker):/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock -v "$HOME":/home -d --name myjenkins jenkins
- $ docker run --name mysql-service -v /opt/mysql:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql
- Build dockerfile from webservice root directory image name as my_webservice
- $ docker run -it --name my-webservie -p 5001:5001 my_webservice

## web app

- python version: 3.7.4
- pip install -r requirements.txt
- run app.py

# webservice

- SQLAlchemy
- Log
- Flask-Restful
- Docker
- JenkinsPipeline

# webapp

- Flask-Login
- Bootstrap table
- ECharts
