#!/bin/bash

# Replace these with your actual Datadog API and Application keys
DD_API_KEY="your_api_key_here"
DD_APP_KEY="your_app_key_here"

# The hostname we're looking for
HOSTNAME="530745-web-01"

# Make the API call and search for the hostname
curl -s -X GET "https://api.datadoghq.com/api/v1/hosts" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" | grep -i "${HOSTNAME}"

# Check the exit status of grep
if [ $? -eq 0 ]; then
    echo "Host ${HOSTNAME} found in Datadog!"
else
    echo "Host ${HOSTNAME} not found in Datadog."
fi
