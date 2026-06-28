import os
import requests

def analyze_and_export_lead(company_name, description):
    print(f"\n--- 🤖 Advanced AI Analysis: {company_name} ---")
    
    # 1. OpenRouter Configuration (Make sure to set your environment variable or paste your key safely!)
    api_key = "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"
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # 2. Reusable Prompt Template (The Strict Instructions)
    system_instructions = (
        "You are an elite B2B Enterprise Consultant. Analyze the provided company name and description.\n\n"
        "You MUST respond using strictly this format:\n"
        "### [Company Name] Intelligence Report\n"
        "**Industry:** [Extracted Industry]\n"
        "**Confidence Score:** [Score between 0% and 100% based on description clarity]\n"
        "**Estimated ROI:** [Predicted annual cost savings or efficiency gain, e.g., $15,000/year]\n"
        "**Recommended Automation Priority:** [High / Medium / Low]\n\n"
        "#### Potential Needs\n"
        "- Need 1\n"
        "- Need 2\n"
        "- Need 3\n\n"
        "#### Strategic Sales Pitch\n"
        "[A compelling, 2-sentence value proposition matching their priority]"
    )
    
    user_input_prompt = f"Company Name: {company_name}\nBusiness Description: {description}"
    
    payload = {
        "model": "google/gemini-2.5-flash",
        "messages": [
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": user_input_prompt}
        ],
        "max_tokens": 600
    }
    
    # 3. Send Request
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        result_data = response.json()
        ai_markdown_report = result_data["choices"][0]["message"]["content"]
        
        # Print to terminal
        print(ai_markdown_report)
        
        # 4. EXPORT TO STRUCTURED REPORT (Append Mode)
        filename = "Lead_Intelligence_Directory.md"
        with open(filename, "a", encoding="utf-8") as file:
            file.write(ai_markdown_report + "\n\n---\n\n") # Adds a divider line between reports
            
        print(f"Success! Report appended to {filename}")
    else:
        print("Error communicating with OpenRouter.")
        print(response.text)

# --- EXECUTE LEAD AUTOMATION RUNS ---

# Lead 1: Tech Startup
analyze_and_export_lead(
    company_name="Zeta Logistics Tech",
    description="We run an on-demand delivery fleet tracking software but manually email updates to clients."
)

# Lead 2: Retailer
analyze_and_export_lead(
    company_name="Vintage Threads Boutique",
    description="A local vintage clothing store looking to start selling online but struggling with managing stock."
)