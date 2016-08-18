
# Stress level vs time for Onyx Data
This  application is to visualize the stress level based on the rri data from the redshift data warehouse. The rmssd is calculated to represent the heart rate variablity.

## How to use
### Structure

1. index.js is the nodejs server hosting the static files and works as a proxy as well.
2. jsonserver.py is the python code that handles RPC request and connects to database.
3. app/src/stressness.html is the web app
4. output.json is the initial load of vis data
5. The root directory is under app/


## Install
This is for **Mac OS** at the current stage.
### Node.js
    $ npm install http-proxy --save
    $ npm install express --save
### Python
##### Install pip
	$ sudo easy_install pip
##### Install Werkzeug
	$ sudo easy_install Werkzeug
##### Install JSON-RPC
	$ sudo pip install json-rpc
##### Install numpy
	$ sudo pip install numpy
##### Install scikit-learn
	$ sudo pip install -U scikit-learn
##### Install scipy
	$ sudo apt-get install python-scipy
## Basic usage
### Start the python service
	$ python jsonserver.py
Then the Python service will be running at localhost:4010. You can change the port in the source code if port4010 is not available.
### Start the Node.js service
	$ node index.js
The express server is started ans listening on port 3000. The root directory is app/*.
### Open the web app
Open http://localhost:3000/src/stressness.html from the browser.




