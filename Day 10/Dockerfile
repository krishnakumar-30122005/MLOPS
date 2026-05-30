# 1. Use the official pre-built Ultralytics CPU image as the foundation
FROM ultralytics/ultralytics:latest-cpu

# 2. Set the directory inside the container where the app will run
WORKDIR /app

# 3. Copy requirements.txt to the container and install Flask/dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy all your code, weights, and template files into the container
COPY . .

# 5. Expose the port that Flask will run on
EXPOSE 5000

# 6. Set python environment variables
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

# 7. Command to launch the Flask web application
CMD ["python", "app.py"]
