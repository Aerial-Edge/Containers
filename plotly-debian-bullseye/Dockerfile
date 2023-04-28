FROM python:3.9-slim-bullseye

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        nginx \
        build-essential \
        python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app app

# Configure Nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY uwsgi_params /etc/nginx/uwsgi_params

# Start the app with uWSGI and Nginx
CMD uwsgi --ini uwsgi.ini && nginx -g 'daemon off;'
