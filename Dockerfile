FROM python:3.8

RUN mkdir -p tmp
RUN python -m pip install --upgrade pip
COPY requirements.txt /tmp
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt
RUN rm -rf /tmp

COPY . /

ENTRYPOINT [ "python" ]

CMD [ "setup.py" ]