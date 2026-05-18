from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
from langchain_text_splitters import RecursiveCharacterTextSplitter

class DummyTextSplitter:
    # Dummy class to test RecursiveCharacterTextSplitter
    
    def __init__(self, chunk_size=100, chunk_overlap=20):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def split_sample_text(self):
        sample = "First paragraph with some text.\nThis is still first paragraph.\n\nSecond paragraph starts here.\nIt has multiple sentences.\nAnd continues a bit more.\n\nThird paragraph: The end."
        
        chunks = self.splitter.split_text(sample)
        
        for i, chunk in enumerate(chunks):
            print(f"Chunk {i+1}: {chunk}")
            print(f"Length: {len(chunk)}")
            print("-" * 50)
        
        return chunks

if __name__ == "__main__":
    tester = DummyTextSplitter(chunk_size=50, chunk_overlap=10)
    tester.split_sample_text()
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=300,
    chunk_overlap=0,
    language=Language.PYTHON
)

result = splitter.split_text(text)
print(len(result))

# Optional: See the chunks
for i, chunk in enumerate(result):
    print(f"\n--- Chunk {i+1} (Length: {len(chunk)}) ---")
    print(chunk)