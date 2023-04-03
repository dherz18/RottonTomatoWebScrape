Rotten Tomatoes TV Show and Movie Scraper

This Python script scrapes the Rotten Tomatoes website to retrieve the top TV shows and movies, then sends an email containing the list of titles. It uses the requests library to send a GET request to the Rotten Tomatoes website and retrieve the HTML content, and the BeautifulSoup library to parse the HTML content and extract the titles of the top TV shows and movies.

The script also uses the smtplib library to send an email containing the list of titles, and the os library to retrieve the sender and recipient email addresses and the email password from environment variables. It uses the schedule library to schedule the script to run every Friday at 6pm.

Prerequisites

Python 3
requests library
BeautifulSoup library
smtplib library
schedule library
Usage

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/rotten-tomatoes-scraper.git
Install the required libraries:
Copy code
pip install requests beautifulsoup4 schedule
Set the following environment variables:
MY_EMAIL: the sender email address
MY_PASSWORD: the email password
RECIPIENT_EMAIL: the recipient email address
Run the script:
Copy code
python rotten_tomatoes_scraper.py
The script will scrape the Rotten Tomatoes website and send an email containing the list of top TV shows and movies every Friday at 6pm.

License

This project is licensed under the MIT License. See the LICENSE file for details.
