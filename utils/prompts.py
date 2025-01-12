from utils.models import SearchResult, ChatHistory
from utils.textual import format_search_results, format_chat_history

def system_prompt():
    return "You are a helpful assistant."

def user_prompt(user_query: str, search_result: SearchResult, history: ChatHistory):
    return f"""
You are an intelligent and helpful AI assistant. You have access to external documents retrieved based on user queries. Use the provided context to answer the user's questions accurately. If the context does not contain sufficient information, state that explicitly and avoid making assumptions. Always be concise, polite, and precise.

History:
{format_chat_history(history)}

Context:
{format_search_results(search_result)}

User Query:
{user_query}

Response:

"""
