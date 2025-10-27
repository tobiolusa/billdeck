FROM python:3.13-slim
RUN mkdir /app
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Collect static files
RUN python manage.py collectstatic --noinput
