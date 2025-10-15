import google.generativeai as genai
import os

def analyze_code(code_content):
    """
    Analyzes the given code using the Gemini API.

    Args:
        code_content (str): The source code to be reviewed.

    Returns:
        str: The code review report from the LLM.
    """
    try:
        # Configure the API key
        # Make sure to set your GOOGLE_API_KEY in a .env file
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")
        
        genai.configure(api_key=api_key)

        # Create the model
        model = genai.GenerativeModel('gemini-pro-latest')

        # Define the prompt for the LLM
        prompt = f"""
        As an expert code reviewer, please analyze the following code snippet.
        Focus on these key areas:
        1.  **Readability**: Is the code clean, well-commented, and easy to understand?
        2.  **Modularity**: Is the code well-structured? Are functions and classes single-purpose?
        3.  **Best Practices**: Does it follow language-specific conventions and best practices?
        4.  **Potential Bugs**: Are there any logical errors, edge cases missed, or potential runtime issues?
        5.  **Performance**: Are there any obvious performance bottlenecks?

        Provide a structured review report with clear sections and actionable suggestions for improvement. Use markdown for formatting.

        --- CODE START ---
        {code_content}
        --- CODE END ---
        """

        # Generate the content
        response = model.generate_content(prompt)
        
        return response.text
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error: Could not generate code review. Please check the API key and server logs."