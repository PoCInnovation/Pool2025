#!/bin/bash

command_exists() {
    command -v "$1" &> /dev/null
}

if command_exists "yarn"; then
    yarn install && yarn start
else
    echo "Yarn is not installed. Installing Yarn using npm..."
    npm install --global yarn
    if command_exists "yarn"; then
        yarn install && yarn start
    else
        echo "Failed to install Yarn. Please check your npm installation or install Yarn manually."
        exit 1
    fi
fi
