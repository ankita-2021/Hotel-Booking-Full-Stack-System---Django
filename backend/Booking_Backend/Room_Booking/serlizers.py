# from rest_framework import serializers
# from .models import Room, RoomImage, OccupiedDate, User

# class RoomImageSerializer(serializers.ModelSerializer):
#     room = serializers.HyperlinkedRelatedField(view_name='room-detail', queryset = Room.objects.all())
#     class Meta:
#         model = RoomImage
#         fields = ['id', 'image', 'caption', 'room']
    
# class OccupiedDateSerializer(serializers.HyperlinkedModelSerializer):
#     room = serializers.HyperlinkedRelatedField(
#         view_name='room-detail',
#         queryset=Room.objects.all()
#     )
#     user  =  serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())
#     class Meta:
#         model = OccupiedDate 
#         fields = ['url', 'id', 'room', 'date', 'user']   
    
# class RoomSerializer(serializers.HyperlinkedModelSerializer):
#     images = RoomImageSerializer(many=True, read_only=True)
#     OccupiedDate = OccupiedDateSerializer(many=True, read_only=True)
#     class Meta:
#         model = Room
#         fields = ['url', 'id', 'name', 'type', 'pricePerNight', 'currency', 'maxOccupancy', 'description', 'images', 'OccupiedDate']


        
# from django.contrib.auth.hashers import make_password
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'id', 'username', 'email', 'password', 'full_name']
        
#     def validate_password(self, value):
#         return make_password(value)
        
    


from rest_framework import serializers
from .models import Room, RoomImage, OccupiedDate, User


class RoomImageSerializer(serializers.ModelSerializer):

    room = serializers.HyperlinkedRelatedField(
        view_name='room-detail',
        queryset=Room.objects.all()
    )

    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.image.url

    class Meta:
        model = RoomImage
        fields = ['id', 'image', 'caption', 'room']


class OccupiedDateSerializer(serializers.HyperlinkedModelSerializer):
    room = serializers.HyperlinkedRelatedField(
        view_name='room-detail',
        queryset=Room.objects.all()
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all()
    )

    class Meta:
        model = OccupiedDate
        fields = ['url', 'id', 'room', 'user', 'date']


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    occupiedDates = OccupiedDateSerializer(many=True, read_only=True)
    images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = [
            'url',
            'id',
            'name',
            'type',
            'pricePerNight',
            'currency',
            'maxOccupancy',
            'occupiedDates',
            'description',
            'images'
        ]


from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password', 'email', 'full_name']

    def validate_password(self, value):
        return make_password(value)