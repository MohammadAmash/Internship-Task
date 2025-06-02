import datetime

def dental_chatbot():

    
    clinic_info = {
        "working_hours": "Our working hours are:\n"
                        "Monday-Friday: 8:00 AM - 7:00 PM\n"
                        "Saturday: 9:00 AM - 3:00 PM\n"
                        "Sunday: Closed",
        "location": "We're located at:\n"
                   "Gurugram, Haryana",
        "services": "We offer the following services:\n"
                   "- General dentistry (cleanings, fillings)\n"
                   "- Cosmetic dentistry (whitening, veneers)\n"
                   "- Orthodontics (braces, aligners)\n"
                   "- Oral surgery (extractions, implants)\n"
                   "- Pediatric dentistry",
        "appointments": "To book an appointment:\n"
                       "1. Call us at (555) 123-4567\n"
                       "2. Visit our website at www.smiledental.com\n"
                       "3. Walk in during working hours",
        "emergency": "For dental emergencies:\n"
                    "Call our emergency line at (555) 987-6543\n"
                    "Available 24/7 for registered patients",
        "insurance": "We accept most major dental insurance plans including:\n"
                    "- Delta Dental\n"
                    "- MetLife\n"
                    "- Aetna\n"
                    "- Cigna\n\n"
                    "Please bring your insurance card to your appointment."
    }
    
    # Welcome message

    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        print("Good Morning!")
    elif hour >= 12 and hour < 17:
        print("Good Afternoon!")
    else:
        print("Good Evening!")
        
    print("""
    Welcome to Smile Dental Clinic! 😊
    I'm your virtual assistant. How can I help you today?
    You can ask about:
    - Working hours
    - Location
    - Services
    - Appointments
    - Emergency care
    - Insurance
    (Type 'quit' to exit)
    """)
    
    # Main chat loop
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == 'quit':
            print("Thank you for visiting Smile Dental! Have a great day! 🦷")
            break
            
        # Check for matching questions
        response = None
        
        if any(word in user_input for word in ["hour", "time", "open", "close"]):
            response = clinic_info["working_hours"]
        elif any(word in user_input for word in ["where", "location", "address"]):
            response = clinic_info["location"]
        elif any(word in user_input for word in ["service", "offer", "provide", "do"]):
            response = clinic_info["services"]
        elif any(word in user_input for word in ["appointment", "book", "schedule"]):
            response = clinic_info["appointments"]
        elif any(word in user_input for word in ["emergency", "urgent", "pain"]):
            response = clinic_info["emergency"]
        elif any(word in user_input for word in ["insurance", "cover", "payment"]):
            response = clinic_info["insurance"]
            
        # Handle unknown questions
        if response:
            print("\nAssistant:", response, "\n")
        else:
            print("\nAssistant: Sorry, I don't know that yet. Please call us at (555) 123-4567 for more information.\n")

if __name__ == "__main__":
    dental_chatbot()