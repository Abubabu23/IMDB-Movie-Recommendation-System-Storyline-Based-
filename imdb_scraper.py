from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os

driver = webdriver.Chrome()
driver.get("https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31")

wait = WebDriverWait(driver, 40)

csv_file = "movie_data.csv"

# Existing CSV load (to avoid duplicates)
if os.path.exists(csv_file):
    df_existing = pd.read_csv(csv_file)
    existing_titles = set(df_existing["Title"].tolist())
else:
    df_existing = pd.DataFrame(columns=["Title", "Storyline"])
    existing_titles = set()

print("Started scraping...\n")


def extract_movies():
    """Extract movies currently visible on the page (no duplicates)."""
    cards = driver.find_elements(By.XPATH, '//li[contains(@class,"ipc-metadata-list-summary-item")]')
    batch_data = []

    for card in cards:
        try:
            title = card.find_element(By.XPATH, './/h3').text.strip()
        except:
            title = ""

        try:
            story = card.find_element(By.XPATH, './/div[contains(@class, "ipc-html-content-inner-div")]').text.strip()
        except:
            story = ""

        # skip duplicates
        if title in existing_titles:
            continue

        existing_titles.add(title)
        batch_data.append([title, story])

    return batch_data


# ------------ MAIN LOOP ------------
while True:

    # Step 1: Extract movies from current view
    batch = extract_movies()

    if batch:
        print(f"✔ Extracted {len(batch)} new movies")

        # Append to CSV
        df_batch = pd.DataFrame(batch, columns=["Title", "Storyline"])
        df_batch.to_csv(csv_file, mode='a', header=not os.path.exists(csv_file), index=False)
    else:
        print("No new movies found in this batch.")

    # Step 2: Scroll
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

    # Step 3: Try clicking Load More
    try:
        load_more = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/div[2]/div/span/button/span/span'))
        )
        driver.execute_script("arguments[0].click();", load_more)
        print("→ Load More clicked\n")
        time.sleep(5)

    except Exception:
        print("\n✔ No more Load More. Scraping finished.")
        break


driver.quit()

print("\n🎉 Completed scraping all movies WITHOUT duplicates.")
