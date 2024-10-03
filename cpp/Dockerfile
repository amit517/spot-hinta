# Use a lightweight Debian-based image
FROM debian:bullseye-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    g++ cmake libboost-all-dev \
    && apt-get clean

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . .

# Build the project (assuming CMake is used)
RUN cmake . && make

# Expose the port
EXPOSE 18080

# Command to run the application
CMD ["./app"]
