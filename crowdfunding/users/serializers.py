from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class CustomUserSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	username = serializers.CharField(max_length=200)
	email = serializers.EmailField()
	first_name = serializers.CharField(max_length=200)
	last_name = serializers.CharField(max_length=200)
	password = serializers.CharField(write_only = True, required = True , validators =[validate_password])

	class Meta:
		model = CustomUser
		fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
		extra_kwargs = {'password': {'write_only': True}, "id": {"read_only": True}, 'first_name': {'required': True},'last_name': {'required': True}}
	

	def create(self, validated_data):
		user = CustomUser.objects.create(
			email = validated_data['email'],
			username = validated_data['username'],
			first_name = validated_data['first_name'],
			last_name = validated_data['last_name']
		)
		user.set_password(validated_data['password'])
		user.save()
		return user
			# return CustomUser.objects.create(**validated_data)
