from transformers import T5Tokenizer, T5ForConditionalGeneration

class Generator:
    def __init__(self, model_name="t5-small"):
        # Add legacy=False if you want the new tokenizer behavior
        self.tokenizer = T5Tokenizer.from_pretrained(model_name, legacy=True)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)

    def generate(self, context, query):
        input_text = f"context: {context} query: {query}"
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)