import prompts
import streamlit as st
from azure_openai import initialize_azure_openai
from app_setup import set_openai_env_vars, initialize_embeddings, initialize_prompt_template

def main():
    """
    Main function to run the application.
    """
    try:
    # Set environment variables
        set_openai_env_vars()

        # Initialize Azure OpenAI
        llm = initialize_azure_openai()

        # Initialize OpenAI embeddings
        embeddings = initialize_embeddings()

        # Initialize prompt template
        qa_prompt = initialize_prompt_template()
    except Exception as e:
        st.error(f"An error occurred: {e}. Features requiring API keys are currently unavailable.")
        st.info("Allowing user input for API keys or a 'demo mode' will be available soon.")

if __name__ == "__main__":
    main()
