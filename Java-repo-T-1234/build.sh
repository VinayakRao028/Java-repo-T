#!/bin/bash

# Clean the project
echo "Cleaning the project..."
mvn clean

# Package the project
echo "Packaging the project..."
mvn package

# Install the project
echo "Installing the project..."
mvn install

echo "Build process completed."