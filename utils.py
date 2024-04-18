import playwright.sync_api


def get_list_of_posts(page: playwright.sync_api.Page) -> list[playwright.sync_api.ElementHandle]:
    # Select the element
    posts_element = page.query_selector("#main-content > div:nth-child(3)")
    return posts_element.query_selector_all("article")


def remove_google_sign_in(page: playwright.sync_api.Page):
    google_sign_in = page.query_selector("#credential_picker_container")
    if google_sign_in:
        google_sign_in.evaluate("element => element.remove()")


def tts(text: str, description:str, output_filename: str):
    pass
