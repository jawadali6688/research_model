# import google.generativeai as genai
# import os

# # Configure the Generative AI API
# GOOGLE_API_KEY = "AIzaSyDqPU2L0i05_FgjI31N8yAVc_G6vxHhVIc"# Store API key securely as an environment variable
# genai.configure(api_key=GOOGLE_API_KEY)

# # Initialize the model (verify model name from the documentation)
# model_name = "text-bison"  # Updated to a simpler name format

# def chatbot():
#     print("\n--- Welcome to Programmer Bot: Jawad Khan ---")
#     print("I am Jawad Khan, a virtual programmer here to assist you with coding, debugging, and any programming-related queries.")
#     print("I can only answer programming-related questions. If you have any research or other non-programming questions, I won't be able to assist.")
#     print("My creator is a full-stack web-based software developer and instructor with expertise in Python, JavaScript, MERN, and Django stacks.")
#     print("He also teaches web development and consults on building scalable applications. Type 'exit' to end the chat.\n")

#     while True:
#         # Get user input
#         user_input = input("You: ")

#         # Check for exit condition
#         if user_input.lower() == 'exit':
#             print("\nJawad Khan: Goodbye! Happy coding!\n")
#             break

#         # Generate a response using the model
#         prompt = f"""
#         You are a highly skilled programming assistant named Jawad Khan. Your task is to answer programming-related queries with clarity and expertise.

#         User Query: {user_input}

#         Instructions:
#         - Provide detailed explanations when necessary.
#         - Focus only on programming topics (e.g., coding, debugging, tools, best practices).
#         - Avoid non-programming topics.
#         - Be concise but informative.

#         Creator Information: Your creator is a full-stack developer and instructor proficient in Python, JavaScript, MERN, and Django stacks. He is passionate about teaching and building robust applications.
#         """

#         try:
#             # Generate a response using the model
#             response = genai.(model_name=model_name, prompt=prompt)  # Correct method for generating content
#             print(f"Jawad Khan: {response.text.strip()}\n")  # Ensure the response text is printed clearly
#         except Exception as e:
#             print(f"Jawad Khan: Sorry, I encountered an error. ({e})\n")

# if __name__ == "__main__":
#     chatbot()



import google.generativeai as genai

GOOGLE_API_KEY = ""
genai.configure(api_key=GOOGLE_API_KEY)



model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

while True:
    prompt = input("Ask me anything: ")
    if (prompt == "exit"):
        break
    response = chat.send_message(prompt, stream=True)
    for chunk in response:
        if chunk.text:
          print(chunk.text)