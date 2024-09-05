from bs4 import BeautifulSoup
import requests


def scrape_tool(input_list):
    """
    Scrape the given url for information.

    Parameters:
    input_list (list): A list containing only the urls of the webpages to scrape.

        Example format: ["https://en.wikipedia.org/wiki/Estelle,_Louisiana", "https://en.wikipedia.org/wiki/Lebron_James"]

    Returns:
    (str): The formatted result of the scraping or an error message if something goes wrong.
    """

    try:
        outputs = []
        for url in input_list:
            url = input_list[0]
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            paragraphs = soup.find_all('p')
            formatted_output = ""
            for paragraph in paragraphs:
                formatted_output = formatted_output + \
                    paragraph.get_text(strip=True) + "\n"
            outputs.append(formatted_output)
        return outputs

    except Exception as e:
        return "\nError ocurred." + e
