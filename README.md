Project title: World Currency Converter

Overview of the project:-

This is a command-line Python application that calculates live currency exchange rates using the Frankfurter API. It provides a simple terminal interface for users to check rates, browse supported currencies, and track their conversion history during the session.

Features:-

•	Fetches real-time exchange rate data via HTTP requests.
•	Displays a dictionary of global currencies alongside their standard symbols.
•	Maintains a timestamped session history of all conversion
•	Includes validation for user inputs and error handling for network timeouts.

Technologies/tools used:-

    Python 3.x
    requests module
    datetime module
    Frankfurter API

Steps to install & run the project:-

•	Clone this repository to your local machine.
•	Ensure Python 3 is installed.
•	Install the required external library by running: pip install requests
•	Run the script from your terminal: python main.py
  

   Instructions for testing:-

•	Launch the script and select option 1 from the main menu.
•	Input valid currency codes (e.g., USD to JPY) and a positive amount. Verify the math matches the printed exchange rate.
•	Input an invalid currency code (e.g., XXX) to ensure the system catches the invalid input and returns you to the menu.
•	Input a negative amount to verify the negative value constraint works.
•	Disconnect your internet and attempt a conversion to trigger and verify the requests.exceptions.RequestException network error       handling.

