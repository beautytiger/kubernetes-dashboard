FROM harbor.beautytiger.com/docker.io/python:3.8.0
WORKDIR /app
EXPOSE 8000
ADD . /app
RUN cp pip.conf /etc/pip.conf && pip install -r requirements.txt
CMD ./run.sh
