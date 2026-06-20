from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dropdown")
        page.select_option("select#dropdown", "1") # Pilih Option 1 by value
        page.select_option("select#dropdown", label="Option 2") # Pilih by label
        print("Dropdown berhasil dimanipulasi.")
        browser.close()

if __name__ == "__main__": run()