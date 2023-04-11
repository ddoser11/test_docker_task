FROM python:3.6-slim
WORKDIR /flaskex-master
COPY . .

RUN pip install --user -r requirements.txt

CMD [ "python", "-u", "app.py" ]

EXPOSE 5000