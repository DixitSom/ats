from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.db import models

from v1.models import Candidate
from v1.serializers import CandidateModelSerializer


class CandidateListCreateAPIView(ListCreateAPIView):
    """Candidate List Create API View"""

    queryset = Candidate.objects.all()
    serializer_class = CandidateModelSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get("search")
        if query:
            words = query.split(" ")
            filtered_queryset = Candidate.objects.none()
            for word in words:
                filtered_queryset |= queryset.filter(name__icontains=word)
            relavance = sum(
                [
                    models.Case(
                        models.When(name__icontains=word, then=1),
                        default=0,
                        output_field=models.IntegerField(),
                    )
                    for word in words
                ],
            )
            queryset = filtered_queryset.annotate(relavance=relavance).order_by(
                "-relavance", "name"
            )
        return queryset


class CandidateRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Candidate Retrive Update API View"""

    queryset = Candidate.objects.all()
    serializer_class = CandidateModelSerializer
