import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class CommentsSummarizer:
    def __init__(self, model_name: str = "sshleifer/distilbart-cnn-12-6", device: str | None = None) -> None:
        print("Initialising model...")
        self.model_name = model_name
        self.device = device or ("cuda" if torch.cuda.is_available() else 
                                 "mps" if torch.backends.mps.is_available() else "cpu")
        self.tokenizer = None
        self.model = None
        self._modelLoader()

    def _modelLoader(self) -> None:
        print(f"Loading model {self.model_name} on {self.device}...")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        self.model.to(self.device)

    def setModelMode(self, mode: str) -> None:
        if self.model is None:
            raise ValueError("Model not loaded. Call _modelLoader() first.")
        if mode == "train":
            self.model.train()
        elif mode == "eval":
            self.model.eval()
        else:
            raise ValueError("Mode Not Recognized. Use 'train' or 'eval'.")
        
    def preProcessText(self, text: str):
        ... # Implementation of text preprocessing

    def summarize(self):
        ... # Implementation of summarization logic
