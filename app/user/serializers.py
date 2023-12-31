from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
      Serializer for ther users object
    """
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """
          Create a new user with encryted password and return it
        """
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validate_data):
        """
          Update a user, setting the password correctly and return it
        """
        # pop is similar to get, and if password
        # is valid the default value is None
        password = validate_data.pop('password', None)
        user = super().update(instance, validate_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """
      Serializer for the user authentication object
    """
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """
          Validate and authenticate the user
        """
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            resquest=self.context.get('request'),
            username=email,
            password=password
        )

        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
