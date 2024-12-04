# Selenium Driverless Multi-Tab Example

This repository demonstrates how to use selenium-driverless for handling multiple tabs while connecting to a custom browser instance (such as browserless or anty).

## Features

- Custom browser instance connection using WSS URL
- Multi-tab handling
- Asynchronous operation
- Cloudflare bypass capability

## Installation

1. Install the requirements:
```bash
pip install -r requirements.txt
```

2. Make sure you have Google Chrome installed

## Usage

1. Update the `wss_url` in `multi_tab_example.py` to point to your browser instance
2. Run the example:
```bash
python multi_tab_example.py
```

## Configuration

The example demonstrates:
- Connecting to a custom browser instance
- Creating and managing multiple tabs
- Concurrent tab operations
- Proper resource cleanup

## Notes

- This example uses selenium-driverless 0.1.16
- Requires Python 3.8 or higher
- Compatible with browserless, anty, and similar services