# Person Generator Microservice
CS 361 Person Generator microservice

Written in Python 3 with Tkinter GUI. This will be a microservice application that will generate personal information for a fictional person(s) using open source information. First commit made during Sprint 3.

### Program Dependencies:

This program uses Pandas, Flask, random, sys, and Tkinter to run. If you have not downloaded these programs please do so before running the program. Random and sys should already be installed if you are running Python 3 or above.

To download Pandas in the command line enter:

`$ pip install pandas`

To download and install Tkinter, in the command line enter:

`$ pip install tkinter`

To download and install Flask, in the command line enter:

`$ pip install flask`


**ALERT:** In order for the program to access the necessary data the information from Kaggle (https://www.kaggle.com/openaddresses/openaddresses-us-west) MUST be downloaded from Kaggle directly (due to size restrictions) and unzipped in the SAME directory as the one you will run the program in. The file the downloaded information is in MUST be named "archive". If the information from Kaggle is not downloaded or in the proper directory the program will not execute properly.
### Run Independently in GUI or Command Line
To run the program from a terminal enter "python" or "python3" then "persongenerator.py" to launch the GUI interface. The _**Submit**_ button will return randomly selected addresses from a selected state. The _**Return**_ button will return the population of a state in a given year from an external microservice.

`$ python persongenerator.py`

If you wish to input a .csv file from the command line enter "python person-generator.py input.csv", the .csv file used for input must have the header [input_state,input_number_to_generate], the program will then skip the GUI and output results directly to `output.csv` in the same directory as the person-generator.py with the header of [input_state,input_number_to_generate,output_content_type,output_content_value].

`$ python persongenerator.py input.csv`

**NOTE:** This method will not work for communicating with an external microservice at this time.

### For HTTP Requests (Communicating with Another Microservice)
To run the microservice in the background you will need _requests_ and _jsonify_ from Flask, if you have already downloaded Flask you do not need to do anything. If you have not, see the above reference for directions on downloading Flask from the command line.
To launch the Person Generator microservice to listen for HTTP requests enter:

`$ flask run -p 6001`

The microservice will then take GET requests and return a JSON response. To test this you can launch any browser and then enter: http://localhost:6001/?state=AK&nums=5
The response in JSON should look like:
`[["input_state","input_number_to_generate","output_content_type","output_content_value"],["AK",5,"Street Address","2147 ASPEN LN HOMER"],["AK",5,"Street Address","35170 SOARING AVE STERLING"],["AK",5,"Street Address","73280 STERLING HWY NINILCHIK"],["AK",5,"Street Address","41347 MONROE ST DIAMOND RIDGE"],["AK",5,"Street Address","50961 RAMONA RD NIKISKI"]]`



