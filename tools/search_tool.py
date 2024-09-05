import requests
from dotenv import dotenv_values


def search_tool(input_list):
    """
    Search the given query on google.

    Parameters:
    input_list (list): A list containing the queries to search on google.

        Example format: ["longest river in the world", "who is the current president of the USA"]

    Returns:
    (str): The formatted result of the search or an error message if something goes wrong.
    """
    try:
        searches = []
        for query in input_list:
            CONFIG = dotenv_values("./config/.env")
            API_KEY = CONFIG["SERPER_API_KEY"]
            params = {
                'q': query,
                'api_key': API_KEY
            }
            response = requests.get(
                "https://google.serper.dev/search", params=params)
            data = response.json()
            formatted_output = ""
            for result in data["organic"]:
                formatted_output = formatted_output + \
                    f"""Title: "{result["title"]}" Abstract: {result["snippet"]} URL: {result["link"]}"""
            searches.append(formatted_output)
        return searches

    except Exception as e:
        return "\nError ocurred." + e
