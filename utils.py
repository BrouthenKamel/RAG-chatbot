import re
from models import SearchResult, ChatHistory

def clean_text(text: str, keep_newline: bool = False) -> str:
    if keep_newline:
        pattern = r'[^a-zA-Z0-9.,!?;:\'\"()\[\]\-_\s]'
        space_pattern = r'[^\S\n]+'
    else:
        pattern = r'[^a-zA-Z0-9.,!?;:\'\"()\[\]\-_\s\n]'
        space_pattern = r'\s+'
    cleaned_text = re.sub(pattern, '', text)
    cleaned_text = re.sub(space_pattern, ' ', cleaned_text).strip()
    return cleaned_text

def format_search_results(search_results: SearchResult) -> str:
    formatted_results = ""
    for i, (distance, document) in enumerate(zip(search_results.distances, search_results.documents), 1):
        repeat = 20
        formatted_results += "="*repeat
        formatted_results += f"Retrieval Stats: Rank {i}, Distance {distance}"
        formatted_results += f"Retrieval Content: {document}"
        formatted_results += "\n"
    return formatted_results

def format_chat_history(chat_history: ChatHistory) -> str:
    formatted_history = ""
    for i, interaction in enumerate(chat_history.interactions, 1):
        formatted_history += f"Interaction {i}:\n"
        formatted_history += f"User: {interaction.user}\n"
        formatted_history += f"You: {interaction.chatbot}\n"
        formatted_history += "\n"
    return formatted_history

def summarize(text: str, size: int = 5) -> str:
    words = text.split()
    return " ".join(words[:size]) + "..." if len(words) > size else text
