FROM python:latest
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY hello_world.py .
EXPOSE 3000
CMD ["waitress-serve","--port=3000", "hello_world:app"]

