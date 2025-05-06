FROM python:3.9-slim

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update
RUN apt-get install -y curl software-properties-common libpq-dev build-essential libssl-dev


# install python dependencies
RUN pip install --upgrade pip

# Copy requirements file
COPY requermint.txt /app/requermint.txt


# Install remaining requirements 
RUN pip install  -r requermint.txt 

# Copy application code
COPY . /app/

# Set environment variables
ENV football_api="d20816f6bfmsh4bd8471a7d15f8bp109432jsn5459274f3f36"
ENV setfit_model_id="Ah7med/setfit-football_bootpress_paraph-multi-v2"
ENV gliner_model_id="urchade/gliner_multi-v2.1"

# # Expose the port the app will run on
# EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]