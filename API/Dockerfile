FROM python
RUN git clone https://github.com/yahelron/World-of-Games_P3.git
WORKDIR /World-of-Games_P3
RUN pip install flask
Run pip install pymysql
#RUN pip install -r requirements.txt
RUN cd /World-of-Games_P3
RUN chmod 644 GuessGame.py
CMD ["python", "GuessGame.py"]
EXPOSE 5000/tcp
