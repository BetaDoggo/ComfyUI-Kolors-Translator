import os
import gc
import folder_paths
from llama_cpp import Llama
from huggingface_hub import hf_hub_download

class TranslateToChinese:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "unload_model": ("BOOLEAN", {
                    "default": False,
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("translated_text",)
    FUNCTION = "translate"
    CATEGORY = "Text"

    def translate(self, text, unload_model):
        model_path = os.path.join(folder_paths.models_dir, "ggml", "Yi-1.5-6B-Chat.q5_k.gguf")
        if not os.path.exists(model_path):
            print(f"Downloading translation model to: {model_path}")
            hf_hub_download(repo_id="ZeroWw/Yi-1.5-6B-Chat-GGUF", filename="Yi-1.5-6B-Chat.q5_k.gguf", local_dir=(os.path.join(folder_paths.models_dir, "ggml")))
        
        llm = Llama(model_path=model_path, n_ctx=1024)
        translated_text = llm(
            "English: " + text + "Chinese: ",
            max_tokens=None,
            stop=["English:", "│", "\n"], #It likes to output "|" at the end so this also stops it
        )
        
        if unload_model:
            del llm
            gc.collect()
            print("Translation Model unloaded")
        
        return (translated_text['choices'][0]['text'],)

# Add the node to NODE_CLASS_MAPPINGS and NODE_DISPLAY_NAME_MAPPINGS
NODE_CLASS_MAPPINGS = {
    "TranslateToChinese": TranslateToChinese
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TranslateToChinese": "Translate Prompt With Yi"
}
