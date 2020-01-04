This is a learnning project.
Inside:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back  
2. Guess Game - guess a number and see if you chose like the computer 

After every win  points will be added to a score.txt file. 1 point per difficulty level (difficulty 3 = 3 points). 
- MainScores.py will show to current score as a flask website.
- Dockerfile - build env with the project.
- docker-compose.yml run the orchestration
- Jenkinsfile.groovy:
    test the project by testing the score from the flask webserver (MainScores.py)
    /test/e2e.py will be used to test the webserver