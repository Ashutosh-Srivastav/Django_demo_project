from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class my_first_API(APIView):
    """Returns a list of APIView features."""

    def get(self, request, format = None):
        my_response_list = ["I am a response",
        "I am called by APIView",
        "Happy learning",
        "Django"]

        return (Response({"Hello":"World", "my_response_list":my_response_list}))
