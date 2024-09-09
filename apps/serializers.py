from rest_framework import serializers
from django.contrib.auth.models import User
# from .models import VerificationCode
from django.contrib.auth.password_validation import validate_password


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError("User does not exist.")

            if not user.check_password(password):
                raise serializers.ValidationError("Incorrect password.")

            data['user'] = user
            return data
        else:
            raise serializers.ValidationError("Email and password required.")


from .models import VerificationCode, Unit, Essential


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6, write_only=True)

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email not found.")
        return value

    def validate(self, data):
        email = data.get('email')
        code = data.get('code')
        try:
            user = User.objects.get(email=email)
            verification_code = VerificationCode.objects.get(user=user)
            if verification_code.code != code:
                raise serializers.ValidationError("Invalid verification code.")
        except (User.DoesNotExist, VerificationCode.DoesNotExist):
            raise serializers.ValidationError("Invalid credentials.")

        return data



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class EssentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Essential
        fields = ['id', 'name']


class UnitSerializer(serializers.ModelSerializer):
    essential = EssentialSerializer(read_only=True)
    essential_id = serializers.PrimaryKeyRelatedField(queryset=Essential.objects.all(), source='essential', write_only=True)

    class Meta:
        model = Unit
        fields = ['id', 'title', 'essential', 'essential_id', 'is_published']







