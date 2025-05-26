# llm-fine-tuning

## Text-to-SQL Finetuning Project - Plan of Work

This document outlines the plan of work a project to finetune a Large Language Model (LLM) for Text-to-SQL generation.

## Team Members

- Eryk Zarębski
- Kacper Starzyk
- Szymon Rogowski

## Project Goal

To finetune a pre-trained Large Language Model to accurately translate natural language questions into executable SQL queries for a given database schema.

## Project structure

```
.
├── data/                          # Directory containing JSON data files
│   ├── dataset_info.json          # File used to generate data for training
│   └── dataset_train.json         # Data file generated using dataset_info.json
├── docs/                          # Directory containing documentation files
├── LLaMA-Factory/                 # Framework for easy and convenient model training using JSON configuration files
├── llama-factory-configs/         # Configuration files for LLaMA-Factory
├── README.md                      # Main file documenting the project
├── requirements/                 
│   └── requirements.txt           # Python dependencies
├── setup-python-env.sh            # Script to set up the project environment
├── src/                           # Utilities for data preprocessing and validation
├── GPTNeoX.ipynb                  # Notebook for training the GPT-NeoX pretrained model
├── Qwen.ipynb                     # Notebook for training the Qwen pretrained model
└── T5-Large.ipynb                 # Notebook for training the T5-Large pretrained model
```

## Project setup

Create environment:
```bash
./setup-python-env.sh
```

**Responsibility**

**Week 1: 13.05-20.05**

- Understand Text-to-SQL task, datasets (e.g. [synthetic_text_to_sql](https://huggingface.co/datasets/gretelai/synthetic_text_to_sql)), and evaluation metrics.
- Load, explore, and preprocess the chosen dataset.
- Split data into train and validation sets.
- Use of LLaMA-Factory. Definition and save of training arguments for fine-tuning the Qwen/Qwen3-0.6B model using techniques like LoRA, FP16 precision, and Flash Attention, optimized for efficient supervised fine-tuning on a Text-to-SQL dataset.
- Test of AutoModelForSeq2SeqLM by Hugging Face using the T5-small model for fine-tuning on a Text-to-SQL task.
- Training and evaluation with BLEU scoring and a driver function to generate SQL queries from natural language inputs.

**Week 2: 20.05-27.05**

- Fine-tune the Qwen/Qwen3-0.6B model using LoRA and evaluate its performance.
- Explore the dataset and improve preprocessing if needed.
- Set up Weights & Biases (W&B) for tracking training metrics, such as loss and accuracy.
- Experiment with basic hyperparameters like learning rate and batch size.
- Test the model on a simple test dataset to verify outputs.

**Week 3: 27.05-03.06**

- Use BLEU scoring to validate the quality of generated SQL queries.
- Add a few basic prompt templates to see their impact on performance.
- Train the model on a slightly larger dataset if results look promising.
- Perform error analysis to identify common mistakes in SQL generation.

**Week 4: 03.06-10.06**

- Test the model by executing generated SQL queries in a database.
- Analyze final training and validation metrics in W&B to visualize model performance.
- Write a short report summarizing results, challenges, and next steps.
- Present the project and gather feedback for potential improvements.

## Notes

- https://yale-lily.github.io/spider
