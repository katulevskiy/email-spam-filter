# naive_bayes_example.py

import email_spam_filter as esf

def load_data():
    # Sample data for demonstration purposes
    emails = [
        ("Hey there! Wanna grab a coffee tomorrow?", "ham"),
        ("Free lottery tickets now!!! Click here", "spam"),
        ("Could we schedule a meeting for next week?", "ham"),
        ("Congratulations, you've won a $1000 gift card!", "spam"),
        ("Reminder: Project deadline is Friday.", "ham"),
    ]
    
    # Separate emails into spam and ham lists
    spam_emails = [email[0] for email in emails if email[1] == "spam"]
    ham_emails = [email[0] for email in emails if email[1] == "ham"]
    
    return spam_emails, ham_emails

def train_filter():
    # Load training data
    spam_emails, ham_emails = load_data()
    
    # Train the Naive Bayes filter
    filter_instance = esf.NaiveBayesFilter()
    filter_instance.train(spam_emails, ham_emails)
    
    print("Training completed.")
    return filter_instance

def test_filter(filter_instance):
    # Test cases to demonstrate real-world applications
    test_cases = [
        ("Win a free vacation now!!!", "spam"),
        ("Please review the attached document for our next meeting.", "ham")
    ]
    
    for email, expected in test_cases:
        result = filter_instance.predict(email)
        print(f"Email: '{email}'\nPredicted: {result}, Expected: {expected}\n")

def integrate_with_email_client():
    # Example of integrating with an email client (e.g., using IMAP to fetch emails)
    import imaplib
    import email

    def connect_to_email_server(username, password, server='imap.gmail.com'):
        mail = imaplib.IMAP4_SSL(server)
        mail.login(username, password)
        return mail
    
    def fetch_emails(mail):
        mail.select('inbox')
        status, messages = mail.search(None, 'ALL')
        
        for num in messages[0].split():
            typ, data = mail.fetch(num, '(RFC822)')
            
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            
            subject = msg['subject']
            from_ = msg['from']
            
            # Process each email with the spam filter
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    ctype = part.get_content_type()
                    cdispo = str(part.get('Content-Disposition'))
                    
                    # Skip any text/plain (txt) attachments
                    if ctype == 'text/plain' and 'attachment' not in cdispo:
                        body = part.get_payload(decode=True).decode()  # decode
                        break
            else:  # it's not multipart - i.e. plain text, no attachments, keeping it simple
                body = msg.get_payload(decode=True).decode()
            
            filter_instance = train_filter()
            is_spam = filter_instance.predict(body)
            print(f"Subject: {subject}\nFrom: {from_}\nSpam: {is_spam}")

def main():
    # Train the spam filter
    filter_instance = train_filter()

    # Test the filter with example cases
    test_filter(filter_instance)

    # Example of integration - Uncomment and configure for your email client
    # mail = connect_to_email_server('your-email@gmail.com', 'your-password')
    # fetch_emails(mail)
    
if __name__ == "__main__":
    main()

This script demonstrates how to use the Naive Bayes filter in a practical scenario. It includes training with sample data, testing predictions, and an example of integration with an email client using IMAP (commented out for security reasons). Users can adapt the `integrate_with_email_client` function by providing their own credentials and server details.