# main.py
def greeting(name):
    return f"Hello, {name}! Welcome to Jenkins CI/CD."

if __name__ == "__main__":
    message = greeting("My Friend")
    print(message)
    print("Execution Successful!")