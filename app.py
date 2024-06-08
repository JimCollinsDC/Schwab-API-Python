# https://github.com/JimCollinsDC/Schwab-API-Python
# Examples on how to use the client are in tests/api_demo.py and tests/stream_demo.py
# The schwabdev folder contains code for main operations:
# api.py contains functions relating to api calls, requests, and automatic token checker threads.
# stream.py contains functions for streaming data from websockets.
# terminal.py contains a program for making additional terminal windows and printing to the terminal with color.

# Import the package 
import schwabdev
#Create a client 
client = schwabdev.Client('Your app key', 'Your app secret')

if __name__ == '__main__':
