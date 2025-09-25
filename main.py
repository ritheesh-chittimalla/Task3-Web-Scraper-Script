import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    # Target news website
    url = "https://www.bbc.com/news"

    try:
        # Fetch page content
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error if failed
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching the website:", e)
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract headlines (here we use <h2> tags)
    headlines = soup.find_all("h2")

    # Save to file
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for i, headline in enumerate(headlines, 1):
            text = headline.get_text(strip=True)
            if text:  # Avoid empty strings
                f.write(f"{i}. {text}\n")

    print("✅ Headlines scraped and saved to 'headlines.txt'")

if __name__ == "__main__":
    scrape_headlines()
