from django.urls import path

from v1.apis import (
    CandidateListCreateAPIView,
    CandidateRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path(
        "candidate/", CandidateListCreateAPIView.as_view(), name="candidate-list-create"
    ),
    path(
        "candidate/<pk>/",
        CandidateRetrieveUpdateDestroyAPIView.as_view(),
        name="candidate-retrieve-update-destroy",
    ),
]
