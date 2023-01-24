from rest_framework import serializers
from .models import CustomUser

# Added by Karthika V - Start Code
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
# Added by Karthika V - End  Code
class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ['id', 'username', 'email', 'password']
		extra_kwargs = {'password': {'write_only': True}, "id": {"read_only": True}}

#  Registration Code  - Added by Karthika V - Start Code 
class RegisterSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=CustomUser.objects.all())])
	password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
	# auth_token = serializers.SerializerMethodField()
	print("inside Register Serialiser")

	class Meta:
		model = CustomUser
		fields = ['id', 'username', 'password','email', 'first_name', 'last_name']
		extra_kwargs = {'first_name': {'required': True},'last_name': {'required': True},"id": {"read_only": True}}

		def create(self,validated_data):
			user = CustomUser(**validated_data)
			user.set_password(validated_data['password'])
			user.save()
			print(f"Printing USER {user}")
			return user

#  Registration Code  - Added by Karthika V - End code

