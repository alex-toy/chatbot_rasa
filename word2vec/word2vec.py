from gensim.models import Word2Vec
import pandas as pd
import os

from gensim.models import Phrases
from gensim.models.phrases import Phraser


if __name__ == "__main__":

    file_path = os.path.join(os.getcwd(), 'word2vec', "reviews_combined_amazon.csv")
    combined_reviews = pd.read_csv(file_path)
    #print(combined_reviews.head())

    reviews_title_text_list = combined_reviews['review_title']. \
        apply(lambda x:str(x)) + " " + combined_reviews['review_text']. \
        apply(lambda x:str(x)). \
        to_list()

    sentence_stream = [doc.split(" ") for doc in reviews_title_text_list]

    print(sentence_stream[0][0:10])
    