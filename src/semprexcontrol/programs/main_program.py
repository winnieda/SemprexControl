import sys
import os

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, "../../")  # Adjust the relative path
sys.path.insert(0, src_dir)

from semprexcontrol.samc_client import SAMCClient

if __name__ == "__main__":
    client = SAMCClient()

    result = client.set_addr(1, 38400)
    print(f"Controller initialized: {result}")
    
    client.reset()
    print("Controller reset to power-on defaults.")

    filter_params = [500, 200, 1400, 500, 100, 50]
    motion_params = [200000, 40000]

    client.def_parms(1, filter_params, motion_params)
    print("Filter and motion parameters defined successfully.")
    
    axis = 1
    border = 100
    while not client.find_range(axis, border):
        print("Finding range...")
    print("Safe travel range determined.")

    # More statements in the order you want them
    # Call functions from client
    # Continue putting inside this try statement (here)
    # make variable equivalent to output of function (such as 'result' above)
    # and print out in easily understood way (such as Controller initialized above)