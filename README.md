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
- Through manual inspection, missing edge cases and boundaries in the LLM-generated tests were identified. Additional unit tests were written to enhance test coverage and reveal logical errors in the generated outputs.
- For outputs that were incorrect or incomplete, the original prompts (but not the code) were clarified or extended to address the issues. These revised prompts were then re-submitted to the same LLMs, and all tests—both human-written and LLM-generated—were re-executed to evaluate the effectiveness of the modifications.

## Results
- LLM-generated tests often lacked boundary coverage and inter-method logic validation, which were uncovered by human-written tests.
- Integration testing highlighted that even when unit tests pass, combined logic may fail in real scenarios.
- For algorithmically complex tasks, Qwen and Deepseek are superior.
- Mistral is not yet reliable for autonomous code generation.
- More detailed evaluation is available in the final project report.

## Team Members
- Feray Lina Yence
- Fitnete Guni
- Sıla Keküllüoğlu

## Tools and Environment
- Python 3.11.0
- pytest 8.3.5
- Hugging Face Transformers
- Windows 11 and macOS Sequoia 15.3.2
