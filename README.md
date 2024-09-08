# Reddit-Omni: Reddit's AI-Powered Question Vigilante

Reddit-Omni is an AI-powered bot that scrapes Reddit for questions, conducts research using online sources, and automatically generates and posts relevant answers to help users.

## Index
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Models](#models)
7. [License](#license)
8. [Contact](#contact)

---

## Overview
Reddit-Omni is an AI-powered bot designed to enhance user interaction on Reddit by automatically scraping subreddits for questions, researching those topics using external online sources (like Google), and posting detailed, relevant answers. This bot helps users get timely, researched responses, making it a useful tool for increasing engagement and providing high-quality information across various Reddit communities. It leverages web scraping, natural language processing, and automation to perform these tasks with minimal human intervention.

## Features
- No cost API usage.
- Leverage of Meta's Llama 3.1 70B model.
- Automatization of reddit commenting.

## Workflow
There are 4 tool usages in this project:
- reddit_scrapper: Scrapes a given subreddit for a number of posts.
- search_tool: Searches a given query on Google.
- scrape_tool: Scrapes a given webpage.
- reddit_commenter: Comments given Reddit post.

  
Also, the AI model adquires 3 diferent personas in this project:
- Planner: Recieves the reddit scraped question and generates queries for the search_tool.
- Researcher: Receives the titles, summaries and URLs from the search_tool and decides which is more likely to contain useful information about the question.
- Writer: Recieves the scrapped webpages dump and generates a concise and correct answer to the initial question.

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




