# index.py

def greet_user(name):
    return f"Hello, {name}! Welcome to my project."

if __name__ == "__main__":
    # Example usage
    user_name = input("Enter your name: ")
    message = greet_user(user_name)
    print(message)
