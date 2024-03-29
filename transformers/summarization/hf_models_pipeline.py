# -*- coding: utf-8 -*-
"""hf_models_pipeline.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DkKLaPy5RcuQS7F9aW-JxUW5kR85khVR
"""

!pip install transformers

# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

# Sample paragraph
sample_paragraph = """
Let's go to the Hugging Face website at huggingface.co. Hugging Face offers a section dedicated to tasks where you can tackle natural language processing challenges. Here, you'll find everything you need to begin working on a task: demos, use cases, models, datasets, and more! Let's click on text to image. Here we can find instructions to solve a task related to generating images from text. Let's try out their sample code on Colab, and then we will understand how it all works. In Google Colab, let's create a new notebook. Then we will change the runtime to use a GPU. After that, we will install the required libraries. Then we will import torch since the sample code is PyTorch code. After that, we will copy and execute the code. We can see that an image is getting generated from the given text.
"""

# Tokenize
inputs = tokenizer.encode("summarize: " + sample_paragraph, return_tensors="pt", max_length=1024, truncation=True)

inputs

#Generate summary

summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)

summary_ids

# Decode and print the summary
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print("Generated Summary:", summary)

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("summarization", model="facebook/bart-large-cnn")

# Sample paragraph
sample_paragraph = """
Let's go to the Hugging Face website at huggingface.co. Hugging Face offers a section dedicated to tasks where you can tackle natural language processing challenges. Here, you'll find everything you need to begin working on a task: demos, use cases, models, datasets, and more! Let's click on text to image. Here we can find instructions to solve a task related to generating images from text. Let's try out their sample code on Colab, and then we will understand how it all works. In Google Colab, let's create a new notebook. Then we will change the runtime to use a GPU. After that, we will install the required libraries. Then we will import torch since the sample code is PyTorch code. After that, we will copy and execute the code. We can see that an image is getting generated from the given text.
"""

# Generate summary using pipeline
summary = pipe(sample_paragraph, max_length=150, min_length=40, do_sample=False)

# Print the generated summary
print("Generated Summary:", summary[0]['summary_text'])

