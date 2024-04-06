To launch a simple "Hello World" app using Docker Desktop, you will follow a few straightforward steps. This example will guide you through creating a minimal web application using Python and Flask, packaging it into a Docker container, and running it on Docker Desktop. Flask is chosen for its simplicity and Python because of your familiarity with it. If you’re more comfortable with another language or framework, the steps are similar.

## Step 1: Create the Flask App
First, create a new directory for your project and add a Python file for your Flask app, for example, app.py. In app.py, write the following code to create a simple web server that returns "Hello, World!" when accessed:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

## Step 2: Create a Requirements File
Create a requirements.txt file in the same directory with the following content to specify the Flask dependency:

```makefile
Flask
```

## Step 3: Create a Dockerfile
Next, create a Dockerfile in the same directory. This file contains instructions for building the Docker image:

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

## Step 4: Build the Docker Image
Open a terminal, navigate to the directory containing your project, and run the following command to build your Docker image. Replace my-hello-world-app with your preferred image name.

```sh
docker build -t my-hello-world-app .
```

## Step 5: Run the Docker Container
Once the image is built, run the container using the following command. This command maps port 5000 of the container to port 5000 on your host, allowing you to access the Flask app from your web browser.

```sh
docker run -p 5000:5000 my-hello-world-app
```

To modify step 5 so that your Docker container runs automatically and restarts no matter what, you'll use the --restart flag with the docker run command. This flag controls the restart policy for how a Docker container should be handled at exit. For your requirement, the always policy is appropriate. This ensures that the container will restart if it exits for any reason, if Docker restarts, or if the system reboots, ensuring high availability.

Here's how you modify step 5:

```sh
docker run -d -p 5000:5000 --restart=always --name hello-world-container my-hello-world-app
```

Let's break down the modifications:

-d: This runs the container in detached mode, meaning it runs in the background of your terminal. It allows you to continue using the terminal session.
--restart=always: This sets the restart policy to always, so the container will always restart unless it is explicitly stopped or Docker itself is stopped or restarted.
Understanding Restart Policies
Docker supports several restart policies:

no: This is the default restart policy, and it does not restart a container under any circumstance when it exits.
on-failure: This restarts the container if it exits with a non-zero exit status. Optionally, you can limit the number of restart retries Docker will attempt.
always: This always restarts the container unless it is explicitly stopped or Docker is stopped or restarted.
unless-stopped: Similar to always, but it does not restart the container if the container has been stopped before Docker is restarted.
Choosing the right restart policy depends on your application's needs and how you manage your containers. For most production scenarios, always or unless-stopped is recommended to ensure your applications remain available.


## Step 6: Access the App
Open your web browser and navigate to http://localhost:5000. You should see the "Hello, World!" message displayed.

This example provides a basic understanding of developing and containerizing applications with Docker. Docker Desktop simplifies managing Docker containers on your local machine, offering an intuitive GUI for monitoring and interacting with your containers. For more complex applications, consider exploring Docker Compose for managing multi-container applications, integrating databases, and adding persistent storage.


