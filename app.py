from models.llama_3_1_70B import llama_3_1_70B
from tools.reddit_scrapper import reddit_scrapper
from tools.search_tool import search_tool
from tools.scrape_tool import scrape_tool
from tools.reddit_commenter import reddit_commenter
import json


def prepare_system_prompts():
    with open("prompts/planner.md", "r") as file:
        system_prompt_planner = file.read()
    with open("prompts/researcher.md", "r") as file:
        system_prompt_researcher = file.read()
    with open("prompts/writer.md", "r") as file:
        system_prompt_writer = file.read()
    return system_prompt_planner, system_prompt_researcher, system_prompt_writer


def chain_of_action(model, system_prompt_planner, system_prompt_researcher, system_prompt_writer):
    # Scrape reddit posts for questions

    reddit_scrape, post_ids = reddit_scrapper(["askbaking", "1"])
    print(f"Somebody in reddit has this question:\n{reddit_scrape}")

    # Give question to planner in order to plan the search queries
    plan_prompt = f"""
    {{
    "question": "{reddit_scrape}"
    }}    
    """

    plan = model.answer(
        system_prompt=system_prompt_planner, prompt=plan_prompt)
    plan = json.loads(plan)
    print("\nFor this question I decided to search:")
    print(plan["query1"])
    print(plan["query2"])
    print(plan["query3"])

    # Use the search tool
    search_results = search_tool(
        [plan["query1"], plan["query2"], plan["query3"]])
    print("\nI've found this:")
    print(search_results)

    # Use the researcher to choose the most crucial info
    research_prompt = f"""
    {{
    "question": "{reddit_scrape}",
    "query1": "{plan["query1"]}",
    "query2": "{plan["query2"]}",
    "query3": "{plan["query3"]}",
    "search": "{search_results}"
    }}    
    """
    research = model.answer(
        system_prompt=system_prompt_researcher, prompt=research_prompt)
    print(research)

    # Use the web scrapper
    research = json.loads(research)
    scrape_results = scrape_tool(
        [research["url1"], research["url2"], research["url3"]])
    print(scrape_results)

    # Use the writer
    writer_prompt = f"""
    {{
    "question": "{reddit_scrape}",
    "dump": "{scrape_results}"
    }}    
    """
    writer = model.answer(
        system_prompt=system_prompt_writer, prompt=writer_prompt)
    writer = json.loads(writer)
    print(f"""\n\n{writer["answer"]}""")

    # Use the reddit_poster tool
    reddit_commenter([post_ids[0], writer["answer"]])


if __name__ == "__main__":

    model = llama_3_1_70B()

    system_prompt_planner, system_prompt_researcher, system_prompt_writer = prepare_system_prompts()

    chain_of_action(model, system_prompt_planner=system_prompt_planner,
                    system_prompt_researcher=system_prompt_researcher, system_prompt_writer=system_prompt_writer)
