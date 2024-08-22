import os
from datetime import datetime

def create_meeting_summary(meeting_date, attendees, topics_discussed, action_items):
    summary = f"Meeting Summary - {meeting_date.strftime('%Y-%m-%d')}\n"
    summary += f"Attendees: {', '.join(attendees)}\n\n"
    summary += "Topics Discussed:\n"
    for topic in topics_discussed:
        summary += f"- {topic}\n"
    summary += "\nAction Items:\n"
    for item in action_items:
        summary += f"- {item}\n"
    return summary

def create_email_template(subject, body, to_email, from_email):
    email_template = f"From: {from_email}\n"
    email_template += f"To: {to_email}\n"
    email_template += f"Subject: {subject}\n\n"
    email_template += body
    return email_template

if __name__ == "__main__":
    # Prompt for customer name and meeting name
    customer_name = input("Enter customer name: ")
    meeting_name = input("Enter meeting name: ")

    # Prompt for meeting details
    attendees = input("Enter attendees (comma-separated): ").split(',')
    topics_discussed = input("Enter topics discussed (comma-separated): ").split(',')
    action_items = input("Enter action items (comma-separated): ").split(',')

    # Example meeting details
    meeting_date = datetime.now()
    meeting_details = f"Meeting Date: {meeting_date.strftime('%Y-%m-%d')}\n"
    meeting_details += f"Attendees: {', '.join(attendees)}\n"
    meeting_details += f"Topics Discussed: {', '.join(topics_discussed)}\n"
    meeting_details += f"Action Items: {', '.join(action_items)}\n"

    # Create the meeting summary
    summary = create_meeting_summary(meeting_date, attendees, topics_discussed, action_items)

    # Email details
    subject = f"Meeting Summary - {meeting_name}"
    to_email = "recipient@example.com"
    from_email = "your_email@example.com"

    # Create the email template
    email_template = create_email_template(subject, summary, to_email, from_email)

    # Create customer directory if it doesn't exist
    customer_dir = os.path.join("customers", customer_name)
    os.makedirs(customer_dir, exist_ok=True)

    # Create the file name using meeting name and date
    file_name = f"{meeting_name}_{meeting_date.strftime('%Y-%m-%d')}.txt"
    file_path = os.path.join(customer_dir, file_name)

    # Save the email template to the file
    with open(file_path, "w") as file:
        file.write(email_template)

    print(f"Email template created and saved to {file_path}")