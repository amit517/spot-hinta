# Use a minimal Go image
FROM golang:1.20-alpine

# Set the working directory
WORKDIR /app

# Copy the Go files
COPY . .

# Build the Go application
RUN go build -o app .

# Expose the port
EXPOSE 8080

# Command to run the application
CMD ["./app"]
