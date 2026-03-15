FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and dependencies into the container
COPY app.py .
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the outside world
EXPOSE 8080

# Run the Python script when the container starts
CMD ["python", "bot.py"]