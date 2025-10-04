import streamlit as st
import dotenv
import os
import boto3
import json

dotenv.load_dotenv(override=True)

# Load AWS credentials
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_session_token = os.getenv('AWS_SESSION_TOKEN')
model_arn = os.getenv('MODEL_ARN')

# Initialize Bedrock client
@st.cache_resource
def get_bedrock_client():
    return boto3.client(
        service_name='bedrock-runtime',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token if aws_session_token else None
    )

client = get_bedrock_client()

# Create a simple title
st.title('Chat Bot Demo')
st.subheader("Powered by Amazon Bedrock with Anthropic Claude v2")

# Display the welcome message
with st.chat_message('assistant'):
    st.markdown("Hello there! How can I assist you today?")
    

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing messages
for message in st.session_state.messages:
    
    if message['role'] == 'Assistant':
        display_role = 'assistant'
    else:
        display_role = 'user'

    with st.chat_message(display_role):
        st.markdown(message["content"])   

# Helper function to format chat history
def get_history() -> str:
    """Get the formatted chat history from session state"""
    history_list = [
        f"{record['role']}: {record['content']}" for record in st.session_state.messages
    ]
    return '\r\n'.join(history_list)

def get_response(prompt: str) -> str:
    """Get a response from the Claude model using the Messages API"""
    
    try:
        body = json.dumps({
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": prompt}],
            "anthropic_version": "bedrock-2023-05-31"
        })
        
        response = client.invoke_model(
            body=body,
            modelId=os.getenv('MODEL_ARN'),
            accept="application/json",
            contentType="application/json"
        )
        
        response_body = json.loads(response.get('body').read().decode())
        return response_body['content'][0]['text']
    except Exception as e:
        return f"Error: {str(e)}"
# Create a text input for user messages
prompt = st.chat_input("What's up")

# Add message to history when user submits
if prompt:
    st.session_state.messages.append({"role": "Human", "content": prompt})

    # Display user message
    with st.chat_message("Human"):
        st.markdown(prompt)

    # Get and display assistant response
    with st.chat_message("assistant"):
        history = get_history()
        response = get_response(f"{history}\n\nAssistant:")

        st.markdown(response)
        st.session_state.messages.append({"role": "Assistant", "content": response})
# ----------------------------
# Display all messages
# ----------------------------
for msg in st.session_state.messages:
    role_display = "assistant" if msg["role"] == "Assistant" else "user"
    with st.chat_message(role_display):
        st.markdown(msg["content"])

# ----------------------------
# Chat input + response generation
# ----------------------------
user_input = st.chat_input("Say something...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "Human", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate assistant reply
    with st.chat_message("assistant"):
        history = get_history()
        reply = get_response(f"{history}\n\nAssistant:")
        st.markdown(reply)
        st.session_state.messages.append({"role": "Assistant", "content": reply})
