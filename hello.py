# hello.py
# Machine Problem 2 - Introduction to Git and GitHub
# Author: Emmarlon Ogoc

def main():
    print("Hello, World!")
    name = input("What's your name? ").strip()
    if name:
        print(f"Nice to meet you, {name}! Thanks for checking out GitHub-Intro.")
    else:
        print("Nice to meet you, mystery coder!")

if __name__ == "__main__":
    main()