import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class ModelHandler:
    def __init__(self):
        self.model_name = "numind/NuExtract-1.5"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = None
        self.tokenizer = None

    def load_model(self):
        if self.model is None:
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                torch_dtype=torch.bfloat16,
                trust_remote_code=True
            ).to(self.device).eval()

            self.tokenizer = AutoTokenizer.from_pretrained(
                self.model_name,
                trust_remote_code=True
            )

    def predict_NuExtract(self, texts, template, example_text, example_json, batch_size=1, max_length=10_000, max_new_tokens=4_000):
        template = json.dumps(json.loads(template), indent=4)
        example_json = json.dumps(json.loads(example_json), indent=4)

        prompts = [
            f"""<|input|>\n### Template:\n{template}\n\n### Example:\n{example_json}\n###
            Example Text:\n{example_text}\n\n### Text:\n{text}\n\n<|output|>"""
            for text in texts
        ]

        outputs = []
        with torch.no_grad():
            for i in range(0, len(prompts), batch_size):
                batch_prompts = prompts[i:i+batch_size]
                batch_encodings = self.tokenizer(
                    batch_prompts,
                    return_tensors="pt",
                    truncation=True,
                    padding=True,
                    max_length=max_length
                ).to(self.device)

                pred_ids = self.model.generate(**batch_encodings, max_new_tokens=max_new_tokens)
                outputs += self.tokenizer.batch_decode(pred_ids, skip_special_tokens=True)

        return [output.split("<|output|>")[1] for output in outputs]

    def extract_information(self, text_content, keys_to_extract, example_text, example_json):
        self.load_model()
        prediction = self.predict_NuExtract([text_content], keys_to_extract, example_text, example_json)[0]
        return json.loads(prediction)