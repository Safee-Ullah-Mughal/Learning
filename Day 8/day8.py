import requests

def analyze_business_lead(company_name, description):
    print(f"\n--- 🤖 AI is Analyzing Lead: {company_name} ---")
    
    # 1. OpenRouter Configuration
    # Swap out the key below with your fresh OpenRouter key if needed!
    api_key = "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"
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # 2. Crafting the System Prompt (Giving the AI its professional role)
    system_instructions = (
        "You are an expert B2B Sales Consultant. Your job is to analyze a company's description "
        "and extract their Industry, three Potential Needs that automation could solve, "
        "and a compelling 2-sentence Sales Pitch offering AI solutions."
    )
    
    # 3. Crafting the User Prompt (Injecting the raw business inputs)
    user_input_prompt = f"Company Name: {company_name}\nBusiness Description: {description}"
    
    payload = {
        "model": "google/gemini-2.5-flash", # Using a highly efficient, fast model on OpenRouter
        "messages": [
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": user_input_prompt}
        ],
        "max_tokens": 500  # Safeguards your credits while allowing plenty of space for the pitch
    }
    
    # 4. Sending the POST Request
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        result_data = response.json()
        ai_analysis = result_data["choices"][0]["message"]["content"]
        print("\n--- AI Lead Analysis Result ---")
        print(ai_analysis)
    else:
        print("\n❌ Failed to communicate with AI Engine.")
        print(response.text)

# --- SIMULATE THE REAL-WORLD WORKFLOW ---

# Test Case 1: A Digital Agency
analyze_business_lead(
    company_name="Dough & Co.",
    description="Pizza Cloud kitchen."
)

print("\n" + "="*40 + "\n")

# Test Case 2: A Dental Clinic
analyze_business_lead(
    company_name="Apex Steriteh",
    description="Pakistan based import company, specialized in distribution of infection control (CSSD0 and IVD solution)"
)