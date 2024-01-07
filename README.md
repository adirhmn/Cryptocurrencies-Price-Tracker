# Cryptocurrencies Price Tracker Api
Cryptocurrencies Price Tracker is a rest api application for storing coin price data. Coin prices are obtained from https://api.coincap.io/v2/assets.
- You can access this api using [https://cryptopricetracker.fly.dev](https://github.com/adirhmn/cryptocurrencies-price-tracker/tree/main/documentation) and you can check health app by access [https://cryptopricetracker.fly.dev/health](https://cryptopricetracker.fly.dev/health)
- Documentation [Here](https://github.com/adirhmn/cryptocurrencies-price-tracker/tree/main/documentation)
- Postman Collection [Here](https://github.com/adirhmn/cryptocurrencies-price-tracker/blob/main/Crypto%20Price%20Tracker%20Api.postman_collection.json)

# How to Running Project
## Prerequisites

Before you begin, make sure you have Git installed on your computer. If not, you can download and install it from the [official Git website](https://git-scm.com/).

## Clone Project Github

1. **Copy Repository URL**

   On the repository page, look for the `Code` or `Clone` button located at the top right. Click on the button and copy the displayed URL (usually in HTTPS or SSH format).

2. **Open Terminal**

   Open the terminal or command prompt on your computer.

3. **Navigate to Destination Directory**

   Use the `cd` command to navigate to the directory where you want to store the project. For example:

   ```bash
   cd path/to/destination/directory
   ```

4. **Clone Repository**

   Type the following command to clone the repository:

   ```bash
   git clone [Repository URL]
   ```

   Replace `[Repository URL]` with the URL

   ```bash
   git clone https://github.com/adirhmn/cryptocurrencies-price-tracker
   ```

5. **Done!**

   The project has now been successfully cloned to your computer. You can start working or exploring the code of the project.

## Run Application Using Docker Compose

6. **Navigate to Project Directory**

   After cloning the repository, navigate to the project directory:

   ```bash
   cd repository-directory
   ```

7. **Start Docker Compose**

   - Make sure Docker is installed and running on your system.
     Run the following command to start the application using Docker Compose:

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images and start the containers in detached mode.
   Congratulations your app has been running at `http://localhost:8000` and you can checking health app by access `http://localhost:8000/health` and you will get response

   ```
   {
       "status": "success",
       "message": "App running well"
   }
   ```

### Test the Application Using Postman

This app has 6 endpoint

- Sign Up
- Sign In
- Sign Out
- Add coin to tracker
- Show user list of tracked coins
- Remove coin from tracker

##### Sign Up

1. **Open Postman**

   - Ensure you have installed and opened the Postman application on your computer.

2. **Select Request Method**
   - At the top, select "POST" from the HTTP method dropdown menu.
3. **Enter URL**

   - In the URL bar, input `http://localhost:8000/signup/`.
   - You can change to production app url `https://cryptopricetracker.fly.dev/signup/`

4. **Set Request Body**

   - Below the URL, click on the "Body" tab.
   - Choose the "raw" option and select the format "JSON (application/json)".
   - Input the following data into the body section (example):

   ```json
   {
     "email": "johndoe@gmail.com",
     "password": "password1*",
     "password_confirm": "password1*"
   }
   ```

5. **Send Request**

   - Click the "Send" button located to the right of the URL bar to send your request to the server.

6. **Check Response**
   - After sending the request, you will see the server's response below the section where you input the body like this.
   ```json
   {
     "code": 200,
     "status": "success",
     "data": {
       "email": "johndoe@gmail.com"
     }
   }
   ```
   - Ensure the response indicates successful registration or displays an error message if any issues occur.

##### Sign In

1. **Open Postman**

   - Ensure you have installed and opened the Postman application on your computer.

2. **Select Request Method**
   - At the top, select "POST" from the HTTP method dropdown menu.
3. **Enter URL**

   - In the URL bar, input `http://localhost:8000/signin/`.
   - You can change to production app url `https://cryptopricetracker.fly.dev/signin/`

4. **Set Request Body**

   - Below the URL, click on the "Body" tab.
   - Choose the "raw" option and select the format "JSON (application/json)".
   - Input the following data into the body section (example):

   ```json
   {
     "email": "johndoe@gmail.com",
     "password": "password1*"
   }
   ```

5. **Send Request**

   - Click the "Send" button located to the right of the URL bar to send your request to the server.

6. **Check Response**
   - After sending the request, you will see the server's response below the section where you input the body like this.
   ```json
   {
     "code": 200,
     "status": "success",
     "data": {
       "email": "johndoe@gmail.com",
       "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lQGdtYWlsLmNvbSIsImV4cCI6MTcwNDYzODIwNX0.GuV3cUW-WbarPp_Qal1czpg061e7FGF_C3Yg6NZoSyc"
     }
   }
   ```
   - There is a `token` field in the response that will be used as an access token for the next api.

##### Sign Out

1. **Select Request Method**
   - At the top, select "GET" from the HTTP method dropdown menu.
2. **Enter URL**

   - In the URL bar, input `http://localhost:8000/signout/`.
   - You can change to production app url `https://cryptopricetracker.fly.dev/signout/`

3. **Set Authorization Header**

   - Go back to the "Headers" tab in Postman.
   - Add a new key-value pair:
     - Key: `Authorization`
     - Value: `Bearer YOUR_AUTH_TOKEN` (Replace `YOUR_AUTH_TOKEN` with the `token` you receive from signin response).

4. **Send Request**

   - Click the "Send" button located to the right of the URL bar to send your request to the server.

5. **Check Response**
   - After sending the request, you will see the server's response below the section where you input the body like this.
   ```json
   {
     "code": 200,
     "status": "success",
     "data": "johndoe@gmail.com success signout"
   }
   ```

##### Add coin to tracker

1. **Select Request Method**
   - At the top, select "POST" from the HTTP method dropdown menu.
2. **Enter URL**

   - In the URL bar, input `http://localhost:8000/tracker/{COIN_ID}`.
   - Replace `COIN_ID` with id coin from coin cap `https://api.coincap.io/v2/assets`.
   - For example `http://localhost:8000/tracker/bitcoin`.

3. **Set Authorization Header**

   - Go back to the "Headers" tab in Postman.
   - Add a new key-value pair:
     - Key: `Authorization`
     - Value: `Bearer YOUR_AUTH_TOKEN` (Replace `YOUR_AUTH_TOKEN` with the `token` you receive from signin response).

4. **Send Request**

   - Click the "Send" button located to the right of the URL bar to send your request to the server.

5. **Check Response**
   - After sending the request, you will see the server's response below the section where you input the body like this.
   ```json
   {
     "code": 200,
     "status": "success",
     "data": [
       {
         "name": "Bitcoin",
         "priceIdr": 689065860.2108535
       }
     ]
   }
   ```

##### Show user list of tracked coins

1. **Select Request Method**
   - At the top, select "GET" from the HTTP method dropdown menu.
2. **Enter URL**

   - In the URL bar, input `http://localhost:8000/tracker/`.
   - - You can change to production app url `https://cryptopricetracker.fly.dev/tracker/`.

3. **Set Authorization Header**

   - Go back to the "Headers" tab in Postman.
   - Add a new key-value pair:
     - Key: `Authorization`
     - Value: `Bearer YOUR_AUTH_TOKEN` (Replace `YOUR_AUTH_TOKEN` with the `token` you receive from signin response).

4. **Send Request**

   - Click the "Send" button located to the right of the URL bar to send your request to the server.

5. **Check Response**
   - After sending the request, you will see the server's response below the section where you input the body like this.
   ```json
   {
     "code": 200,
     "status": "success",
     "data": [
       {
         "name": "Bitcoin",
         "priceIdr": 689065860.2108535
       }
     ]
   }
   ```

##### Remove coin from tracker

1. **Select Request Method**
   - At the top, select "DELETE" from the HTTP method dropdown menu.
2. **Enter URL**

   - In the URL bar, input `http://localhost:8000/tracker/{COIN_ID}`.
   - Replace `COIN_ID` with id coin name from your tracker.
   - For example `http://localhost:8000/tracker/bitcoin`.
   - - You can change to production app url `https://cryptopricetracker.fly.dev/tracker/bitcoin`

3. **Set Authorization Header**

   - Go back to the "Headers" tab in Postman.
   - Add a new key-value pair:
     - Key: `Authorization`
     - Value: `Bearer YOUR_AUTH_TOKEN` (Replace `YOUR_AUTH_TOKEN` with the `token` you receive from signin response).

4. **Send Request**

   - Click the "Send" button located to the right of the URL bar to send your request to the server.

5. **Check Response**
   - After sending the request, you will see the server's response below the section where you input the body like this.
   ```json
   {
     "code": 200,
     "status": "success",
     "data": "bitcoin success deleted"
   }
   ```

## How to Run API Testing Using Docker

### Steps:

1. **Open a New Terminal**

   - Launch a new terminal window or tab on your computer.
   - Make sure Docker is running on your system.

2. **List Running Containers**

   - In the terminal, execute the command:
     ```
     docker container ls
     ```
   - You will see a response similar to the following example:
     ```
     CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                    NAMES
     bfd5edbd157b   app-web   "sh -c 'uvicorn main…"   40 minutes ago   Up 25 minutes   0.0.0.0:8000->8000/tcp   app-web-1
     ```
   - Note down `IMAGE` name from the list. In this example, the `IMAGE` is `app-web`.

3. **Run Testing Command**

   - Replace `{IMAGE_NAME}` with the actual image name (from step 2) in the following command:
     ```
     docker run {IMAGE_NAME} sh -c "pytest"
     ```
   - For example, if your image name is `app-web`, the command will be:
     ```
     docker run app-web sh -c "pytest"
     ```
   - Execute the command in the terminal to run the API tests inside the Docker container.

4. **Observe Test Results**
   - The terminal will display the output of the tests. Ensure all tests pass and check for any error messages or failures.
