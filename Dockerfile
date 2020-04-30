FROM python:3.7

RUN mkdir -p tmp
RUN pip install -U pip
COPY requirements.txt /tmp
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt
RUN rm -rf /tmp

COPY . /

ENTRYPOINT [ "python" ]

CMD [ "setup.py" ]