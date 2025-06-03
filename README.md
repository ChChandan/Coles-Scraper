# Coles website price scrapper

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange)
![Web Scraping](https://img.shields.io/badge/Web-Scraping-green)

A Python-based web scraper that extracts meat and seafood product data from Coles Australia's website with human-like behavior to avoid detection.

## Features

- **Human-like interactions** with randomized delays, mouse movements, and scrolling patterns
- **Anti-detection techniques** to bypass WAF protections like Imperva
- **CSV output** for easy data analysis
- **Automatic retries** for failed requests
- **Configurable** for different product categories and page ranges

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/coles-web-scraper.git
   cd coles-web-scraper
   ```

2. Install the required dependencies:
   ```bash
   pip install selenium numpy
   ```

3. Download the appropriate WebDriver for your browser (Safari, Chrome, or Firefox) and ensure it's in your PATH.

## Usage

```python
from scraper import HumanLikeScraper

# Initialize and run the scraper
scraper = HumanLikeScraper()
scraper.run(start_page=2, end_page=9)  # Scrape pages 2-9
```

### Configuration Options

You can modify these parameters in the `HumanLikeScraper` class:

- `min_delay`/`max_delay`: Adjust the range of random delays between actions
- `scroll_variations`: Change scroll distances for more natural behavior
- Page range: Set which pages to scrape in the `run()` method

## Output

The scraper saves data to `coles_products.csv` with the following format:

```
Product Title,Price
Beef Mince Premium 500g,$9.50
Atlantic Salmon Portions 400g,$12.00
...
```

## Anti-Detection Techniques

This scraper implements several methods to avoid blocking:

1. Randomized delays between actions
2. Human-like mouse movements
3. Natural scrolling patterns
4. Randomized request timing
5. Automatic retries for failed requests

## Limitations

- Coles may update their website structure, requiring selector updates
- Heavy scraping may still trigger protections
- Requires maintenance as anti-bot systems evolve

## Contributing

Contributions are welcome! Please open an issue or pull request for:
- Bug fixes
- Additional anti-detection techniques
- Performance improvements
- Enhanced data processing

## Legal Notice

This project is for educational purposes only. Please review Coles' Terms of Service and robots.txt before use. The maintainers are not responsible for any misuse of this tool.

## License

MIT License - See [LICENSE](LICENSE) file for details.
