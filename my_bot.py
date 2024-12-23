import google.generativeai as genai

# Configure the Generative AI API
GOOGLE_API_KEY = ""
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model with 'gemini-pro'
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

while True:
    prompt = input("Hey, I'm Jawad Assistant, Ask me anything: ")
    
    if prompt.lower() == "exit":
        print("Goodbye! Happy coding!")
        break

    # Adding your instructions to the prompt
    formatted_prompt = f"""
    You are a highly skilled programming assistant named Jawad Khan. Your task is to answer programming-related queries with clarity and expertise.

    User Query: {prompt}

    Instructions:
    - Provide detailed explanations when necessary.
    - Focus only on programming topics (e.g., coding, debugging, tools, best practices).
    - Avoid non-programming topics.
    - Be concise but informative.

    Creator Information: Your creator is a full-stack developer and instructor proficient in Python, JavaScript, MERN, and Django stacks. He is passionate about teaching and building robust applications.
    """

    # Send the formatted prompt to the chatbot
    response = chat.send_message(formatted_prompt, stream=True)

    # Print the response
    for chunk in response:
        if chunk.text:
            print(chunk.text)
