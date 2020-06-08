import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import  stopwords
stop_words=stopwords.words('english')
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import re
from nltk import RegexpTokenizer



class IntentPred(object):


    def __init__(self,model,vocabulary,id_to_intent):
        self.model = model
        self.vocabulary=vocabulary
        self.id_to_intent = id_to_intent



    def clean_text(self, text):
        tokenized_text = word_tokenize(str(text))
        cleaned_text = " ".join(tokenized_text)
        cleaned_text = " ".join((word) for word in cleaned_text.split() if word not in stop_words)
        return cleaned_text

    def predict_intent(self, text):

        cleaned_text = self.clean_text(text)
        tfidf_obj = TfidfVectorizer(vocabulary=self.vocabulary)
        X = tfidf_obj.fit_transform([cleaned_text]).toarray()
        predicted_value = self.model.predict(X)
        for key in self.id_to_intent.keys():
            if key == predicted_value:
                prediction= self.id_to_intent[key]

        return prediction


if __name__ == "__main__":


    filename = "svc_model.pkl"
    with open(filename ,'rb') as f:
        svc_model = pickle.load(f)

    filename = "tf_idf.pkl"
    with open(filename ,'rb') as f:
        tf_idf= pickle.load(f)

    filename = "id_to_intent.pkl"
    with open(filename, 'rb') as f:
        id_to_intent = pickle.load(f)

    #print(tfidf_obj.vocabulary_)



    intent_obj = IntentPred(svc_model,tf_idf.vocabulary_,id_to_intent)
    predicted_value = intent_obj.predict_intent('Can I book bmw in advance?')
    print("\n",predicted_value)









