FROM python
RUN git clone https://github.com/yahelron/World-of-Games_P3.git
WORKDIR /World-of-Games_P3
RUN pip install flask
Run pip install pymysql
#RUN pip install -r requirements.txt
RUN chmod 644 MainScores.py
CMD ["python", "MainScores.py"]
EXPOSE 8777/tcp
