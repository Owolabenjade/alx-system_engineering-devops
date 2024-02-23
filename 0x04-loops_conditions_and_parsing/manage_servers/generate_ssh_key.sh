#!/usr/bin/env bash
# This script generates an RSA key pair and saves the public key to 0-RSA_public_key.pub

# Generate RSA key pair
ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa -N ""

# Copy the public key to the designated file
cp ~/.ssh/id_rsa.pub 0-RSA_public_key.pub

# Display a success message
echo "RSA key pair generated successfully. Public key saved to 0-RSA_public_key.pub."
