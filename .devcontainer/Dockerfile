FROM python:3.8.2-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /code

# Create and set the working directory
RUN mkdir /code/
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    time \
    npm \
    vim \
    pypy3 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY .devcontainer/requirements.txt /code

# Upgrade pip and setuptools, install Python dependencies
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

# Install atcoder-cli using npm
RUN npm install -g atcoder-cli

# Add aliases
COPY ./.alias /root
RUN cat /root/.alias >> /root/.bashrc

#Add cache & config
COPY .cache /root/.cache 
COPY .config /root/.config

# Set the entry point to bash (optional)
CMD ["bash"]
