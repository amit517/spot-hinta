# Use an official C++ base image
FROM gcc:latest

# Set the working directory
WORKDIR /app

# Install required packages
RUN apt-get update && apt-get install -y \
    cmake \
    git \
    libboost-all-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Clone Crow, CPR, and nlohmann/json libraries
RUN git clone https://github.com/CrowCpp/Crow.git && \
    git clone https://github.com/libcpr/cpr.git && \
    git clone https://github.com/nlohmann/json.git

# Build and install CPR
WORKDIR /app/cpr
RUN mkdir build && cd build && \
    cmake .. && \
    make && \
    make install

# Build and install Crow
WORKDIR /app/Crow
RUN mkdir build && cd build && \
    cmake .. && \
    make && \
    make install

# Build your application
WORKDIR /app
COPY . .

# Compile the application
RUN g++ -o my_app app.cpp -I /usr/local/include -L /usr/local/lib -lcpr -lCrow -lnlohmann_json

# Expose the application port
EXPOSE 18080

# Command to run the application
CMD ["./my_app"]
