FROM harbor.beautytiger.com/docker.io/python:3.8.0
WORKDIR /app
EXPOSE 8000
ENV PYTHONUNBUFFERED 0
ADD . /app
RUN cp pip.conf /etc/pip.conf && pip install -r requirements.txt
#CMD ./run.sh
ENTRYPOINT ["./run.sh"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
