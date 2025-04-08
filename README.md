## 🧠 Chat with Your Files

Upload multiple documents (PDF, DOCX, TXT, or ZIP), and ask natural language questions based on their content using LLMs. Powered by **LangChain**, **Groq (LLaMA3)**, **FAISS**, and **HuggingFace Embeddings** — all inside a simple **Streamlit** web interface.

---
## 🚀 Features

- 🧾 Supports multiple file types: PDF, DOCX, TXT, ZIP (multi-files inside)
- 🧠 Conversational memory (chat history)
- ⚡ Ultra-fast responses via Groq (LLaMA3-70B)
- 🔍 Retrieves only relevant content from your files
- 🛠️ Runs completely in your local environment

---

## 🧰 Tech Stack

| Tool           | Why It's Used |
|----------------|---------------|
| **Streamlit**  | To build the interactive web app easily. |
| **LangChain**  | For chaining LLM + document retrievers. |
| **Groq LLM (LLaMA3)** | Provides ultra-fast and powerful LLM responses. |
| **FAISS**      | Efficient vector-based document retrieval. |
| **HuggingFace Embeddings** | Converts text to numerical form for FAISS search. |
| **UnstructuredFileLoader** | Supports extra file types for flexibility. |

---

## 📦 Installation

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/yourusername/chat-with-your-files.git
cd chat-with-your-files
```

### 2️⃣ Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install streamlit langchain langchain-community langchain-groq faiss-cpu sentence-transformers
```

---

## 🔐 API Key

Get your **Groq API Key** from: https://console.groq.com/

Then, replace the following line in your `filenmae.py` file:

```python
api_key="your_groq_api_key_here"
```

---

## ▶️ Run the App

```bash
streamlit run filename.py
```

---

## 🗂️ How It Works

1. Upload your files (PDFs, DOCXs, TXTs, ZIP of any of them).
2. Files are loaded and chunked into smaller parts.
3. Each chunk is embedded using HuggingFace transformers.
4. FAISS stores these embeddings for fast similarity search.
5. Groq’s LLaMA3 answers your questions based on the relevant chunks.
6. LangChain handles the full pipeline and maintains chat history.

---

## 📚 Example Use Cases

- Academic research Q&A
- Company document assistant
- Resume screening or HR bots
- Legal or compliance file search
- Custom chatbot for internal data

---
---
##  output

<img width="919" alt="image" src="https://github.com/user-attachments/assets/4605fe73-08cc-447c-bb58-03e546b1d2b9" />
