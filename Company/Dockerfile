FROM python:3.7.4-slim-buster
RUN apt-get update && apt-get install -y libaio1 wget
RUN apt-get install -y unzip
WORKDIR /opt/oracle
RUN wget https://download.oracle.com/otn_software/linux/instantclient/214000/instantclient-basiclite-linux.x64-21.4.0.0.0dbru.zip
RUN unzip instantclient-basiclite-linux.x64-21.4.0.0.0dbru.zip && \
    rm -f instantclient-basiclite-linux.x64-21.4.0.0.0dbru.zip
RUN cd /opt/oracle/instantclient_21_4 && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci
RUN echo /opt/oracle/instantclient_21_4 > /etc/ld.so.conf.d/oracle-instantclient.conf && ldconfig

RUN echo 'running docker, install dependencies of docker file '
ADD requirements.txt /app/requirements.txt
RUN echo 'now installing from req.txt if any left'
RUN pip install -r /app/requirements.txt
RUN echo 'copying everything to app'
COPY . /opt/oracle

COPY /keys  /opt/oracle/instantclient_21_4/network/admin

RUN echo 'Exposing port 5060'
EXPOSE 5060
CMD ["gunicorn", "-b", "0.0.0.0:5060", "-t","120", "wsgi"]