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

**Student 1: Data Management & Preprocessing**

* Understand Text-to-SQL task, datasets (e.g. [synthetic_text_to_sql](https://huggingface.co/datasets/gretelai/synthetic_text_to_sql)), and evaluation metrics.
* Load, explore, and preprocess the chosen dataset (schema linking, formatting).
* Split data into train, validation, and test sets.
* Contribute data-related sections to the final report.

**Student 2: Model & Finetuning**

* Understand LLMs, Transformer architecture, and finetuning concepts.
* Select the pre-trained LLM - small and suitable one.
* Write and execute the Python finetuning code using `transformers`.
* Experiment with hyperparameters and monitor training.
* Contribute model and finetuning sections to the final report.

**Student 3: Evaluation & Analysis**

* Set up development environment and ensure team access.
* Implement the evaluation metric.
* Evaluate the finetuned model on the test set.
* Perform error analysis on generated SQL queries.
* Contribute evaluation and results sections to the report and prepare the presentation.
