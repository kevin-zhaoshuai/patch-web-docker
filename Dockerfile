FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/db
WORKDIR /code
ADD ./mysite/requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update -y && apt-get install -y apache2 libapache2-mod-wsgi && apt-get clean 
ADD . /code/
RUN cp /code/mysite/mysite /var/www/ -r
RUN cp /code/mysite/*.conf /etc/apache2/sites-available/

EXPOSE 80

CMD /bin/bash -c "python /code/mysite/mysite/manage.py syncdb --noinput;/usr/sbin/apache2ctl -D FOREGROUND"
