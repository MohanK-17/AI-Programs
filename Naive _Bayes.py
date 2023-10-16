import re
import numpy as np

# Sample training data
data = [
    ("This is a spam email", "spam"),
    ("Buy one get one free", "spam"),
    ("Hello, how are you?", "ham"),
    ("Congratulations, you've won a prize!", "spam"),
    ("Meeting at 3 PM", "ham"),
    ("Get a discount on your next purchase", "spam"),
]

# Preprocess the training data
word_set = set()

# Loop through each training example
for text, label in data:
    # Tokenize the text by finding words (ignores punctuation and converts to lowercase)
    words = re.findall(r"\w+", text.lower())
    # Add the words to a set to get unique words
    word_set.update(words)

# Convert the set of unique words to a list and sort it
word_list = list(word_set)
word_list.sort()

# Create a vocabulary
vocab = {word: index for index, word in enumerate(word_list)}

# Initialize counts for spam and ham
# Count how many spam and ham messages are in the training data
spam_count = sum(1 for _, label in data if label == "spam")
ham_count = sum(1 for _, label in data if label == "ham")

# Count the occurrences of words in spam and ham messages
# Create arrays to count how many times each word appears in spam and ham messages
spam_word_count = np.zeros(len(vocab))
ham_word_count = np.zeros(len(vocab))

# Populate the counts
# Loop through the training data again
for text, label in data:
    # Tokenize the text
    words = re.findall(r"\w+", text.lower())
    # Choose the appropriate word count array based on the label
    label_count = spam_word_count if label == "spam" else ham_word_count
    for word in words:
        if word in vocab:
            # Find the index of the word in the vocabulary
            word_index = vocab[word]
            # Increment the word count for that word
            label_count[word_index] += 1

# Calculate the prior probabilities
# Calculate the probability that a message is spam or ham
total_messages = len(data)
prior_spam = spam_count / total_messages
prior_ham = ham_count / total_messages

# Input text to classify
input_text = input("Enter the fact:")

# Tokenize and process the input text
input_words = re.findall(r"\w+", input_text.lower())

# Calculate likelihoods and apply the Naive Bayes formula
# Calculate the probability of the input text being spam or ham
likelihood_spam = 1.0
likelihood_ham = 1.0

# Loop through the words in the input text
for word in input_words:
    if word in vocab:
        # Find the index of the word in the vocabulary
        word_index = vocab[word]
        # Calculate the likelihood of the word given spam or ham and update the probabilities
        likelihood_spam *= (spam_word_count[word_index] + 1) / (spam_count + len(vocab))
        likelihood_ham *= (ham_word_count[word_index] + 1) / (ham_count + len(vocab))

# Apply Bayes' theorem
# Calculate the probability that the input text is spam or ham using Bayes' theorem
posterior_spam = (likelihood_spam * prior_spam) / (
    (likelihood_spam * prior_spam) + (likelihood_ham * prior_ham)
)
posterior_ham = 1 - posterior_spam

# Make a classification decision
# Compare the probabilities and classify the input text as spam or ham
if posterior_spam > posterior_ham:
    print("Classified as: Spam")
else:
    print("Classified as: Ham")
