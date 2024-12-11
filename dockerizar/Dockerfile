FROM python:3.12-slim
COPY connectAPI.py /
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./connectAPI.py"]
