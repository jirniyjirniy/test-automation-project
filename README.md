# Test Automation Project

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/test-automation-project.git
   ```

2. Navigate to the project directory:
   ```bash
   cd test-automation-project
   ```

3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

To run the tests, use the following command:

```bash
  pytest
  
```  

Or for specific tests:

```bash
  pytest test/test_name.py
```

## Supported Environments

### Browsers
- **Chrome** (latest stable version)
- **Firefox** (latest stable version)
- **Safari** (macOS only)

### Mobile Devices
- **iOS** (latest stable version)
- **Android** (latest stable version)

## Requirements

### Prerequisites
- [ChromeDriver](https://chromedriver.chromium.org/) (for Chrome)
- [GeckoDriver](https://github.com/mozilla/geckodriver) (for Firefox)
- Python 3.8+
- Installed dependencies:
  ```bash
  pip install -r requirements.txt