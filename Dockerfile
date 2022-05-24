FROM python:3.10.4-slim-bullseye

WORKDIR /

COPY . ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "-u", "app/app.py"]