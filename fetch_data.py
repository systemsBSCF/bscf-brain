import requests

def fetch_data_from_backend(prospect_id, sales_rep_id):
    # Replace the URL below with the actual URL of your Flask backend
    api_url = "https://your-flask-app-url.com/api/endpoint"
    params = {"prospect_id": prospect_id, "sales_rep_id": sales_rep_id}
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()  # Assuming your Flask API returns JSON
    else:
        # Handle errors or unexpected responses
        return {"error": "Failed to fetch data from backend"}

# Then, you would call this function somewhere in your Streamlit app
# For example, right after retrieving the IDs:

# And use the returned data in your app
