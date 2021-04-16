FROM tiangolo/uwsgi-nginx-flask:python3.6
WORKDIR /app/ 
COPY . /app/
#EXPOSE 8000
RUN pip install -r requirements.txt 
CMD python3 main.py
