FROM python
COPY . /app
WORKDIR /app
COPY reqs.txt .
RUN pip install -r reqs.txt
CMD ["python3", "app.py"]
EXPOSE 5000
