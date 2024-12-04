from browser_use import Browser, BrowserConfig
from selenium_driverless import webdriver
import asyncio

async def main():
    # Configure browser-use to connect to selenium-driverless instance
    browser = Browser(
        config=BrowserConfig(
            wss_url='ws://localhost:3000'  # Replace with your API URL
        )
    )

    # Start browser and create new tabs
    async with browser:
        # Open first tab
        tab1 = await browser.new_tab()
        await tab1.goto('https://example.com')

        # Open second tab
        tab2 = await browser.new_tab()
        await tab2.goto('https://google.com')

        # Switch between tabs and perform operations
        await tab1.bring_to_front()
        print(f'Tab 1 title: {await tab1.title()}')

        await tab2.bring_to_front()
        print(f'Tab 2 title: {await tab2.title()}')

        # Close tabs
        await tab1.close()
        await tab2.close()

if __name__ == '__main__':
    asyncio.run(main())