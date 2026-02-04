from tools_gemini import create_agent_gemini
from prompts import SYSTEM_PROMPT

def main():
    csv_path = "healthcare_dataset_cleaned.csv"
    
    print("--- 🌟 Gemini Medical Agent Online ---")
    print("💡 Using Google Gemini API")
    print()
    
    try:
        agent = create_agent_gemini(csv_path)
    except ValueError as e:
        print(f"❌ Error: {e}")
        return
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        try:
            full_query = f"{SYSTEM_PROMPT}\n\nUser Question: {user_input}"
            response = agent.invoke(full_query)
            print(f"\nAgent: {response['output']}")
        except Exception as e:
            print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
