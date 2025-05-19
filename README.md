# llm-fine-tuning

## Text-to-SQL Finetuning Project - Plan of Work

This document outlines the plan of work a project to finetune a Large Language Model (LLM) for Text-to-SQL generation.

## Team Members

* Eryk Zarębski
* Kacper Starzyk
* Szymon Rogowski

## Project Goal

To finetune a pre-trained Large Language Model to accurately translate natural language questions into executable SQL queries for a given database schema.

**Responsibility**

**Tydzień 1: 13.05-20.05**

* Understand Text-to-SQL task, datasets (e.g. [synthetic_text_to_sql](https://huggingface.co/datasets/gretelai/synthetic_text_to_sql)), and evaluation metrics.
* Load, explore, and preprocess the chosen dataset.
* Split data into train and validation sets.
* Use of LLaMA-Factory. Definition and save of training arguments for fine-tuning the Qwen/Qwen3-0.6B model using techniques like LoRA, FP16 precision, and Flash Attention, optimized for efficient supervised fine-tuning on a Text-to-SQL dataset.
* Test of AutoModelForSeq2SeqLM by Hugging Face using the T5-small model for fine-tuning on a Text-to-SQL task.
* Training and evaluation with BLEU scoring and a driver function to generate SQL queries from natural language inputs.

**Tydzień 2: 20.05-27.05**

* Understand LLMs, Transformer architecture, and finetuning concepts.
* Select the pre-trained LLM - small and suitable one.
* Write and execute the Python finetuning code using `transformers`.
* Experiment with hyperparameters and monitor training.
* Contribute model and finetuning sections to the final report.

**Tydzień 3: 27.05-03.06**

* Set up development environment and ensure team access.
* Implement the evaluation metric.
* Evaluate the finetuned model on the test set.
* Perform error analysis on generated SQL queries.
* Contribute evaluation and results sections to the report and prepare the presentation.

**Tydzień 4: 03.06-10.06**
