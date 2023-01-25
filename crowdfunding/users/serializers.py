from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
		extra_kwargs = {'password': {'write_only': True}, "id": {"read_only": True}, 'first_name': {'required': True},'last_name': {'required': True}}
	# id = serializers.ReadOnlyField()
	# username = serializers.CharField(max_length=200)
	# email = serializers.EmailField()

	def create(self, validated_data):
		user = CustomUser(email = validated_data['email'],username = validated_data['username'],first_name = validated_data['first_name'],last_name = validated_data['last_name'])
		user.set_password(validated_data['password'])
		user.save()
		return user
			# return CustomUser.objects.create(**validated_data)
