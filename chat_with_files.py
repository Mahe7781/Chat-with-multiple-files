import streamlit as st
import os
import tempfile
import zipfile
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader, UnstructuredFileLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq

st.set_page_config(page_title="🧠 Chat with Your Files", layout="wide")
st.title("🧠 Chat with Multiple Files")
st.markdown("Upload PDFs, DOCX, TXT, or a ZIP of files and ask questions based on their content.")

uploaded_files = st.file_uploader("Upload files (PDF, TXT, DOCX, ZIP)", type=["pdf", "txt", "docx", "zip"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Processing documents..."):
        docs = []

        with tempfile.TemporaryDirectory() as temp_dir:
            for uploaded_file in uploaded_files:
                file_path = os.path.join(temp_dir, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                if uploaded_file.type == "application/zip":
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(temp_dir)
                    for root, _, files in os.walk(temp_dir):
                        for file in files:
                            ext = file.split('.')[-1].lower()
                            full_path = os.path.join(root, file)
                            if ext == "pdf":
                                docs.extend(PyPDFLoader(full_path).load())
                            elif ext == "txt":
                                docs.extend(TextLoader(full_path).load())
                            elif ext == "docx":
                                docs.extend(Docx2txtLoader(full_path).load())
                            else:
                                docs.extend(UnstructuredFileLoader(full_path).load())
                else:
                    ext = uploaded_file.name.split('.')[-1].lower()
                    if ext == "pdf":
                        docs.extend(PyPDFLoader(file_path).load())
                    elif ext == "txt":
                        docs.extend(TextLoader(file_path).load())
                    elif ext == "docx":
                        docs.extend(Docx2txtLoader(file_path).load())
                    else:
                        docs.extend(UnstructuredFileLoader(file_path).load())

        embeddings = HuggingFaceEmbeddings(model_name="my_model")
        vectorstore = FAISS.from_documents(docs, embeddings)

        llm = ChatGroq(
            api_key="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",  # Replace with your actual Groq API key
            model_name="llama3-70b-8192"
        )

        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )

        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            memory=memory,
            return_source_documents=True,
            output_key="answer"
        )

        st.success("Files processed successfully. You can now start chatting.")

        user_question = st.text_input("Ask a question based on the uploaded files:", key="user_input")
        if user_question:
            with st.spinner("Getting answer..."):
                response = qa_chain.invoke({"question": user_question})
                st.write("🧠 **Answer:**", response["answer"])
                with st.expander("📚 Source Documents"):
                    for doc in response["source_documents"]:
                        st.markdown(f"- {doc.metadata.get('source', 'Unknown source')}")
