from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.llm.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

def create_filename_string(topic: str = "AI") -> str:
    """Create a filename string for the given topic.
    
    Args:
        topic (str): The topic of the file.
    
    Returns:
        str: The filename string.
    """
    return f"./articles/{topic.replace(' ', '_').lower()}.md"

def main():

    # get userr input for the topic
    topic = input("Enter the topic for the article: ")
    topic_filename = create_filename_string(topic)

    llm = OpenAIChat(model = "gpt-4o")

    assistant = Assistant(
        llm = llm,
        tools = [DuckDuckGo()],
        markdown = True,
        save_output_to_file = topic_filename
    )

    assistant.print_response(f"Write an article in the style of a New York Times reporter about the topic: {topic}.")

if __name__ == "__main__":
    main()