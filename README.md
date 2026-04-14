# 🛒 Amazon Product Scraper (Playwright + Python)

A **production-style web scraping project** built with Playwright that extracts product data from Amazon search results using **human-like automation techniques**.

---

## 🚀 Features

* 🔍 Automated product search (Amazon)
* 🤖 Human-like behavior (random delays, scrolling, typing)
* 📦 Extracts:

  * Product Title
  * Product Price
  * Product URL
* 🧠 Handles dynamic content (lazy loading)
* ⚠️ Error-safe extraction (try/except handling)
* 📁 Saves clean structured data to CSV
* 🧹 Filters incomplete or broken products

---

## 🧰 Tech Stack

* Python
* Playwright
* CSV (data storage)

---

## 📂 Project Structure

```
amazon-scraper/
│── scraper.py
│── products.csv
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/amazon-scraper.git
cd amazon-scraper
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Install Playwright browsers

```
playwright install
```

---

## ▶️ Usage

Run the scraper:

```
python scraper.py
```

The script will:

1. Open Amazon
2. Search for a product (default: `"bags"`)
3. Scroll like a human
4. Extract product data
5. Save results in `products.csv`

---

## 📊 Output Example

| Title                 | Price | URL                        |
| --------------------- | ----- | -------------------------- |
| Laptop Bag Waterproof | 29.99 | https://amazon.com/dp/XXXX |
| Travel Duffel Bag     | 45.50 | https://amazon.com/dp/YYYY |

---

## 🧠 How It Works

* Uses Playwright to control a real browser
* Simulates human behavior:

  * Random typing delays
  * Scrolling patterns
  * Natural pauses
* Targets structured product containers:

```
div[data-component-type="s-search-result"]
```

---

## ⚠️ Disclaimer

This project is created for **educational purposes only**.

* It does **not** intend to violate any website’s Terms of Service
* Do **not** use this for large-scale or commercial scraping
* Always respect website policies and robots.txt

---

## 🔮 Future Improvements

* Pagination support (multiple pages)
* Proxy rotation
* CAPTCHA handling
* Product filtering (price, rating, etc.)
* Database integration (MongoDB / PostgreSQL)

---

## 👩‍💻 Author

**Amara Aqeel**

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
