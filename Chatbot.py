#Chatbot By Kirklen Allen

import random
import json
import os

# File to store the chatbot's memory
MEMORY_FILE = "chatbot_memory.json"

def load_memory():
    # Load memory from the memory file.
    # If the file doesn't exist, return an empty dictionary.
    try:
        if os.path.exists(MEMORY_FILE):  # # Check if memory file exists
            with open(MEMORY_FILE, "r") as file:  # # Open the file in read mode
                return json.load(file)  # # Parse JSON data
        return {}  # # Return empty memory if file is missing
    except json.JSONDecodeError:
        print("Warning: Memory file is corrupted. Starting with empty memory.")
        return {}  # # Return empty memory on JSON errors

def save_memory(memory):
    # Save the chatbot's memory to a JSON file.
    try:
        with open(MEMORY_FILE, "w") as file:  # # Open file in write mode
            json.dump(memory, file, indent=4)  # # Write memory in JSON format
    except IOError:
        print("Error: Unable to save memory. Changes will not persist.")  # # Warn if saving fails

def get_response(memory, user_input):
    # Get a response from memory.
    # If input is unknown, ask the user and store their response.
    if user_input in memory:  # # Check if user input exists in memory
        return random.choice(memory[user_input])  # # Return a random response from stored options
    else:
        print("Chatbot: I don’t know how to respond to that. What should I say?")
        user_response = input("You: ").strip()  # # Get user's response
        if user_response:  # # Check if response is not empty
            memory[user_input] = memory.get(user_input, []) + [user_response]  # # Add response to memory
            print("Chatbot: Got it! I'll remember that for next time.")
        else:
            print("Chatbot: Response not provided. Moving on...")  # # Handle empty response
        return None  # # Return nothing if no response is given

def chatbot():
    # Main chatbot function to handle the conversation loop.
    print("Welcome to the Learning Chatbot!")
    print("Type 'bye' to exit the conversation.")
    print("Tip: I’ll learn from what you tell me and use it in future conversations.")

    memory = load_memory()  # # Load existing memory from file

    while True:
        try:
            user_input = input("You: ").strip().lower()  # # Get user input
            if user_input == "bye":  # # Exit condition
                print("Chatbot: Goodbye! I'll remember our chat for next time.")
                save_memory(memory)  # # Save memory before exiting
                break

            response = get_response(memory, user_input)  # # Retrieve or learn a response
            if response:
                print(f"Chatbot: {response}")  # # Display chatbot's response
        except KeyboardInterrupt:
            print("\nChatbot: Exiting... Goodbye!")  # # Graceful exit on Ctrl+C
            save_memory(memory)  # # Save memory before exiting
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  # # Handle unexpected errors

if __name__ == "__main__":
    chatbot()  # # Start the chatbot
