FROM python
RUN git clone https://github.com/yahelron/World-of-Games/
WORKDIR /World-of-Games
RUN pip install -r requirements.txt
RUN chmod 644 MainScores.py
CMD ["python", "MainScores.py"]
EXPOSE 8777/tcp
# RUN curl -f http://127.0.0.1:8777`
