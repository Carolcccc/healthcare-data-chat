from tools import create_agent
from prompts import SYSTEM_PROMPT

def main():
    csv_path = "healthcare_dataset_cleaned.csv" 
    agent = create_agent(csv_path)
    
    print("--- 🖥️ Local M4 Medical Agent Online ---")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break
            
        full_query = f"{SYSTEM_PROMPT}\n\nUser Question: {user_input}"
        response = agent.invoke(full_query)
        print(f"\nAgent: {response['output']}")

if __name__ == "__main__":
    main()