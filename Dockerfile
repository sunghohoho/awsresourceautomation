FROM amazon/aws-lambda-python:3.10

RUN /var/lang/bin/python3.10 -m pip install --upgrade pip

RUN

ENTRYPOINT ["top", "-b"]