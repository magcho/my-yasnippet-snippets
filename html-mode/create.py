from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pprint import pprint

MDN_ELEMENT_URL = "https://developer.mozilla.org/ja/docs/Web/HTML/Element"
MDN_ATTR_URL = "https://developer.mozilla.org/ja/docs/Web/HTML/Attributes"


def main():
    options = Options()

    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    elements = scrapeTagName(driver)
    attributes = scrapeAttrName(driver)

    for tagName in elements:
        createTagNameSnippet(tagName)

    for attr in attributes:
        createAttrSnippet(attr)


def scrapeTagName(driver):
    """scrapeing from MDN

    Args:
       driver  webdriver
    """
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
    return elements


def scrapeAttrName(driver):
    """scrapeing from MDN
    
    Args:
       driver  webdriver
    """
    driver.get(MDN_ATTR_URL)
    attributes = [ele.text for ele in driver.find_elements_by_tag_name("code")]
    attributes = list(set(attributes))
    attributes = [
        attr
        for attr in attributes
        if not attr[0:1] == "<"
        and not attr[-1:] == ">"
        and not attr == ""
        and not attr[-1:] == ")"
        and not attr[-1:] == '"'
        and not attr[-1:] == "*"
    ]
    return attributes


def createTagNameSnippet(tagName):
    """create snippet file

    Args:
       tagName  create snippet file of tagName
    """
    buff = """
# -*- mode: snippet -*-
# name: {0}
# key: {0}
# --
<{0}>$0</{0}>
    """[
        1:-1
    ].format(
        tagName
    )

    filename = "tag." + tagName
    createSnippetFile(buff, filename)


def createAttrSnippet(attr):
    """create snippet file
    
    Args:
       attr   create snippet file of attr
    """
    buff = """
# -*- mode: snippet -*-
# name: {0}
# key: {0}
# --
{0}=\"$0\"
"""[
        1:-1
    ].format(
        attr
    )

    fileName = "attr." + attr
    createSnippetFile(buff, fileName)


def createSnippetFile(buff, fileName):
    """create snippet file

    Args:
       buff fileBuff
       fileName create snippet fileName


    """
    with open(fileName, "w") as fp:
        fp.write(buff)


main()
