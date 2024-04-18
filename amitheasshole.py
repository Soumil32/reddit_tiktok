from time import sleep
import utils
import playwright.sync_api


def get_aita_post(browser: playwright.sync_api.Browser):
    page = browser.new_page()
    page.goto("https://www.reddit.com/r/AITAFiltered/new")
    page.wait_for_load_state()
    sleep(1)
    top_post = utils.get_list_of_posts(page)[0]
    top_post = top_post.query_selector("shreddit-post")
    post_link = top_post.get_attribute("content-href")
    print(post_link)
    page.close()
    page = browser.new_page()
    page.goto(f"https://reddit.com{post_link}")
    page.wait_for_load_state()
    page.wait_for_function("() => document.fonts.ready")
    sleep(1)
    post = page.query_selector("#t3_1c6c9bf")
    post_title = post.query_selector("h1")
    print(post_title.text_content())
    post_title.screenshot(path="aita.png")
