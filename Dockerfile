# Use an official Debian runtime as a parent image
FROM debian:bookworm-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . .

# Create a virtual environment
RUN python3 -m venv venv

# Install any needed packages specified in requirements.txt using the virtual environment
RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

# Make the virtual environment's Python the default
ENV PATH="/app/venv/bin:$PATH"

# Run subdomaincheck.py when the container launches
CMD ["python", "subdomaincheck.py"]
