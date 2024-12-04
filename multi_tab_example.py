from selenium_driverless import webdriver
from selenium_driverless.types.by import By
import asyncio

async def setup_browser(wss_url):
    # Configure browser with custom WSS URL
    browser_config = webdriver.BrowserConfig(
        wss_url=wss_url
    )
    options = webdriver.ChromeOptions()
    return await webdriver.Chrome(options=options, config=browser_config)

async def handle_tab(driver, url):
    await driver.get(url, wait_load=True)
    await driver.wait_for_cdp('Page.domContentEventFired', timeout=15)
    return await driver.title

async def main():
    # Replace with your browserless/anty instance URL
    wss_url = 'ws://localhost:3000'
    
    async with await setup_browser(wss_url) as driver:
        # Create multiple tabs
        tab1 = driver.current_window_handle
        await driver.new_window('tab')
        tab2 = driver.current_window_handle
        await driver.new_window('tab')
        tab3 = driver.current_window_handle

        # List of URLs to visit
        urls = [
            'https://example.com',
            'https://google.com',
            'https://github.com'
        ]

        # Handle each tab concurrently
        tasks = []
        for tab, url in zip([tab1, tab2, tab3], urls):
            await driver.switch_to.window(tab)
            tasks.append(handle_tab(driver, url))

        # Wait for all tabs to complete
        results = await asyncio.gather(*tasks)
        
        # Print results
        for i, title in enumerate(results, 1):
            print(f'Tab {i} title: {title}')

if __name__ == '__main__':
    asyncio.run(main())