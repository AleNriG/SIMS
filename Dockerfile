FROM python:3.7

COPY . /app
WORKDIR /app

RUN pip3 install -r req.txt
RUN pip3 install pytest==3.7.1 pluggy==0.7.1 pytest-quickcheck

ENTRYPOINT ["pytest"]
CMD ["--disable-pytest-warnings", "-v", "tests/"]
