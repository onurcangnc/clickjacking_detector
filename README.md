# Clickjacking Detection Tool

This is a Python-based tool designed to detect clickjacking vulnerabilities on websites. It utilizes `Selenium` to simulate potential clickjacking scenarios, `Requests` for analyzing HTTP headers, and `Colorama` to display color-coded results in the terminal. The tool is user-friendly and allows users to either test a single URL or load multiple URLs from a text file for batch testing.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Features
- **Single or Multiple URL Testing**: Choose to test a single URL manually or load multiple URLs from a text file.
- **Automated Header Checks**: Automatically detects common anti-clickjacking headers such as `X-Frame-Options` and `Content-Security-Policy`.
- **Iframe Testing**: If no anti-clickjacking headers are found, the tool tries to load the page inside an iframe to simulate a clickjacking attack.
- **Color-Coded Output**: Easy-to-read, color-coded output in the console:
  - Green for detected vulnerabilities.
  - Red for protected pages.
- **Beginner-Friendly**: Straightforward prompts and guided steps.

## Installation
To set up the clickjacking detection tool:

1. **Clone the repository**:
```bash
git clone https://github.com/your-username/clickjacking-detection-tool.git
cd clickjacking-detection-tool
``` 
2. **Create a virtual environment (recommended)**:
```bash
python -m venv venv
```

3. **Activate the virtual environment**:

- On **macOS/Linux**:
```bash
source venv/bin/activate
```

- **On Windows**:
```bash
venv\Scripts\activate
```

4. **Install the required dependencies**:
```bash
pip install -r requirements.txt
```

## Usage
- To use the clickjacking detection tool:

1. **Run the script**:

```bash
python clickjacking.py
```

2. **The tool will ask you how you want to input the URLs**:

- **Single URL**: Choose "single" to manually enter one URL for testing.
- **Multiple URLs**: Choose "file" to provide a text file containing URLs (e.g., `urls.txt`). Place the file in the same directory as the script.

3. **Input Examples**:

- **For multiple URLs**:
```bash
Would you like to test multiple URLs from a file or a single URL? (file/single): file
Enter the filename (e.g., urls.txt) in the current directory: urls.txt
```

- **For a single URL**:
```bash
Would you like to test multiple URLs from a file or a single URL? (file/single): single
Enter the website URL to test for clickjacking: example.com
```


## Example Output
- **If a clickjacking vulnerability is detected**:

```bash
[+] Potential clickjacking detected: The page rendered within the iframe.
```
(This message will be displayed in green.)

- **If the site is protected against clickjacking**:

```bash
[-] No clickjacking detected ! ! !
```
(This message will be displayed in red.)


## How It Works

- **Check Headers**: The tool uses the requests library to perform a GET request and check if the site has anti-clickjacking headers (X-Frame-Options or Content-Security-Policy).
- **Iframe Test**: If no headers are found, the tool opens the URL in an iframe using Selenium.
- **Detection Logic**: If content loads within the iframe, a clickjacking vulnerability is considered detected. If the iframe fails to load content or an error message is shown, the site is considered protected.

## Requirements
- **Python 3.x**

- **Dependencies**:
 - selenium
 - requests
 - colorama
 - webdriver-manager

To install the dependencies, use:

```bash
pip install -r requirements.txt
```
## Creating `requirements.txt`
- To generate the `requirements.txt` file for this project:

```bash
pip freeze > requirements.txt
```

## License
- This project is licensed under the MIT License.

## Contributing
- Feel free to fork the repository and submit pull requests. Contributions are always welcome!

## Contact
- If you have any questions or need help, feel free to open an issue or contact us.