from config import load_cfg
from docs import load_docs, get_chunks, get_embeddings


if __name__ == "__main__":
    cfg = load_cfg()
    paths = cfg["paths"]
    docs = load_docs(input_path=paths["input"], output_path=paths["output"])
    chunks = get_chunks(docs, output_path=paths["output"], **cfg["chunks"])
    embeddings = get_embeddings(chunks, output_path=paths["output"], **cfg["embeddings"])
