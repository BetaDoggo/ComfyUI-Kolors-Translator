# ComfyUI-Kolors-Translator
A custom node designed to complement [KwaiKolorsWrapper](https://github.com/kijai/ComfyUI-KwaiKolorsWrapper) by kijai and hopefully a more flexible implementation in the future.
![image](https://github.com/BetaDoggo/ComfyUI-Kolors-Translator/blob/main/preview.png)
example workflow
# Install:
Automatic:

Use the "install via git url" option in comfyui manager 

Manual:
1. Clone the repo into your custom nodes folder
2. Run `pip install -r requirements.txt`
The translation model will be downloaded on the first run
# Uninstall
Just delete the node's folder, then delete the translation model in models/ggml
# Method and Reasoning
This node uses the Yi-1.5-6B-chat model to do the translation. I found this model to be roughly on par with google translate for English to Chinese. It's small and only takes a few seconds for long prompts on just the cpu. The model is run on cpu with llama-cpp-python to minimize gpu overhead.
