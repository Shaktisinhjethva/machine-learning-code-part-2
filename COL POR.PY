import nltk
import random
from nltk.corpus import movie_reviews

def extract_features(words):
    return dict([(word, True) for word in words])

def text_classification():
    nltk.download('movie_reviews')
    documents = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)
    featuresets = [(extract_features(words), category) for (words, category) in documents]
    train_set, test_set = featuresets[:1500], featuresets[1500:]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    accuracy = nltk.classify.accuracy(classifier, test_set)
    print("Accuracy:", accuracy)
    while True:
        user_input = input("Enter a sentence to classify (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        features = extract_features(user_input.split())
        sentiment = classifier.classify(features)
        print("Sentiment:", sentiment)

if __name__ == "__main__":
    text_classification()

