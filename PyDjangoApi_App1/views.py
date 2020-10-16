from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        """ Return a list of APIView """
        an_apiview =[
            'Uses HTTP methods as function (get,patch,put,delete)',
            'is similer to a Django View',
            'Give you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!!','an_apiview': an_apiview})
