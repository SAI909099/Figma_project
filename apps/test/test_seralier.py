from django.contrib.auth import get_user_model
from django.test import TestCase
from apps.serializers import UserModelSerializer

User = get_user_model()


class TestUserModelSerializer(TestCase):
    def setUp(self):
        User.objects.create_user(username='tursinxon' ,email='tursinxon@gmail.com', password='Tursinali123')
        User.objects.create_user(username='yotsinxon' ,email='yotsinxon@gmail.com', password='Yotsinali123')

    def test_get_user(self):
        obj = User.objects.get(email='yotsinxon@gmail.com')
        data = UserModelSerializer(obj).data
        assert isinstance(data, dict)
        assert data['email'] == 'yotsinxon@gmail.com'
        assert obj.check_password('ASAssd232')