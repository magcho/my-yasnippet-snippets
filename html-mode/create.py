from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pprint import pprint

MDN_ELEMENT_URL = "https://developer.mozilla.org/ja/docs/Web/HTML/Element"
MDN_ATTR_URL = "https://developer.mozilla.org/ja/docs/Web/HTML/Attributes"


def main():
    options = Options()

    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(MDN_ELEMENT_URL)

    elements = [ele.text for ele in driver.find_elements_by_tag_name("code")]
    elements = list(set(elements))
    elements = [
        ele[1:-1]
        for ele in elements
        if ele[0:1] == "<"
        and not ele[1:2] == "/"
        and ele[-1:] == ">"
        and not ele == "<h1>-<h6>"
    ]
    pprint(elements)


main()
