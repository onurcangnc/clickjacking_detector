from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Define color-coded symbols and full messages
INFO = f"{Fore.GREEN}-> {Style.RESET_ALL}"
NEGATIVE = f"{Fore.RED}[-]{Style.RESET_ALL}"
POSITIVE = f"{Fore.GREEN}[+]{Style.RESET_ALL}"

DETECTED_GREEN = f"{Fore.GREEN}[+] Potential clickjacking detected: The page rendered within the iframe.{Style.RESET_ALL}"
NOT_DETECTED_RED = f"{Fore.RED}[-] No clickjacking detected ! ! !{Style.RESET_ALL}"

# Function to test a single URL for clickjacking
def test_url_for_clickjacking(website_url):
    print(f"{INFO} Testing {website_url}")

    # Check headers for clickjacking protection
    try:
        response = requests.get(f"https://{website_url}")
        headers = response.headers
        
        # Check for X-Frame-Options or Content-Security-Policy headers
        if 'X-Frame-Options' in headers:
            print(f"{NEGATIVE} Clickjacking protection detected: X-Frame-Options = {headers['X-Frame-Options']}")
        elif 'Content-Security-Policy' in headers and "frame-ancestors" in headers['Content-Security-Policy']:
            print(f"{NEGATIVE} Clickjacking protection detected: Content-Security-Policy = {headers['Content-Security-Policy']}")
        else:
            # Proceed with iframe testing if no protection headers are found
            print(f"{NEGATIVE} No explicit clickjacking protection headers detected. Proceeding with iframe test...")

            # Use the exact template provided by the user
            html_content = f"""
            <style>
                iframe {{
                    position:relative;
                    width:1000px;
                    height: 800px;
                    opacity: 0.5;
                    z-index: 2;
                }}
                div {{
                    position:absolute;
                    top:300px;
                    left:60px;
                    z-index: 1;
                }}
            </style>
            <div>Buraya Tıklayınız</div>
            <iframe src="https://{website_url}"></iframe>
            """

            # Write HTML content to a temporary file with UTF-8 encoding
            with open("clickjacking_test.html", "w", encoding="utf-8") as file:
                file.write(html_content)

            # Initialize WebDriver
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

            # Get the absolute path of the generated HTML file and add file:/// prefix
            file_path = "file:///" + os.path.abspath("clickjacking_test.html")
            driver.get(file_path)  # Open the local HTML file

            # Allow time for the page to load
            time.sleep(2)

            # Check for the presence and loading status of the iframe
            try:
                iframe = driver.find_element(By.TAG_NAME, "iframe")
                driver.switch_to.frame(iframe)

                # Check if the iframe content is loaded by looking for any visible text
                body_content = driver.find_element(By.TAG_NAME, "body").text
                if body_content.strip():
                    print(DETECTED_GREEN)  # Display in green if clickjacking is detected
                else:
                    print(NOT_DETECTED_RED)  # Display in red if no clickjacking detected
                    
            except (NoSuchElementException, TimeoutException):
                print(NOT_DETECTED_RED)  # Display in red if no content is loaded in the iframe

            # Close WebDriver
            driver.quit()
            
    except requests.RequestException as e:
        print(f"{NEGATIVE} Failed to connect to the website: {e}")


# Main script to handle user input
def main():
    choice = input(f"{INFO} Would you like to test multiple URLs from a file or a single URL? (file/single): ").strip().lower()
    
    if choice == "file":
        # Ask for the file name in the current directory
        file_name = input(f"{INFO} Enter the filename (e.g., url.txt) in the current directory: ").strip()
        file_path = os.path.join(os.getcwd(), file_name)
        
        try:
            with open(file_path, "r") as file:
                urls = [line.strip() for line in file if line.strip()]
            print(f"{INFO} Loaded {len(urls)} URLs from {file_name}")
            for url in urls:
                test_url_for_clickjacking(url)
        except FileNotFoundError:
            print(f"{NEGATIVE} File not found: {file_name}")
    elif choice == "single":
        # Ask for a single URL
        website_url = input(f"{INFO} Enter the website URL to test for clickjacking: ").strip()
        test_url_for_clickjacking(website_url)
    else:
        print(f"{NEGATIVE} Invalid choice. Please enter 'file' or 'single'.")

# Run the main function
if __name__ == "__main__":
    main()
