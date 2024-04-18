from time import sleep
import utils
import playwright.sync_api


def get_aita_post(browser: playwright.sync_api.Browser):
    page = browser.new_page()
    page.goto("https://www.reddit.com/r/AITAFiltered/new")
    page.wait_for_load_state()
    sleep(2)
    page.screenshot(path="image.png")
    posts = utils.get_list_of_posts(page)
    print(posts)
