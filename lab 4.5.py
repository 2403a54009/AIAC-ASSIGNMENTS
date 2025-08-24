# Lab 4.5: Advanced Prompt Engineering

# Sample email data
emails = [
    {
        "subject": "Meeting Reminder",
        "body": "Don't forget about the meeting at 10am tomorrow in Conference Room A."
    },
    {
        "subject": "Project Update",
        "body": "The project is on track for completion by the end of the month. Let me know if you need any help."
    },
    {
        "subject": "Lunch Invitation",
        "body": "Would you like to join me for lunch today at 12:30pm?"
    }
]

# Zero-shot prompt example
def zero_shot_prompt(email):
    prompt = f"Summarize the following email:\nSubject: {email['subject']}\nBody: {email['body']}\nSummary:"
    return prompt

# One-shot prompt example
def one_shot_prompt(email):
    example = (
        "Subject: Team Outing\n"
        "Body: We are planning a team outing next Friday. Please RSVP by Monday.\n"
        "Summary: Invitation to a team outing next Friday."
    )
    prompt = (
        f"Summarize the following email:\n"
        f"{example}\n"
        f"Subject: {email['subject']}\n"
        f"Body: {email['body']}\n"
        f"Summary:"
    )
    return prompt

# Few-shot prompt example
def few_shot_prompt(email):
    examples = (
        "Subject: Team Outing\n"
        "Body: We are planning a team outing next Friday. Please RSVP by Monday.\n"
        "Summary: Invitation to a team outing next Friday.\n\n"
        "Subject: Password Reset\n"
        "Body: Click the link below to reset your password.\n"
        "Summary: Instructions to reset your password."
    )
    prompt = (
        f"Summarize the following email:\n"
        f"{examples}\n\n"
        f"Subject: {email['subject']}\n"
        f"Body: {email['body']}\n"
        f"Summary:"
    )
    return prompt

# Evaluation format template
def evaluate_summary(email, summary):
    print("Email Subject:", email['subject'])
    print("Email Body:", email['body'])
    print("Generated Summary:", summary)
    print("Evaluation: [Your evaluation here]\n")

# Template for deliverable
def generate_deliverable():
    print("Lab 4: Advanced Prompt Engineering Deliverable\n")
    print("1. Sample Email Data:")
    for email in emails:
        print(email)
    print("\n2. Zero-shot Prompt Example:")
    print(zero_shot_prompt(emails[0]))
    print("\n3. One-shot Prompt Example:")
    print(one_shot_prompt(emails[1]))
    print("\n4. Few-shot Prompt Example:")
    print(few_shot_prompt(emails[2]))
    print("\n5. Evaluation Format Example:")
    evaluate_summary(emails[0], "Reminder about tomorrow's 10am meeting in Conference Room A.")

if __name__ == "__main__":
    generate_deliverable()