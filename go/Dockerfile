# Use the official Golang image as a build environment
FROM golang:1.20 AS builder

# Set the Current Working Directory inside the container
WORKDIR /app

# Copy go.mod and go.sum files first to leverage cached layers
COPY go.mod go.sum ./

# Download all dependencies. Dependencies will be cached if the go.mod and go.sum files are not changed
RUN go mod download

# Copy the source code into the container
COPY app.go .  # Copy only the app.go file

# Build the Go app
RUN go build -o my_app app.go  # Build the application from app.go

# Use a smaller image for the final deployment
FROM alpine:latest

# Set the Current Working Directory inside the container
WORKDIR /root/

# Copy the binary from the builder stage
COPY --from=builder /app/my_app .

# Expose the port the app runs on
EXPOSE 8080

# Command to run the executable
CMD ["./my_app"]
