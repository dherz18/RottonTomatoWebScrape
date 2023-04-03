Rotten Tomatoes TV Show and Movie Scraper

This Python script scrapes the Rotten Tomatoes website to retrieve the top TV shows and movies, then sends an email containing the list of titles. It uses the requests library to send a GET request to the Rotten Tomatoes website and retrieve the HTML content, and the BeautifulSoup library to parse the HTML content and extract the titles of the top TV shows and movies.

The script also uses the smtplib library to send an email containing the list of titles, and the os library to retrieve the sender and recipient email addresses and the email password from environment variables. It uses the schedule library to schedule the script to run every Friday at 6pm.

- Prerequisites
  - Python 3
  - Requests
  - BeautifulSoup
  - smtplib
  - Schedule

Getting Started  

1. Clone the repository to your local machine!![Screenshot 2023-04-03 at 4 27 31 PM](https://user-images.githubusercontent.com/121212892/229634989-0bc609c6-ce7c-441f-a05f-a583bd9f93dc.JPG)

2. Set up your email credentials as environment variables!![Screenshot 2023-04-03 at 4 28 11 PM](https://user-images.githubusercontent.com/121212892/229635001-e2d9a2de-e117-4c8a-acce-bc67a448ffba.JPG)

3. Run the script![Screenshot 2023-04-03 at 4 28 33 PM](https://user-images.githubusercontent.com/121212892/229635011-8cf1533c-4dd9-4793-b856-d6e079a40763.JPG)


