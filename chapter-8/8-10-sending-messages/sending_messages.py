# 8.10 Sending Messages

messages = ["Hello", "How are you?", "Goodbye"]
sent_messages = []


def send_messages(messages, sent_messages):
    """Simulate sending each message, until none are left.
    Move each message to sent_messages after sending."""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


send_messages(messages, sent_messages)
print(f"\nOriginal list: {messages}")
print(f"Sent messages: {sent_messages}")