from langchain_docling import DoclingLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

FILE_PATH = "2025 campus hiring_Assessment prerequisite.pdf"


def build_rag():
    # 1. Load PDF using Docling
    loader = DoclingLoader(file_path=FILE_PATH)
    docs = loader.load()

    if not docs:
        raise ValueError("Empty PDF or no text extracted")

    # 2. Chunking
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    # Chunk size 500 is enough for demo:
    # small chunks, fast embedding, clear retrieval
    chunks = text_splitter.split_documents(docs)

    if not chunks:
        raise ValueError("No chunks created from document")

    # 3. Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="intfloat/e5-small-v2"
    )

    # 4. Vector store (FAISS flat index)
    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vector_store


def retrieve(query: str, vector_store):
    if not query.strip():
        raise ValueError("Query is empty")

    results = vector_store.similarity_search_with_score(
        query,
        k=3
    )

    if not results:
        return {
            "chunks": [],
            "scores": []
        }

    chunks = [doc.page_content for doc, _ in results]
    scores = [score for _, score in results]

    return {
        "chunks": chunks,
        "scores": scores
    }


if __name__ == "__main__":
    vs = build_rag()

    output = retrieve(
        query="mandatory prerequisites",
        vector_store=vs
    )

    print(output)
