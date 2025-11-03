# Use Ubuntu 24.04 base
FROM ubuntu:24.04

# Install build tools and Python
RUN apt-get update && apt-get install -y \
    build-essential git cmake g++ python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /workspace

# Default command
CMD ["/bin/bash"]
