# 📖 Project Description – Web Scraper for News Headlines

This project is a Python-based web scraper that collects the latest news headlines from a public news website. Using the requests library, the scraper fetches the HTML content of the webpage, and BeautifulSoup is used to parse and extract relevant text (such as <h2> headline tags). The collected headlines are then stored in a .txt file for easy access and analysis.

The main purpose of this project is to demonstrate web scraping automation, where repetitive data collection tasks are replaced by a simple Python script. This allows users to stay updated with fresh news headlines without manually visiting multiple websites.

✨ Key Features

Fetches HTML content of a news website using requests

Extracts top news headlines with BeautifulSoup

Stores the headlines in a clean format inside a text file

Simple and lightweight script with minimal dependencies

Can be easily modified to scrape multiple websites or different tags

🎯 Objective

The objective of this project is to automate the collection of news headlines from the web, making it easier for users to gather real-time information for personal use, analysis, or research.

⚙️ Tools & Technologies

Python (programming language)

Requests (for fetching HTML content)

BeautifulSoup (for parsing HTML and extracting text)

📂 Deliverables

Python Script (main.py) → Runs the scraper

Text File (headlines.txt) → Stores the extracted news headlines

📊 Outcome

With this project, the process of visiting news websites and copying headlines is automated. The script can be scheduled to run periodically (using task schedulers like cron jobs or Windows Task Scheduler) to always keep the collected headlines up-to-date.
