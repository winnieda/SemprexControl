import sys
import os

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, "../../")  # Adjust the relative path
sys.path.insert(0, src_dir)

from semprexcontrol.samc_client import SAMCClient

if __name__ == "__main__":
    client = SAMCClient()
    try:
        result = client.set_addr(1, 38400)
        print(f"Controller initialized: {result}")
        # More statements in the order you want them
        # Call functions from client
        # Continue putting inside this try statement (here)
        # make variable equivalent to output of function (such as 'result' above)
        # and print out in easily understood way (such as Controller initialized above)
    except Exception as e:
        print(f"Error: {e}")
