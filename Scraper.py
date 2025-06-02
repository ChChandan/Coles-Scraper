from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
import time
import random
import numpy as np

class HumanLikeScraper:
    def __init__(self):
        # Configure browser options to look more like a regular user
        options = webdriver.SafariOptions()
        # options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        
        self.driver = webdriver.Safari(options=options)
        self.itemlist = {}
        
        # Configure human-like behavior parameters
        self.min_delay = 1.5
        self.max_delay = 5.0
        self.scroll_variations = [100, 200, 300, 400, 500]
        
    def random_delay(self):
        """Random delay between actions to mimic human reading/thinking time"""
        delay = random.uniform(self.min_delay, self.max_delay)
        time.sleep(delay)
        
    def random_mouse_movement(self):
        """Generate random mouse movements to mimic human behavior"""
        actions = ActionChains(self.driver)
        
        # Generate random movement pattern
        for _ in range(random.randint(2, 5)):
            x_offset = random.randint(-50, 50)
            y_offset = random.randint(-50, 50)
            actions.move_by_offset(x_offset, y_offset)
            
        # Sometimes click randomly
        if random.random() < 0.3:
            actions.click()
            
        actions.perform()
        
    def human_scroll(self):
        """Scroll the page in a human-like manner"""
        scroll_distance = random.choice(self.scroll_variations)
        if random.random() < 0.7:
            # Normal scroll
            self.driver.execute_script(f"window.scrollBy(0, {scroll_distance})")
        else:
            # Sometimes use page down key
            body = self.driver.find_element(By.TAG_NAME, 'body')
            body.send_keys(Keys.PAGE_DOWN)
            
        self.random_delay()
        
    def scroll_to_element(self, element):
        """Scroll to element with human-like variation"""
        # First scroll near the element
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", 
            element
        )
        
        # Random small adjustment
        self.driver.execute_script(
            f"window.scrollBy(0, {random.randint(-100, 100)})"
        )
        
        self.random_delay()
        
    def scrape_page(self, url):
        """Scrape a single page with human-like behavior"""
        try:
            # Random delay before loading page
            self.random_delay()
            
            # Navigate to URL
            self.driver.get(url)
            
            # Random mouse movements after page load
            self.random_mouse_movement()
            
            # Human-like scrolling pattern
            for _ in range(random.randint(2, 4)):
                self.human_scroll()
                
            # Wait for elements with some randomness
            wait_time = random.uniform(5, 10)
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product__title"))
            )
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "price__value"))
            )
            
            # Get elements
            titles = self.driver.find_elements(By.CLASS_NAME, "product__title")
            prices = self.driver.find_elements(By.CLASS_NAME, "price__value")
            
            # Process each product with human-like delays
            for title, price in zip(titles, prices):
                # Scroll to element in a human-like way
                self.scroll_to_element(title)
                
                title_text = title.text.strip()
                price_text = price.text.strip()
                print(f"{title_text} - {price_text}")
                self.itemlist[title_text] = price_text
                
                # Random delay between items
                if random.random() < 0.7:
                    self.random_delay()
                    
            # Save progress intermittently
            if random.random() < 0.3:
                self.save_to_csv()
                
            return True
            
        except Exception as e:
            print(f"Error scraping page: {e}")
            # Random delay before retrying or continuing
            time.sleep(random.uniform(5, 10))
            return False
        
    def save_to_csv(self):
        """Save data to CSV file"""
        with open('coles_products.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Product Title', 'Price'])
            for title, price in self.itemlist.items():
                writer.writerow([title, price])
                
    def run(self, start_page, end_page):
        """Run the scraper for a range of pages"""
        try:
            for page in range(start_page, end_page + 1):
                print(f"Scraping page {page}...")
                url = f"https://www.coles.com.au/browse/meat-seafood?pid=homepage_cat_explorer_meat_seafood&page={page}"
                
                # Try scraping the page (with retries)
                success = False
                for attempt in range(3):  # Max 3 attempts per page
                    if self.scrape_page(url):
                        success = True
                        break
                    print(f"Retrying page {page} (attempt {attempt + 1})")
                
                if not success:
                    print(f"Failed to scrape page {page} after multiple attempts")
                    
                # Random longer delay between pages
                time.sleep(random.uniform(5, 15))
                
        finally:
            # Ensure data is saved and browser is closed
            self.save_to_csv()
            self.driver.quit()

# Run the scraper
if __name__ == "__main__":
    scraper = HumanLikeScraper()
    scraper.run(2, 9)  # Scrape pages 2-9