FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip3 install requests python-dotenv websocket-client
ENV GOTIFY_HOST=push.example.com
ENV GOTIFY_TOKEN=XXXXXXXXXXXX
ENV NTFY_HOST=https://ntfy.sh/gotify
COPY gtfy.py /usr/bin
CMD ["python3", "/usr/bin/gtfy.py"]