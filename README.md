**🌐 Language Transition Model**

A language translation project that converts English text into a target language (e.g., Hindi) using pretrained neural machine translation models. Includes accurate sentence-level translation and optional batch translation from datasets.

🔍 Overview

This project focuses on translating English text into another language using state-of-the-art machine translation models. It leverages pretrained Hugging Face models (e.g., MarianMT) and beam search to improve translation accuracy, enabling applications such as multilingual content generation, education, and cross-lingual communication.

🔍 Dataset

Source: Kaggle IIT Bombay English-Hindi Translation Dataset 

Description: The dataset contains paired English and Hindi sentences suitable for training or testing translation models. It provides a reliable resource for evaluating sentence-level translation quality and can be extended to other languages.

🎯 Project Goals

Translate English text into a target language with high accuracy

Handle single-sentence input as well as batch translation from CSV datasets

Compare translation outputs and optimize for readability and grammar

Provide a reusable translation function/module for integration into applications

🧰 Tools & Technologies

Python, Jupyter Notebook – Core development and testing

pandas, numpy – Data handling

Hugging Face Transformers – MarianMTModel and MarianTokenizer for translation

PyTorch – Model inference backend

Optional CSV support – Batch translation

📊 Results

Translations are evaluated qualitatively for accuracy and readability

Beam search improves output consistency and fluency

Works efficiently for both single sentences and dataset-based batch translations

