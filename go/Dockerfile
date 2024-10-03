# Use the official Golang image as a build environment
FROM golang:1.20 AS builder

# Set the Current Working Directory inside the container
WORKDIR /app

# Copy the source code into the container
COPY app.go .

# Copy go.mod if you have it
COPY go.mod . 

# Build the Go app with CGO disabled for static binary
RUN CGO_ENABLED=0 go build -o my_app app.go  

# Use a smaller image for the final deployment
FROM alpine:latest

# Set the Current Working Directory inside the container
WORKDIR /root/

# Copy the binary from the builder stage
COPY --from=builder /app/my_app .

# Expose the port the app runs on
EXPOSE 8080

# Command to run the executable
CMD ["/root/my_app"]
