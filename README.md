# World-of-Games_P3
The World-of-Games -  a Learning Devops project

Welcome to my learning project :)

Inside you can find an app written in python, using a flask framework. 
This project presents many DevOps technologies and can help you to understand better how to use each of them.

The WOG DevOps learning app:
Contains of two web games:
1.	Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
2.	Guess Game - guess a number and see if you chose like the computer
After every win, points will be added to a MySQL database. 1 point per difficulty level (difficulty 3 = 3 points).
app components:
•	App.py will – run the webserver, control the app and also contains the memory game.
•	GuessGame..py – contains the guest game. run in a separate flask webserver. returns result via REST API.
•	Score.py – connect to the Database and manage the scores.
Building options:
•	Dockerfile - build the containers of the project.
•	docker-compose.yml run the orchestration
•	k8s – build 
•	Jenkinsfile.groovy: test the project by testing the score from the flask webserver (MainScores.py) /test/e2e.py will be used to test the webserver
•	Kubernetes folder – contains all the yamel files to build the project with kubernetes orchestration.
•	kubernetes/helm folder – easy build of the project in kubernetes with helm Package Manager.
