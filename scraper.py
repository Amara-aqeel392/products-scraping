from playwright.sync_api import sync_playwright
import time
import random
import csv




# 🔸 Advanced Human Delay
def random_delay(a=1.5, b=4.5):
    delay = random.uniform(a, b)
    
    # micro pauses (real human jitter)
    if random.random() < 0.3:
        delay += random.uniform(0.2, 1.2)
    
    time.sleep(delay)


# 🔸 Advanced Human Scroll (very realistic)
def human_scroll(page):
    
    total_scrolls = random.randint(4, 8)

    for _ in range(total_scrolls):
        
        # random scroll distance
        scroll_amount = random.randint(300, 1000)
        
        # sometimes small scroll (like user reading)
        if random.random() < 0.3:
            scroll_amount = random.randint(100, 300)

        page.mouse.wheel(0, scroll_amount)
        
        # random pause after scroll
        random_delay(0.8, 2.2)

        # sometimes pause longer (user reading content)
        if random.random() < 0.25:
            time.sleep(random.uniform(2, 5))

    # sometimes scroll slightly up (VERY HUMAN behavior)
    if random.random() < 0.4:
        page.mouse.wheel(0, -random.randint(200, 600))
        random_delay(0.5, 1.5)

def scraper():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False, slow_mo=50)

        context = browser.new_context(
            user_agent=random.choice([
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"
            ]),
            viewport={"width": random.choice([1280, 1366, 1440]), "height": random.choice([720, 768, 900])},
            locale="en-US"
        )

        page = context.new_page()

        # CSV setup
        with open("products.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Price", "Link"])

        # 🔸 Open Amazon
            page.goto("https://www.amazon.com/", wait_until="domcontentloaded", timeout=60000)
            random_delay(3, 6)
            search_box = page.locator("#twotabsearchtextbox")

            search_box.click()
            search_box.fill("")  # clear if needed

            for char in "bags":
                 search_box.type(char, delay=random.randint(100, 200))

            page.keyboard.press("Enter")
            page.wait_for_timeout(10000)
            human_scroll(page)
          
            products = page.locator('div[data-component-type="s-search-result"]')

            count = products.count()
            print("Total product:", count)

# scroll for lazy loading (important for Amazon)
            for _ in range(3):
                  page.mouse.wheel(0, 3000)
                  page.wait_for_timeout(1500)

            for i in range(count):
               try:
                    product = products.nth(i)

       
                    if product.locator("h2 span").count() == 0:
                     continue

        
                    title = product.locator("h2 span").inner_text(timeout=5000)

       
                    price_whole_locator = product.locator(".a-price-whole")
                    price_fraction_locator = product.locator(".a-price-fraction")

                    price_whole = (
                       price_whole_locator.first.inner_text(timeout=3000)
                      if price_whole_locator.count() > 0
                      else ""
                    )

                    price_fraction = (
                        price_fraction_locator.first.inner_text(timeout=3000)
                        if price_fraction_locator.count() > 0
                        else ""
                    )

                    price = price_whole + price_fraction

       
                    
                    link_locator = product.locator("a.a-link-normal.s-no-outline")

                    if link_locator.count() > 0:
                       link = link_locator.first.get_attribute("href", timeout=5000)
                       link = "https://www.amazon.com" + link if link else ""
                    else:
                       link = ""

                    writer.writerow([title, price, link])
               except Exception as e:
                   print(f"Error in product {i}:", e)

        browser.close()

scraper()

