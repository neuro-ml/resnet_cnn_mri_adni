FROM nvidia/cuda:7.5-cudnn5-devel

MAINTAINER Safiullin Amir amir147@rambler.ru

RUN apt-get clean && apt-get update
RUN apt-get install -yqq python3 python3-pip python3-dev build-essential \
    python3-setuptools python3-numpy python3-scipy \
    libatlas-dev libatlas3gf-base \
    git wget gfortran libatlas-base-dev libatlas3-base libhdf5-dev \
    libfreetype6-dev libpng12-dev pkg-config libxml2-dev libxslt-dev \
    libboost-program-options-dev zlib1g-dev libboost-python-dev

ADD scripts /scripts

RUN pip3 install -U pip cython numpy
RUN pip3 install -U -r scripts/requirements.txt

EXPOSE 8888
VOLUME ["/notebook", "/scripts"]
WORKDIR /scripts

ADD test_scripts /test_scripts
COPY .theanorc /root/.theanorc
ADD jupyter /jupyter
ENV JUPYTER_CONFIG_DIR="/jupyter"

CMD ["jupyter", "notebook", "--ip=localhost"]
