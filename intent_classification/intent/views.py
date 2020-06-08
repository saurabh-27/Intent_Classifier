from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import IntentSerializer
from .models import Intent
import pickle
from intent.services.intent_service import IntentPred
from intent.apps import IntentConfig


class IntentView(APIView):

    def post(self, request):
        intent_serializer = IntentSerializer(data=request.data)


        if intent_serializer.is_valid():
            intent_serializer.save()
            # call service class
            input_text = intent_serializer.data.get("xyz")
            # Load model
            with open(IntentConfig.model_path, 'rb') as f:
                svc_model= pickle.load(f)

            # Load tfidf
            with open(IntentConfig.vocab_path, 'rb') as f:
                tf_idf= pickle.load(f)

            #
            with open(IntentConfig.id_to_intent, 'rb') as f:
                id_to_intent = pickle.load(f)


            intent_obj = IntentPred(svc_model, tf_idf.vocabulary_,id_to_intent)
            prediction = intent_obj.predict_intent(input_text)

            print("prediction is", prediction)

            return Response(prediction, status=status.HTTP_201_CREATED)
        else:
            return Response(intent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
