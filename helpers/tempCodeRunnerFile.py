import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ollama.client import heartbeat, list  # Adjust this line if necessary

if __name__ == "__main__":
    print(heartbeat())
    
    models = list()
    if models is not None:
        print("Available models:")
        for model in models:
            print(model)
    else:
        print("Failed to retrieve models.")
