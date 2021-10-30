FROM python
COPY . /app
WORKDIR /app
COPY reqs.txt
RUN pip install -r req.txt
CMD ["python3", "app.py"]
