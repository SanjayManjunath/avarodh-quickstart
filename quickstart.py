import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize the OpenAI client to route through the Avarodh Gateway
client = OpenAI(
    base_url="https://api.avarodh.dev/v1",
    api_key=os.environ.get("OPENAI_API_KEY"),
    default_headers={
        # This isolates your enterprise tenant and applies your custom RBAC/guardrails
        "x-plan-id": os.environ.get("AVARODH_WORKSPACE_ID")
    }
)

def main():
    print("🔐 Routing request through Avarodh Zero-Trust Gateway...")
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful financial assistant."},
                {"role": "user", "content": "Summarize the Q3 revenue report."}
            ]
        )
        
        print("\n✅ Response Received:")
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"\n❌ Request Failed or Blocked by Avarodh Policy: {e}")

if __name__ == "__main__":
    main()