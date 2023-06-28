FROM python:3.10.5
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python main.py