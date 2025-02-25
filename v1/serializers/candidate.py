from rest_framework import serializers

from v1.models import Candidate


class CandidateModelSerializer(serializers.ModelSerializer):
    """Candidate Model Serializer"""

    phone_number = serializers.CharField(min_length=10, max_length=13)

    class Meta:
        model = Candidate
        fields = "__all__"
