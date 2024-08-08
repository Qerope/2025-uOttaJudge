# Use Debian Buster as the base image
FROM debian:buster

# Set environment variables to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && \
    apt-get install -y \
    postgresql-11 postgresql-server-dev-11 \
    redis-server \
    python3-dev python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python virtualenv
RUN pip3 install virtualenv

# Configure PostgreSQL
RUN echo "local all   postgres              peer"  > /etc/postgresql/11/main/pg_hba.conf && \
    echo "local all   all                   peer"  >> /etc/postgresql/11/main/pg_hba.conf && \
    echo "host  uottajudge vagrant  ::1/128      trust" >> /etc/postgresql/11/main/pg_hba.conf && \
    echo "host  uottajudge vagrant  127.0.0.1/32 trust" >> /etc/postgresql/11/main/pg_hba.conf

# Create the database and user
RUN service postgresql start && \
    su postgres -c "createdb uottajudge 2>/dev/null || true" && \
    su postgres -c "createuser vagrant 2>/dev/null || true" && \
    service postgresql stop

# Expose ports
EXPOSE 5000

# Set the working directory
WORKDIR /uottajudge

# Copy application code and configuration files
COPY . /uottajudge

# Set up virtual environment and install Python dependencies
RUN virtualenv env && \
    . env/bin/activate && \
    pip install -r requirements.txt && \
    cp config.vagrant.yaml config.yaml && \
    python initialize.py

# Start PostgreSQL and Redis, then run the application
CMD service postgresql start && \
    service redis-server start && \
    . env/bin/activate && \
    DEBUG=true python runserver.py
