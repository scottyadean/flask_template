FROM python:3.10-slim
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip
COPY . .

CMD [ "python", "app.py" ]