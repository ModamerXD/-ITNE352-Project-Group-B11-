# -ITNE352-Project-Group-B11-

-**Project Title**
News API Client-Server System

# Project description
-**Project Description**
An program called the News API Client-Server System enables users to access the NewsAPI service to look for news headlines and sources. The system is scalable and effective for retrieving news in real time because it is designed to support several users.

-**Semester**
 (1 , 2024/2025)


-**Group**

-**Group Name: B11**
-**Course Code: ITNE352**
-**Section: 2**
-**Students:**

-Sayed Ali Shafeeq Alawi - 202209438

-HUSAIN JAMEEL HUSAIN - 202210372


**Table of Contents**
- [Project-Description](#project-description)
- [Requirements](#requirements)
- [How-to-Run](#how-to-run)
- [Scripts](#scripts)
- [Additional-Concepts](#additional-concepts)
- [Acknowledgments](#acknowledgments)
- [Conclusion](#conclusion)


# Requirements
-**Requirements**
-**need Python 3.8 or higher installed:**

-**python packages**
- 'socket'
-'threading'
-'requests'
-'json'
-'os'
-'tkinter or tk'
-'you must have a NewsAPI API key. You can get it by creating an account on NewsAPI.'

# How to run
-**how to run**

- Start the server - 
Running the server by python server.py

the server will:
Accept client connection and will display the Accepted form with the client name 
like: Accepted connection from Hussain
save responses in JSON

- Start the client -
Running the client by python Client.py
Follow the menu options to interact with the server:

# Scripts
**The scripts**
- First enter your name
- 1 for Search by headlines , 
- 2 for List for sources.
- 3 Quit

Then you should choose how you want toe search 1 for Search by keywords ,  2 for Search by category ,  
3 for Search by country  , 4 for List all new headlines and 5 for Back to main menu.

You can search multiple time , and if you finish you can back to main menu and choose Quit option .

 
- Scripts Overview -
Server Script (`server.py`)

-**Purpose:**  
  Handles client connections and fetches news data using the NewsAPI.

- Key Functionalities:  
  - Accepts and handles multiple client connections using multithreading.  
  - Processes client requests for news headlines and sources.  
  - Saves retrieved data in JSON files for testing and evaluation.  


Client Script (`client.py`)

- Purpose:  
  Provides a user-friendly interface to interact with the server.

-Key Functionalities:  
  - Displays categorized menus for news browsing.  
  - Sends requests to the server and processes responses.

# Additional concepts
-**Addintional concept (GUI)** 
you should run the Client by (python Client_gui.py)
First you have to enter your name . 

Will display the gui page for client menu option ,you should choose if you want to search of by headlines for the new or list sources to list the sources , or choose Quit to leave .

Then you should choose how you want to search by keyword , category , country and back to main menue to return to the main page.
If you choose keyword you should enter the keyword you want to search about it , and if you choose category you should choose from the categories , and if you choose country you should choose the country you want and you .

If you finish you can just close the GUI to terminate the session

# Acknowledgement
**Acknowledgments**
(Instructor: Dr. Mohammed Almeer)
- Dr. Mohammed Almeer's constant support and outstanding advice throughout this project and the semester are greatly appreciated. His wise counsel and support have been essential to our educational process, motivating us to overcome obstacles and achieve excellence in our work. Dr. Almeer, your commitment to creating a cooperative and stimulating learning atmosphere has been really motivating, and we are incredibly appreciative of the beneficial influence you have had on our academic development.
(University of Bahrain)

# Conclusion
**Conclusion**
This project showcases the development of a client-server application in Python using socket programming and multi-threading to interact with external APIs. It efficiently retrieves and serves real-time news data, demonstrating scalable and interactive client-server architecture.
