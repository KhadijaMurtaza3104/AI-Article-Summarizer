from transformers import pipeline

# Small lightweight model
generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

# Input text
text = "Artificial Intelligence is helping students"

# Generate AI text
result = generator(
    text,
    max_length=30,
    num_return_sequences=1
)

# Print result
print("\nAI GENERATED TEXT:\n")
print(result[0]['generated_text'])