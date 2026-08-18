from pathlib import Path


def create_chunks(text: str, chunk_size: int = 500) -> list[str]:
    """
    Divide um texto em blocos de tamanho aproximado.
    """

    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def load_document(file_path: str) -> list[str]:
    """
    Lê um documento Markdown e retorna seus chunks.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    text = path.read_text(encoding="utf-8")

    return create_chunks(text)