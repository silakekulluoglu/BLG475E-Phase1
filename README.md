# BLG475E-Phase1 - Software Quality and Testing Project

## Project Description
This repository is for the project of Software Quality and Testing class, ITU 2025, Spring.
The project focuses on evaluating Large Language Models (LLMs) for code and test generation based on the HumanEval dataset.

## Summary
- 30 prompts are randomly selected from HumanEval dataset, 10 from each difficulty level.
- For each prompt, source code and corresponding unit tests were generated using three different LLMs:
  - Mistral-7B-Instruct-v0.3
  - Qwen2.5-Coder-32B-Instruct
  - DeepSeek-Coder-v2-Lite-Instruct
- All generated outputs were executed and validated using pytest to assess correctness.

## Results
- Detailed evaluation is available in the final project report.

## Team Members
- Feray Lina Yence
- Fitnete Guni
- Sıla Keküllüoğlu

## Tools and Environment
- Python 3.11.0
- pytest 8.3.5
- Hugging Face Transformers
- Windows 11 and macOS Sequoia 15.3.2