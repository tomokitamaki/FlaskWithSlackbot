FROM python:3.6.4-jessie
add flaskdir /flaskdir
add requirements.txt /flaskdir
WORKDIR /flaskdir
RUN pip install -r requirements.txt
CMD ["python", "index.py"]
