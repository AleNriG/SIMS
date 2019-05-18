FROM python:3.7

WORKDIR /app
COPY Pipfile* ./

RUN apt-get update && python -m pip install pipenv \
	&& pipenv install --system && apt-get clean

COPY src/ .
ENTRYPOINT ["python"]
CMD ["sims.py"]
