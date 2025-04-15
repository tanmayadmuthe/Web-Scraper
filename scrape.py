from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException
from bs4 import BeautifulSoup, Comment


def scrape_website(website):
    try:
        print("Launching Chrome WebDriver...")
        options = Options()
        options.add_argument("--headless")  # Optional: remove this if you want to see browser
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        with webdriver.Chrome(options=options) as driver:
            driver.get(website)
            print("Page loaded. Scraping page content...")
            return driver.page_source
    except (WebDriverException, TimeoutException) as e:
        print(f"[ERROR] Failed to scrape {website}: {e}")
        return ""


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for tag in soup(["script", "style"]):
        tag.extract()

    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    chunks = [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
    print(f"Split DOM content into {len(chunks)} chunk(s).")
    return chunks
