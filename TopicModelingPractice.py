from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
#import seaborn as sns
import pandas as pd
import re
import string
import seaborn as sns


data = pd.read_csv('Joy-11-2021.csv', index_col = 0)
tweets = data['content']


url_regex=r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
punctuations_regex = r'['+re.escape(string.punctuation)+']'
processed_data = []
for t in tweets:
    new_doc = re.sub(url_regex, " ", t)
    new_doc = re.sub(punctuations_regex, " ", new_doc)
    processed_data.append(new_doc)


nltk.download('wordnet')
nltk.download('stopwords')
stopWords = stopwords.words('english')

def tokenize(doc):
    # tokenize the words:
    words = RegexpTokenizer(r'[a-zA-Z]+').tokenize(doc.lower())
    # remove stopwords
    words = [word for word in words if word not in stopWords]
    # lemmatize the tokens
    tokens = (list(map(lambda token: WordNetLemmatizer().lemmatize(token, pos='v'), words)))
    return tokens
tokenized_data = []

for doc in processed_data:
    tokenized_data.append(tokenize(doc))

'''Vectorization Based on Word Frequency'''
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(processed_data)

pca = PCA(2)
pca.fit(vectors.toarray())
docs_pca = pca.transform(vectors.toarray())

plt.figure(figsize = (8, 8))
plt.grid()
# could include the hue parameter but what is the equivalent to dataset.target?
sns.scatterplot(x=docs_pca[:, 0], y = docs_pca[:, 1])
plt.show()
plt.savefig('Word Freq.png')

'''Term Frequency -Inverse Document Frequency'''
vectorizer = TfidfVectorizer(tokenizer = tokenize)
vectors = vectorizer.fit_transform(processed_data)

pca.fit(vectors.toarray())
docs_pca = pca.transform(vectors.toarray())

plt.figure(figsize = (8,8))
plt.grid()
sns.scatterplot(x=docs_pca[:, 0], y = docs_pca[:, 1])
plt.show()
plt.savefig('TF-IDF.png')

'''Topic Modeling'''
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.preprocessing import MinMaxScaler
lda_model = LatentDirichletAllocation(
    n_components = 6,
    max_iter = 10,
    learning_method = 'online',
    learning_offset = 50,
    random_state = 32
)
lda_vectors = lda_model.fit(vectors)

def plot_top_words(model, feature_names, n_top_words, title):
    fig, axes = plt.subplots(2, 3, figsize = (25, 15), sharex = True)
    axes = axes.flatten()
    for topic_idx, topic in enumerate(model.components_):
        top_features_ind = topic.argsort()[: -n_top_words - 1: -1]
        top_features = [feature_names[i] for i in top_features_ind]
        weights = topic[top_features_ind]
        ax = axes[topic_idx]
        ax.barh(top_features, weights, height=0.7)
        ax.set_title(f"Topic {topic_idx + 1}", fontdict={"fontsize": 20})
        ax.invert_yaxis()
        ax.tick_params(axis="both", which="major", labelsize=15)
        for i in "top right left".split():
            ax.spines[i].set_visible(False)
        fig.suptitle(title, fontsize=40)

    plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
    plt.show()
    plt.savefig('JoyTopics.png')
n_top_words = 20
tfidf_feature_names = vectorizer.get_feature_names_out()

plot_top_words(lda_model, tfidf_feature_names, n_top_words, "Topics in LDA model")

