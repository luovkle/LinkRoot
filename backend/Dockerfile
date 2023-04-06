FROM python:3.11-alpine
WORKDIR /app
COPY ["./app/requirements.prod.txt", "/app/"]
RUN pip install --no-cache-dir -r requirements.prod.txt
COPY ["./app/app", "/app/app/"]
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
