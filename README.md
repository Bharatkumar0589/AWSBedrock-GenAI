##### GenAI with AWS Bedrock and Langchain ######
    Let's build simple LLM applications using AWS Bedrock.
    Let's use Langchain,Bedrock and Streamlit to create a app that uses FAISS as VectorDB.

# Chat with PDF using AWS Bedrock:
A Streamlit application utilizing AWS Bedrock Runtime to chat with PDF files using Titan Embeddings and RetrievalQA.

Description:

    This application uses the AWS Bedrock Runtime to ingest PDF files, generate vector embeddings, and store them in a FAISS index. It then uses RetrievalQA to answer user questions by retrieving relevant context from the PDF files and generating a concise answer.

Features:

    Utilizes AWS Bedrock Runtime for model invocation
    Ingests PDF files using PyPDFDirectoryLoader
    Generates vector embeddings using Titan Embeddings(AWS)
    Stores vector embeddings in a FAISS index
    Uses RetrievalQA to answer user questions
    Uses two LLM models: AI21 and Llama3
    Allows user to update or create vector store
    Displays chat interface with user input and response

Requirements

    AWS Bedrock Runtime client library (boto3)
    Streamlit library for web interface
    Langchain library for RetrievalQA and vector embeddings
    FAISS library for vector store
    PyPDFDirectoryLoader library for PDF ingestion

# Simple LLM application using AI21, Llama3-8B:
Artificial Intelligence Prose Generator:
    LLM application utilizing AWS Bedrock Runtime to generate philosophical prose on Artificial Intelligence.

Description:

    This application uses the AWS Bedrock Runtime to invoke a language model and generate a philosophical prose on Artificial Intelligence. The model is prompted with a philosophical question, and the response is printed to the console.

Features:

    Utilizes AWS Bedrock Runtime for model invocation
    Generates philosophical prose on Artificial Intelligence
    Configurable prompt, max tokens, temperature, and topP parameters

Requirements:

    AWS Bedrock Runtime client library (boto3)
    JSON library for payload serialization

AI21 API request:   
    {
    "modelId": "ai21.j2-mid-v1",
    "contentType": "application/json",
    "accept": "application/json",
    "body": "{\"prompt\":\"this is where you place your input text\",\"maxTokens\":200,\"temperature\":0.8,\"topP\":0.9,\"stopSequences\":[],\"countPenalty\":{\"scale\":0},\"presencePenalty\":{\"scale\":0},\"frequencyPenalty\":{\"scale\":0}}"
  }

Llama3-8B API request: 
    {
    "modelId": "meta.llama3-8b-instruct-v1:0",
    "contentType": "application/json",
    "accept": "application/json",
    "body": "{\"prompt\":\"this is where you place your input text\",\"max_gen_len\":512,\"temperature\":0.5,\"top_p\":0.9}"
   }

# Simple app for AI-Generated Art:
An AI application utilizing AWS Bedrock Runtime to generate a 4K HD image using Stable Diffusion XL model.

Description:

    This application uses the AWS Bedrock Runtime to invoke the Stable Diffusion XL model and generate a 4K HD image of Ramayana in a beach scene with a blue sky, rainy season, and cinematic display. The generated image is saved to a file in the output directory.

Features:

    Utilizes AWS Bedrock Runtime for model invocation
    Generates 4K HD image using Stable Diffusion XL model
    Configurable prompt, cfg scale, seed, steps, width, and height parameters
    Saves generated image to a file in the output directory

Requirements:

    AWS Bedrock Runtime client library (boto3)
    JSON library for payload serialization
    Base64 library for image decoding
    OS library for directory creation

Stable-diffusion API request:
    {
    "modelId": "stability.stable-diffusion-xl-v1",
    "contentType": "application/json",
    "accept": "application/json",
    "body": "{\"text_prompts\":[{\"text\":\"this is where you place your input text\",\"weight\":1}],\"cfg_scale\":10,\"seed\":0,\"steps\":50,\"width\":512,\"height\":512}"
   }

