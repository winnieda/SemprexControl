from semprexcontrol.samc_client import SAMCClient

if __name__ == "__main__":
    client = SAMCClient()
    try:
        result = client.set_addr(1, 38400)
        print(f"Controller initialized: {result}")
    except Exception as e:
        print(f"Error: {e}")
