from dotenv import load_dotenv
load_dotenv()

from phi.assistant.openai import OpenAIAssistant
from phi.assistant.openai.file.url import UrlFile
from phi.assistant.openai.file.local import LocalFile
from phi.assistant.openai.tool import Retrieval

# Load the recipe book from s3
recipe_book_s3 = UrlFile(url="https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf").get_or_create()
# Load the recipe book locally
# recipe_book_local = LocalFile(path="data/pdfs/meals-more-recipes.pdf").get_or_create()

# Create an Assistant
with OpenAIAssistant(
    name="RecipeAssistant",
    tools=[Retrieval],
    files=[recipe_book_s3],
    instructions="Format your answers using Markdown.",
) as recipe_assistant:
    # Run the Assistant
    recipe_assistant.print_response("How do I make pad thai?", markdown=True)
