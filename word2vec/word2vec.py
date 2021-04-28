from gensim.models import Word2Vec
import pandas as pd
import os
import gzip

#from gensim.models import Phrases
from gensim.models.phrases import Phraser

from gensim.test.utils import datapath
from gensim.models.word2vec import Text8Corpus
from gensim.models.phrases import Phrases, ENGLISH_CONNECTOR_WORDS


if __name__ == "__main__":

    file_path = os.path.join(os.getcwd(), 'word2vec', "reviews_combined_amazon.csv")
    combined_reviews = pd.read_csv(file_path)
    #print(combined_reviews.head())

    reviews_title_text_list = combined_reviews['review_title']. \
        apply(lambda x:str(x)) + " " + combined_reviews['review_text']. \
        apply(lambda x:str(x)). \
        to_list()

    sentence_stream = [doc.split(" ") for doc in reviews_title_text_list]

    #print(sentence_stream[0][0:10])

    #bigram = Phrases(sentence_stream, min_count=2,threshold = 5, delimiter=b' ')
    bigram = Phrases(
        sentence_stream, 
        min_count=2, 
        threshold=5, 
        connector_words=ENGLISH_CONNECTOR_WORDS
    )
    bigram_phraser = Phraser(bigram)

    tokens_list = []
    for sent in sentence_stream:
        tokens_ = bigram_phraser[sent]
        tokens_list.append(tokens_)
    
    #print(tokens_list[0:5])

    model = Word2Vec(
        tokens_list, 
        vector_size=200, 
        window=5
    )

    most_similar_lens = model.wv.most_similar('lens')

    #print(most_similar_lens)

    model.wv.save_word2vec_format("word2vec/word2vec_shopping.txt")

    fp = open("word2vec/word2vec_shopping.txt",'rb')
    data = fp.read()

    bindata = bytearray(data)

    with gzip.open("word2vec/word2vec_shopping.txt.gz",'wb') as f:
        f.write(bindata)