FROM python
RUN git clone https://github.com/yahelron/World-of-Games_P3.git
WORKDIR /World-of-Games_P3
RUN pip install flask
RUN pip install pymysql
#RUN pip install -r requirements.txt
RUN chmod 644 App.py
CMD ["python", "App.py"]
EXPOSE 5002/tcp
