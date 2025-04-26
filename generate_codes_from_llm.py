""" 
    Authors
    Student Names:  Feray Lina Yence
    Student IDs:  150190007
"""


import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import json
import os

"""
generate_codes_from_llm.py

This script loads any HuggingFace LLM specified via command line,
reads prompts from 'prompts/' folder (easy.json, moderate.json, hard.json),
and generates Python code files saved under 'Codes/<LLM_Name>/'.

Designed to work with chat-style models (e.g., Mistral, CodeLlama) 
and direct text models (e.g., Octocoder).

Usage:
    python3 generate_codes_from_llm.py --model_name Mistral-7B-Instruct --hf_model_path mistralai/Mistral-7B-Instruct-v0.2
    python3 generate_codes_from_llm.py --model_name CodeLlama-13B-Instruct --hf_model_path codellama/CodeLlama-13b-Instruct-hf
    python3 generate_codes_from_llm.py --model_name octocoder --hf_model_path bigcode/octocoder

"""

# ---- Argument parsing ----
parser = argparse.ArgumentParser(description="Generate code files from a given LLM and prompts.")
parser.add_argument('--model_name', type=str, required=True, help='Folder name for output (example: Qwen2.5-Coder-32B-Instruct)')
parser.add_argument('--hf_model_path', type=str, required=True, help='Huggingface model path (example: Qwen/Qwen2.5-Coder-32B-Instruct)')
args = parser.parse_args()

# Extracted values
model_name = args.model_name
hf_model_path = args.hf_model_path

# Decide whether to use chat template
use_chat_template = model_name not in ["octocoder"]

# ---- Model loading ----
print(f"🔵 Loading model {hf_model_path}...")
model = AutoModelForCausalLM.from_pretrained(hf_model_path, torch_dtype="auto", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(hf_model_path)

# ---- Path settings ----
prompt_folder = "prompts"
output_base_folder = os.path.join("Codes", model_name)

os.makedirs(output_base_folder, exist_ok=True)

difficulty_levels = ["easy", "moderate", "hard"]

# ---- Process each difficulty ----
for difficulty in difficulty_levels:
    prompt_path = os.path.join(prompt_folder, f"{difficulty}.json")

    with open(prompt_path, 'r') as f:
        prompts = json.load(f)

    print(f"\n🟢 Processing {difficulty} prompts...")

    for item in prompts:
        task_id = item["task_id"].replace("/", "_")
        prompt = item["prompt"]

        if use_chat_template:
            messages = [
                {"role": "system", "content": "You are a helpful Python coding assistant. Generate clean Python code following instructions precisely."},
                {"role": "user", "content": prompt}
            ]

            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
        else:
            text = prompt  # Octocoder or non-chat model: use raw prompt

        model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=512
        )

        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

        # Save the result
        output_filename = os.path.join(output_base_folder, f"{difficulty}_HumanEval_{task_id}.py")

        with open(output_filename, 'w') as f:
            f.write(response)

        print(f"Saved: {output_filename}")

print("\n✅ All prompts processed and saved successfully!")
