# Cloud-Based-RAG-Chatbot-with-Streamlit-and-AWS-Bedrock-Knowledge-Base
## ABOUT THE PROJECT:
This project extended a basic chatbot into a full Retrieval-Augmented Generation (RAG) system using AWS Bedrock Knowledge Base and Streamlit. The chatbot provides document-grounded answers from company filings (e.g., Amazon 10-K), demonstrating how enterprise knowledge can be turned into interactive insights.

## USE CASE EXPLANATION:
RAG bots are crucial for enterprise Q&A, document-based customer service, and automated compliance assistants. This project shows how to build a chatbot that can reference official documents and provide explainable, grounded responses, beneficial to financial analysts, compliance teams, and internal operations.

## HOW IT IS BUILT AND FULL WORKING:

1. Frontend (Streamlit):
- Built an interactive web UI using Streamlit with persistent chat state (st.session_state).
- Supports natural language queries, response streaming, and system messages.
2. Document Preparation:
- Downloaded and preprocessed Amazon’s 2024 10-K SEC filing in HTML.
- Uploaded it to an S3 bucket, then indexed it using Titan Text Embeddings v2 inside AWS Bedrock Knowledge Base.
3. Backend (AWS Bedrock Integration):
- Used the bedrock-agent-runtime client and retrieve_and_generate() method.
- Combined LLM generation (Claude 3.5 Haiku) with retrieval from the uploaded 10-K.
- Knowledge Base ID and model ARN managed securely using .env files.
4. Response Flow:
- User query → checked against document context via Bedrock → generated grounded response using Claude → returned to Streamlit chat.
5. Error Handling and Session Management:
- Robust exception handling using try-except.
- Session-aware chat formatting with chat history.
## OUTPUT AND RESULTS OR BENCHMARKS:
- Successfully retrieved specific facts like business segments, investment priorities, risk disclosures.
- Example query: "What are Amazon’s strategic investment priorities?" → Generated accurate answer from the 10-K.
- Fully deployable chatbot with real-time document-grounded responses.
## SKILLS, TOOLS:
Python, Streamlit, AWS Bedrock, Amazon Claude 3.5, Bedrock Knowledge Base, Titan Text Embeddings v2, OpenSearch vector DB, boto3, environment variable handling (dotenv), RAG principles

## KEYWORDS:
Retrieval-Augmented Generation, AWS Bedrock, LLM, Claude, Titan Embeddings, OpenSearch, SEC 10-K, Knowledge Base, chatbot, document Q&A, enterprise AI, streamlit apps
