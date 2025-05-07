import llama_index_init
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
import streamlit as st

if __name__ == "__main__":
    # Streamlit UI
    st.title("StudIT Chat")

    # create session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    llama_index_init.init()

    documents = SimpleDirectoryReader("./data").load_data()
    vector_index = VectorStoreIndex.from_documents(documents)
    query_engine = vector_index.as_query_engine()

    response = query_engine.query("Wer ist Datenschutzbeauftragter?")
    print(response)
