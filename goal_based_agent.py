"""Simple, self-contained job-application CLI.

This standalone script fixes the execution issues in the original by removing
LangChain dependencies and a few bugs in the parsing logic.
"""

import re
from dotenv import load_dotenv


load_dotenv()

application_info = {
    "name": None,
    "email": None,
    "skills": None,
}


def extract_application_info(text: str) -> str:
    """Extract name, email, and skills from a single text input.

    Mutates the global `application_info` dict and returns a short summary
    of what was extracted (or a prompt asking for relevant info).
    """

    name_match = re.search(r"(?:my name is|I am|This is)\s+([A-Z][a-zA-Z]+)", text, re.IGNORECASE)
    email_match = re.search(r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", text)
    skills_match = re.search(r"(?:I have experience in|My skills include|I am skilled at|My Skills are)\s+([a-zA-Z0-9 ,]+)", text, re.IGNORECASE)

    parts = []

    if name_match:
        application_info["name"] = name_match.group(1).title()
        parts.append(f"Extracted Name: {application_info['name']}")

    if email_match:
        application_info["email"] = email_match.group(1)
        parts.append(f"Extracted Email: {application_info['email']}")

    if skills_match:
        application_info["skills"] = skills_match.group(1).strip()
        parts.append(f"Extracted Skills: {application_info['skills']}")

    if not parts:
        return "No relevant information found in that message. Please provide your name, email, or skills."

    return " ".join(parts)


def check_application_info() -> str:
    if all(application_info.values()):
        return (
            "You are Ready! All required information received: "
            f"Name: {application_info['name']}, Email: {application_info['email']}, Skills: {application_info['skills']}"
        )
    missing = [k for k, v in application_info.items() if not v]
    return f"Missing information: {', '.join(missing)}. Please provide the missing details."


def main():
    print("Welcome to the Job Application Assistant. Please provide your application details.")
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ("exit", "quit"):
            print("Exiting the application assistant. Goodbye!")
            break

        extract_summary = extract_application_info(user_input)
        print(f"Assistant: {extract_summary}")

        check = check_application_info()
        print(f"Assistant: {check}")

        if "you are ready" in check.lower():
            print("Application process complete. Thank you!")
            break


if __name__ == "__main__":
    main()
