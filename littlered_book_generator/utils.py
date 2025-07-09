from langchain.chains.question_answering.map_rerank_prompt import output_parser
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from prompt_template import system_template_text,user_template_text
from little_red_book_model import little_red_book

def generate_little_red_book(theme,api_key):
    prompt=ChatPromptTemplate.from_messages(
    [('system',system_template_text),('user',user_template_text)]
    )

    model = ChatOpenAI(
        api_key=api_key,  # Replace with your DeepSeek API key
        base_url="https://api.deepseek.com/v1",  # DeepSeek endpoint
        model="deepseek-chat",  # or "deepseek-coder"

    )

    output_parser=PydanticOutputParser(pydantic_object=little_red_book)

    chain=prompt|model|output_parser
    result=chain.invoke(
        {'parser_instructions':output_parser.get_format_instructions(),
            'theme':theme
         }
    )

    return result

#print(generate_little_red_book("守望先锋", 'sk-d5ecfe9df3e34c1e9d2452b6e2841850'))