FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy your app file into the container
COPY app.py .

# Install Flask
RUN pip install flask

# Expose the port Flask will run on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
