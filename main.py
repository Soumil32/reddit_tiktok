from playwright.sync_api import sync_playwright, ViewportSize
from time import sleep
import amitheasshole

dsf = (500 // 600) + 1

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    context = browser.new_context(
        locale="en-us",
        color_scheme="dark",
        viewport=ViewportSize(width=500, height=250),
        device_scale_factor=dsf,
    )

    amitheasshole.get_aita_post(browser)


    browser.close()
