from django.apps import AppConfig
from intent_classification.settings import BASE_DIR
import os


class IntentConfig(AppConfig):
    name = 'intent'
    model_path = os.path.join(BASE_DIR, 'intent', 'resources', 'v1', 'svc_model.pkl')
    vocab_path = os.path.join(BASE_DIR, 'intent', 'resources', 'v1', 'tf_idf.pkl')
    id_to_intent= os.path.join(BASE_DIR, 'intent', 'resources', 'v1', 'id_to_intent.pkl')



