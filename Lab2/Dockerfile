FROM python:3.9-slim

WORKDIR /app

RUN pip install flask

COPY . .

# ✅ Create directory first, then move flag
RUN mkdir -p /var/www && mv flag.txt /var/www/flag.txt

EXPOSE 5000

CMD ["python", "app.py"]