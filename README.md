# Browser-Use Multi-Tab Example with Selenium-Driverless

This example demonstrates how to use browser-use's multi-tab functionality with selenium-driverless as the browser backend, connecting via WSS URL.

## Requirements

- Python 3.8+
- Google Chrome installed
- selenium-driverless 0.1.16
- browser-use

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Update the `wss_url` in the script to point to your selenium-driverless instance
2. Run the example:
```bash
python multi_tab_example.py
```

## Notes

- This example uses browser-use's tab management capabilities
- Connects to a selenium-driverless instance via WSS URL
- Demonstrates basic multi-tab operations
