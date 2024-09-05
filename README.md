# Reddit-Omni: Reddit's AI-Powered Question Vigilante

Reddit-Omni is an AI-powered bot that scrapes Reddit for questions, conducts research using online sources, and automatically generates and posts relevant answers to help users.

## Index
1. [Overview](#overview)
2. [Features](#features)
3. [Files](#files)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Toolbox](#toolbox)
8. [Models](#models)
9. [Learnings](#learnings)
10. [License](#license)
11. [Contact](#contact)

---

## Overview
Reddit-Omni is an AI-powered bot designed to enhance user interaction on Reddit by automatically scraping subreddits for questions, researching those topics using external online sources (like Google), and posting detailed, relevant answers. This bot helps users get timely, researched responses, making it a useful tool for increasing engagement and providing high-quality information across various Reddit communities. It leverages web scraping, natural language processing, and automation to perform these tasks with minimal human intervention.

## Features
- No cost API usage.
- Leverage of Meta's Llama 3.1 70B model.
- Automatization of reddit commenting.

## Files

### `requirements.txt`
This file lists all the Python packages required to run the project. It ensures that all necessary dependencies are installed for the project to function correctly.

### `app.py`
This is the main file of the project and is the one that needs to be run in order to use reddit-omni.

### `__init__.py`
This files exist in every folder in order to use imports from other folders.

### `config`
This folder contains the .env file with all API keys.

### `models`
This folder contains one file per available model.

### `prompts`
This folder contains prompting files, one for formatting and another one with an initial system prompt.

### `tools`
This folder contains one file per available tool and another one for the toolbox that agglutinates all tools and its docs.

## Installation
To install the reddit-omni, follow these steps:
   ```bash
   git clone https://github.com/diegovelilla/reddit-omni
   cd reddit-omni
   pip install -r requirements.txt
   ```

## Configuration:
Set up your API keys in the **.env** file inside the config model:

    GROQ_API_KEY="your_api_key_here"
    SERPER_API_KEY="your_api_key_here"
    CLIENT_ID="your_api_key_here"
    CLIENT_SECRET="your_api_key_here"
    USERNAME="your_reddit_username"
    PASSWORD="your_reddit_password_here"

## Usage:
To use reddit-omni just run the following command:
```bash
python3 -m app
```

## Toolbox:
Here are all the tools supported:
- reddit_scrapper: Scrapes a given subreddit for a number of posts.
- reddit_commenter: Comments given Reddit post.
- search_tool: Searches a given query on Google.
- scrape_tool: Scrapes a given webpage.

## Models
The models used for this project are:

- [Llama 3.1 70B](https://console.groq.com/docs/models) - Groq.

## License
This project is licensed under the **Apache 2.0 License**. See the [LICENSE](https://github.com/diegovelilla/FreeThinker/blob/main/LICENSE) file for more details.

## Contact
For any questions or feedback please reach out to:

- **Email**: [diegovelillarecio@gmail.com](mailto:diegovelillarecio@gmail.com)
- **GitHub Profile**: [diegovelilla](https://github.com/diegovelilla)
- **Hugging Face Profile**: [diegovelilla](https://huggingface.co/diegovelilla)
- **LinkedIn**: [Diego Velilla Recio](https://www.linkedin.com/in/diego-velilla-recio/)

Feel free to open an issue on GitHub or contact me in any way if you have any queries or suggestions.




