
# Define a task for building the Docker image
docker-build:
    docker build -t myapp .

# Define a task for running the Docker container
docker-run:
    docker run myapp

# Define a task for cleaning up Docker artifacts
docker-clean:
    docker system prune --all --force

# Define a task for installing Python dependencies
install:
    pip install -r requirements.txt

# Define a task for running the main script
run:
    python main.py
