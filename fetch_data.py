import requests

def fetch_data_from_backend(prospect_id):
    # Replace the URL below with the actual URL of your Flask backend
    api_url = "https://obainetwork.replit.app/fetch_user_data"
    params = {"user_id": prospect_id, "module_api_name": 'Accounts'}
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()  # Assuming your Flask API returns JSON
    else:
        # Handle errors or unexpected responses
        return {"error": "Failed to fetch data from backend"}

# Then, you would call this function somewhere in your Streamlit app
# For example, right after retrieving the IDs:

# And use the returned data in your app
