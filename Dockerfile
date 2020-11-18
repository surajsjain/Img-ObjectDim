FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN /usr/local/bin/python -m pip install --upgrade pip

# RUN pip3 install -r requirements.txt
RUN pip3 install tensorflow==1.15.4
RUN pip3 install Keras==2.1.3
RUN pip3 install pillow
RUN pip3 install opencv-python
RUN pip3 install h5py==2.10.0

COPY . /code/
CMD bash run.sh
