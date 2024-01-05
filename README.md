# Intelligent Landscape Classifier

Authors: Pablo Sanchez, Axel Loyanta Daoudongar, Esteban Juan Mattiacci (Group 2)

## Overview

This Docker image contains an Intelligent Landscape Classifier (ILC) program. It allows users to classify landscape images into 6 different categories (0:'Buildings', 1: 'Forest', 2: 'Glacier', 3: 'Mountain', 4: 'Sea', 5: 'Street').

## Requirement : Install Docker Desktop

If you don't have Docker Desktop installed, you can download and install it from [Docker's official website](https://www.docker.com/products/docker-desktop).

## Usage

Follow these steps to run the Intelligent Landscape Classifier using Docker:

1. ***Pull the image:***
   ```bash
   docker pull pablo1205/ilc
    ```
2. ***Run the Docker Container:***
    ```bash
    docker run -p 5000:5000 pablo1205/ilc
     ```

3. ***Access the Application:***
    Open your web browser and go to http://127.0.0.1:5000.

4. ***Upload and Classify Images:***
    Click on "Choisir un fichier" to upload an image from the "Dataset Sample" folder.
    After uploading, click on "Classify Landscape" to see the predictions.

5. ***Repeat and Explore:***
    Repeat step 5 with different images to explore the Intelligent Landscape Classifier.

6. ***Stop the Docker Container:***
    Press Ctrl+C in the terminal where the Docker container is running.
    Alternatively, manually stop the container using Docker Desktop.
    
## Additional Information
    The program predicts the class of landscape images with corresponding class names.
    Classes: [0, 1, 2, 3, 4, 5]
    Class Names: ['Buildings', 'Forest', 'Glacier', 'Mountain', 'Sea', 'Street']
