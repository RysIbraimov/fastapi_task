# Project: Setting Up and Running a FastAPI Application Using Docker

## Creating a Repository

1. Initialize a git repository:
    ```sh
    git init
    ```

2. Add a remote repository:
    ```sh
    git remote add origin git@github.com:<username>/<repository_name>.git
    ```

3. Add a .gitignore file:
    ```sh
    # Add necessary rules to the .gitignore file
    ```

4. Add all files to the repository:
    ```sh
    git add .
    ```

5. Commit changes:
    ```sh
    git commit -m "Initial commit"
    ```

6. Create the main branch:
    ```sh
    git branch -M main
    ```

7. Push changes to the remote repository:
    ```sh
    git push -u origin main
    ```

## Preparing the Server

### Installing Git

1. Update the package list:
    ```sh
    sudo apt-get update
    ```

2. Install Git:
    ```sh
    sudo apt-get install git
    ```

### Installing Docker

You can follow the [Docker installation instructions for Ubuntu](https://docs.docker.com/engine/install/ubuntu/) or execute the commands below:

1. Update the package list:
    ```sh
    sudo apt-get update
    ```

2. Install necessary packages:
    ```sh
    sudo apt-get install ca-certificates curl gnupg
    ```

3. Set up Docker keys and repository:
    ```sh
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg

    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    ```

4. Install Docker and plugins:
    ```sh
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

## Running the Application

### Creating a Docker Image

1. Build the application image:
    ```sh
    docker build . --tag fastapi_app
    ```

### Running the Container

1. Run the container with port forwarding:
    ```sh
    docker run -p 80:80 fastapi_app
    ```
