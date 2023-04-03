import requests
from bs4 import BeautifulSoup
import smtplib
import os
import schedule
import time

# Scrape Rotten Tomatoes website for top TV shows and movies
def hot_tv():
    global topShows
    global top_show_titles

    # URL of the Rotten Tomatoes website
    URL = "https://www.rottentomatoes.com/"

    # Send a request to the website and retrieve the HTML content
    page = requests.get(URL).text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(page, "html.parser")

    # Find all the elements with class "dynamic-text-list__item-title clamp clamp-1", which contains the titles of top TV shows and movies
    topShows = soup.find_all(
        "span",
        class_="dynamic-text-list__item-title clamp clamp-1",
    )

    # Extract the titles from the elements and add them to a list
    top_show_titles = []
    for show in topShows:
        show.get_text().strip()
        top_show_titles.append(show.text)

    # Print the list of top TV shows and movies
    print(top_show_titles)

    # Send the list of top TV shows and movies via email
    send_mail(top_show_titles)


# Send an email containing the list of top TV shows and movies
def send_mail(top_show_titles):
    new_line = "\n"

    # Set up the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Get the email address and password from environment variables
    email = os.environ.get("MY_EMAIL")
    password = os.environ.get("MY_PASSWORD")
    server.login(email, password)

    # Set the subject and body of the email
    subject = "Best TV/Movies out right now!"
    body = f"Here are the top TV shows and movies on Rotten Tomatoes: {new_line}{new_line}{chr(10).join(top_show_titles[:10])}{new_line}{new_line}TV{new_line}{new_line}{chr(10).join(top_show_titles[11:20])}{new_line}{new_line}Check it out here: {URL}"

    # Construct the email message
    msg = f"Subject: {subject}\n\n{body}"

    # Get the recipient email address from environment variables and send the email
    recipient_email = os.environ.get("MY_EMAIL")
    server.sendmail(email, recipient_email, msg)

    # Print a message to confirm that the email has been sent
    print("Email has been sent!")

    # Close the SMTP server connection
    server.quit()


# Schedule the hot_tv function to run every Friday at 6pm
schedule.every().friday.at("18:00").do(hot_tv)

# Run the script indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
