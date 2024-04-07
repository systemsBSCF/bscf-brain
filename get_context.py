from openai import OpenAI
import streamlit as st
def get_context(JSON_data):
    # Initialize the OpenAI client with your API key
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    messages = [
        {"role": "system", "content": "you get JSON data from Zoho CRM and create context for the prospect. you get JSON full of prospact data and return context based on the JSON in plain english."},
        {"role": "user", "content": JSON_data}
            ]

    response = client.chat.completions.create(
                model= "gpt-4",
                messages=messages)
    print(response.choices[0].message)
    return response.choices[0].message
# Main execution starts here
data = """
{
    "data": [
        {
            "Owner": {
                "name": "Aharon Kane",
                "id": "4910408000037406001",
                "email": "aharon@blueskycapitalfunding.com"
            },
            "TZtrigger": false,
            "Generate_Link": false,
            "$sharing_permission": "full_access",
            "Send_email_to_merchant": [],
            "$process_flow": false,
            "Requested_Loan_amount": "$50,000 - $100,000",
            "id": "4910408000120836022",
            "Data_Source": "Custom Function",
            "$approval": {
                "delegate": false,
                "approve": false,
                "reject": false,
                "resubmit": false
            },
            "$data_source_details": {
                "service": "Zoho CRM",
                "function_name": "confirm_inbound_lead"
            },
            "Created_Time": "2024-04-03T18:35:15+03:00",
            "Create_a_2nd_QA": false,
            "Disable_auto_ass": false,
            "unqualified_contact": false,
            "I_just_followed_up": false,
            "Created_By": {
                "name": "Systems",
                "id": "4910408000000310001",
                "email": "systems@blueskycapitalfunding.com"
            },
            "Status2": "Waiting on file/app",
            "$review_process": {
                "approve": false,
                "reject": false,
                "resubmit": false
            },
            "Was_brought_in_previously": false,
            "Method_of_Contact": [
                "Phone - Spoke to Merchant",
                "Text - Engaging With Merchant",
                "Email - No response"
            ],
            "Full_Name": "Christopher Louie",
            "full_app_in": false,
            "Credit_Score": "Excellent",
            "Steve_Priority": false,
            "Sent_to_Asana": false,
            "App_in": false,
            "Record_Status__s": "Available",
            "Reached_Out": false,
            "$orchestration": false,
            "Locked__s": false,
            "Lead_Source": "Inbound Lead - FBT",
            "Tag": [
                {
                    "name": "credit",
                    "id": "4910408000056260014",
                    "color_code": "#F17574"
                }
            ],
            "Keep_ontop": false,
            "$pathfinder": false,
            "Company": "Axent Shutters Blinds and Shades",
            "Email": "sweetlou26@mac.com",
            "$currency_symbol": "$",
            "multiuserringcentralmessagingextension__RC_SMS_Opt_Out": false,
            "I_THIS_WORTH_TIME": false,
            "Last_Activity_Time": "2024-04-03T19:17:37+03:00",
            "revenue": "$40,000 - $75,000",
            "$locked_for_me": false,
            "Has_loans_on_the_business": [],
            "Sent": false,
            "$editable": true,
            "Evg": [],
            "Already_copied_notes": false,
            "$zia_owner_assignment": "owner_recommendation_unavailable",
            "Hotness": "2024-04-03T17:35:15+03:00",
            "Has_there_been_a_Bankruptcy": [],
            "First_Name": "Christopher",
            "Modified_By": {
                "name": "Aharon Kane",
                "id": "4910408000037406001",
                "email": "aharon@blueskycapitalfunding.com"
            },
            "Phone": "2094561476",
            "remove_contact_checkbox": false,
            "Use_of_funds": "Equipment",
            "Modified_Time": "2024-04-03T19:17:05+03:00",
            "Interested": false,
            "$stop_processing": false,
            "Pre_declined": false,
            "Last_Name": "Louie",
            "$in_merge": false,
            "Has_there_been_a_default_on_a_card_mortgage": [],
            "$approval_state": "approved",
            "Verse": false
        }
    ]
}
"""
get_context(data)
