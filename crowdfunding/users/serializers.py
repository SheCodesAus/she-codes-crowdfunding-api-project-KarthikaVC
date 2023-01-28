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


class ChangePasswordSerializer(serializers.ModelSerializer):
	old_password = serializers.CharField(write_only=True, required=True)
	new_password = serializers.CharField(write_only=True, required=True)
	class Meta:
		model = CustomUser
		fields =('old_password', 'new_password')

	def validate_old_password(self, value):
		user = self.context['request'].user
		if not user.check_password(value):
			raise serializers.ValidationError({"old_password": "Old password is not correct"})
		return value
	
	def update(self, instance, validated_data):
		user = self.context['request'].user
		
		if user.pk != instance.pk:
			raise serializers.ValidationError({"authorize": "You dont have permission to change password for this user."})

		instance.set_password(validated_data['password'])
		instance.save()
		return instance

class UpdateUserSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(required=True)

	class Meta:
		model = CustomUser
		fields = ('username', 'first_name', 'last_name', 'email')
		extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

	def validate_email(self, value):
		user = self.context['request'].user
		if CustomUser.objects.exclude(pk=user.pk).filter(email=value).exists():
			raise serializers.ValidationError({"email": "This email is already in use."})
		return value

	def validate_username(self,value):
		user = self.context['request'].user
		if CustomUser.objects.exclude(pk=user.pk).filter(username=value).exists():
			raise serializers.ValidationError({"username": "This username is already in use."})
		return value
	
	def update(self, instance, validated_data):
		user = self.context['request'].user
		
		if (user.pk != instance.pk):
			raise serializers.ValidationError({"authorize": "You dont have permission to update Profile for this user."})


		instance.first_name = validated_data['first_name']
		instance.last_name = validated_data['last_name']
		instance.email = validated_data['email']
		instance.username = validated_data['username']
		instance.save()
		return instance