import os
import fitz  # PyMuPDF for reading PDF
from langchain import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain.llms import OpenAI
from openai import OpenAIError
from dotenv import load_dotenv
import os

from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
# from langchain.schema import RunnableSequence 
from helpers.openai_client import OpenAIClient


class CitationService:
    def __init__(self):
        # Load environment variables (like OPENAI_API_KEY)
        load_dotenv()
        
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OpenAI API key is not set. Please set it in the .env file.")

        # Initialize the OpenAI model
        self.llm = OpenAIClient.initialize_llm()

        self.chain = self._initialize_chain()

    def _initialize_chain(self):
        # Create a prompt template for checking citation according to Bluebook
        prompt_template = """
        You are an expert in legal citation standards, particularly the Bluebook. 
        You will be given a text from a research paper and your task is to analyze the citations.
        - Identify any citation that does not follow Bluebook standards.
        - Suggest improvements for incorrect citations.
        - If the citation is correct, mention that it follows the standard.
        * Note : Please use icon / emojis for correct and incorrect citation, 

        Text: {document_text}

        Please provide detailed feedback for each issue.
        """

        prompt = PromptTemplate(template=prompt_template, input_variables=["document_text"])
        return LLMChain(prompt=prompt, llm=self.llm)

    def check_citation(self, document_text):
        # try:
            # Call the LangChain chain to check the citation
        result = self.chain.invoke({"document_text": document_text})

        return result["text"]
        # except OpenAIError as e:
        #     return {"error": f"OpenAI API error: {str(e)}"}
        # except Exception as e:
        #     return {"error": f"An unexpected error occurred: {str(e)}"}

    def extract_text_from_pdf(self, file_path):
        try:
            with fitz.open(file_path) as pdf:
                text = ""
                for page_num in range(pdf.page_count):
                    text += pdf[page_num].get_text()
                return text
        except Exception as e:
            raise Exception(f"Failed to extract text from PDF: {str(e)}")


