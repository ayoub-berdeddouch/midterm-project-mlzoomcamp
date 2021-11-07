FROM python:3.8.12-slim

LABEL maintainer="Ayoub Berdeddouch"

ENV PYTHONUNBUFFERED=TRUE

RUN pip --no-cache-dir install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN set -ex && pipenv install --deploy --system
# RUN pipenv install --deploy --system 

COPY ["predict.py", "model_n_estimators=400.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]