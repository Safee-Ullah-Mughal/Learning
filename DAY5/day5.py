import json
import os

def add_lead(name, email, company, budget):
    if '@' not in email or '.' not in email:
        print("Please Enter an Valid Email")
        return False
    try:
        budgetinput=float(budget)
    except ValueError:
        print("Budget must be a Nueric Value")
        return False

    if budget >= 10000:
        lead_quality = "Tier 1: High-Value Target 💎"
    elif budget >= 3000:
        lead_quality = "Tier 2: Medium Account 📈"
    else:
        lead_quality = "Tier 3: Standard Lead 🪙"
    lead_data = {
        "name": name,
        "email": email,
        "company": company,
        "budget": budget,
        "category": lead_quality
    }

    # --- STEP 4: APPEND TO THE CENTRAL REGISTRY ---
    filename = "business_leads.json"
    
    # Convert our single lead dictionary into a clean string line
    lead_line = json.dumps(lead_data)
    
    with open(filename, "a") as file:
        file.write(lead_line + "\n")
        
    print(f"💾 Successfully saved {name} to {filename}!")
    return True


add_lead("Khalid", "Khalid@gmail.com","Global Company House", 5500)
add_lead("Bob Jones", "bob@startup.io", "ByteSize Co", 5000)