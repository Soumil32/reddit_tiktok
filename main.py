from playwright.sync_api import sync_playwright, ViewportSize
from time import sleep

dsf = (500 // 600) + 1

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        locale="en-us",
        color_scheme="dark",
        viewport=ViewportSize(width=500, height=250),
        device_scale_factor=dsf,
    )

    # context.add_cookies(cookies)  # load preference cookies
    page = browser.new_page()
    page.goto("https://www.reddit.com/r/AITAFiltered/new")
    page.wait_for_load_state()
    sleep(2)
    page.screenshot(path="image.png")
    # Select the element
    element = page.query_selector("#main-content > div:nth-child(3)")
    # loop over the article elements in element
    for article in element.query_selector_all("article"):
        # get the article title
        title = article.query_selector("shreddit-post:nth-child(3)")
        # get the article link
        link = article.query_selector("a").get_attribute("href")
        print(f"Title: {title}\nLink: {link}\n")

    browser.close()
