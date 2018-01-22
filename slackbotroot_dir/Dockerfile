FROM python:3.6.4-jessie
add slackbotdir /slackbotdir
add requirements.txt /slackbotdir
WORKDIR /slackbotdir
RUN pip install -r requirements.txt
CMD ["python", "run.py"]
