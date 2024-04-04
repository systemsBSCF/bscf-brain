from flask import Flask, request, redirect, abort

app = Flask(__name__)

@app.route('/validate_and_redirect', methods=['GET'])
def validate_and_redirect():
    # Extract parameters from request
    prospect_id = request.args.get('prospect_id')
    sales_rep_id = request.args.get('sales_rep_id')
    target_url = "https://bluesky0capital0funding.streamlit.app/prospect"

    # Redirect to the Streamlit app with parameters
    redirect_url = f"{target_url}?prospect_id={prospect_id}&sales_rep_id={sales_rep_id}"
    return redirect(redirect_url)

if __name__ == '__main__':
    app.run(debug=True)
