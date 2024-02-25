#!/usr/bin/env bash
# This script generates a new RSA key pair specifically for SSH authentication.
# It checks if a RSA public key already exists in the user's .ssh directory.
# If it does not exist, the script proceeds to generate a new RSA key pair.
# The public key is shared for setup on remote servers or services that support SSH access.
# The private key is kept secure, and its security is the user's responsibility.
# Usage of a passphrase for the key pair is encouraged for additional security.

# Set the path for the RSA public key
public_key_path="$HOME/.ssh/0-RSA_public_key.pub"

# Inform the user about the script's action
echo "Attempting to generate an RSA key pair for SSH authentication..."

# Check if the RSA public key already exists to avoid overwriting
if [[ -f "$public_key_path" ]]; then
    echo "Error: RSA public key already exists at $public_key_path."
    echo "Please backup and remove the existing key before generating a new one."
    exit 1  # Exit the script with an error status
else
    # Generate the RSA key pair
    ssh-keygen -t rsa -b 2048 -f "${public_key_path%.*}" -C "your_email@example.com"

    # Set the appropriate permissions for the private key
    chmod 600 "${public_key_path%.*}"

    # Output the result and provide further instructions
    echo "RSA key pair generated successfully."
    echo "Public key stored at: $public_key_path"
    echo "Ensure your private key is stored securely."
    echo "Consider adding a passphrase for additional security."
fi
