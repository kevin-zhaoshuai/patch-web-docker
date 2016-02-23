FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD ./git_work.py /code/
RUN apt-get update && apt-get install -y \
    git \
    python-mysqldb
RUN git clone git://git.openstack.org/openstack/nova
RUN git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
RUN git clone git://libvirt.org/libvirt.git
RUN pip install MySQL-python
