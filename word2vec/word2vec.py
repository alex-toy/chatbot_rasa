from gensim.models import Word2Vec
import pandas as pd
import os

from gensim.models import Phrases
from gensim.models.phrases import Phraser


if __name__ == "__main__":

    file_path = os.path.join(os.getcwd(), 'word2vec', "reviews_combined_amazon.csv")
    combined_reviews = pd.read_csv(file_path)
    print(combined_reviews.head())

    