#!/usr/bin/env bash
# This script generates an RSA key pair for SSH authentication.

# Specify the key file name and directory
KEY_DIR="$HOME/.ssh"
KEY_NAME="0-RSA_public_key"
KEY_PATH="$KEY_DIR/$KEY_NAME"

# Create the .ssh directory if it doesn't exist
mkdir -p "$KEY_DIR"

# Set the appropriate permissions for the .ssh directory
chmod 700 "$KEY_DIR"

# Generate a 2048-bit RSA key pair
if [ ! -f "$KEY_PATH" ]; then
    ssh-keygen -t rsa -b 2048 -f "$KEY_PATH" -N ''
    echo "RSA key pair generated at $KEY_PATH and $KEY_PATH.pub"
else
    echo "RSA key pair already exists at $KEY_PATH and $KEY_PATH.pub"
fi

# Set the appropriate permissions for the key files
chmod 600 "$KEY_PATH"
chmod 644 "$KEY_PATH.pub"

# Display the public key
echo "Public key contents:"
cat "$KEY_PATH.pub"
