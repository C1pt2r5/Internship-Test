FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install htop
RUN apt-get update && apt-get install -y htop && apt-get clean

COPY . .

# Make port 5000 available
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

