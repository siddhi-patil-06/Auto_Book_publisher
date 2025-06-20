# versions/version_store.py

import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection(name="book_versions")

def store_version(doc_id, content, step="writer"):
    collection.add(documents=[content], ids=[doc_id], metadatas=[{"step": step}])
    print(f"✅ Stored version: {doc_id} [{step}]")

def search_versions(query_text):
    return collection.query(query_texts=[query_text], n_results=3)

def rank_with_rl_stub(query_text, documents):
    scored_docs = [(doc, doc.lower().count(query_text.lower())) for doc in documents]
    ranked = sorted(scored_docs, key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in ranked]