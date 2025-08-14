from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Setup headless Chrome browser
options = Options()
options.add_argument("--headless")  # comment this out if you want to see the browser
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

# List of keywords to search
keywords = ["necklace", "bracelet", "earrings", "anklet"]

# Lists to store the scraped data
all_names = []
all_prices = []
all_images = []
all_categories = []

for keyword in keywords:
    print(f"🔍 Scraping category: {keyword}")
    driver.get(f"https://www.snapdeal.com/search?keyword={keyword}")
    time.sleep(5)  # Wait for page to load

    # Scroll to load images
    for _ in range(2):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

    products = driver.find_elements(By.CSS_SELECTOR, "div.product-tuple-listing")[:5]

    for product in products:
        try:
            name = product.find_element(By.CLASS_NAME, "product-title").text
            price = product.find_element(By.CLASS_NAME, "product-price").text
            image = product.find_element(By.TAG_NAME, "img").get_attribute("src")

            all_categories.append(keyword)
            all_names.append(name)
            all_prices.append(price)
            all_images.append(image)

        except Exception as e:
            print("⚠️ Error while scraping a product:", e)
            continue

# Close the browser
driver.quit()

# Save to Excel
df = pd.DataFrame({
    "Category": all_categories,
    "Product Name": all_names,
    "Price": all_prices,
    "Image URL": all_images
})

file_name = "snapdeal_products_limited.xlsx"
df.to_excel(file_name, index=False)
print(f"✅ Scraped data saved to '{file_name}'")
