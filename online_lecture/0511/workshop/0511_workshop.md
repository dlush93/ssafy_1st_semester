# 0511_workshop



###  views.py

```python
from django.shortcuts import render
from django.contrib import messages
from .models import Artist,Music,Comment
from rest_framework import status
from .serialzers import ArtistSerializer,ArtistDetailSerializer,MusicSerializer,MusicDetailSerializer,CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def artist_list(request):

    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArtistSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def artist_detail(request,artist_id):
    if request.method == 'GET':
        artist = Artist.objects.get(id=artist_id)
        serializer = ArtistDetailSerializer(artist)
        return Response(serializer.data)
    elif request.method == 'PUT':
        artist = Artist.objects.get(id=artist_id)
        serializer = ArtistDetailSerializer(artist,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        artist = Artist.objects.get(id=artist_id)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def music_list(request):

    if request.method == 'GET':
        musics = Music.objects.all()
        serializer = MusicSerializer(musics, many=True)

        return Response(serializer.data)



@api_view(['GET','PUT','DELETE'])
def music_detail(request,music_id):
    if request.method == 'GET':
        music = Music.objects.get(id=music_id)
        serializer = MusicDetailSerializer(music)
        return Response(serializer.data)
    elif request.method == 'PUT':
        music = Music.objects.get(id=music_id)
        serializer = MusicDetailSerializer(music,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        music = Music.objects.get(id=music_id)
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
def comment_create(request,music_id):
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id = music_id)
        return Response(serializer.data)

@api_view(['PUT','DELETE'])
def comment_detail(request,comment_id):
    if request.method == 'PUT':
        comment = Comment.objects.get(id = comment_id)
        serializer = CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"성공적으로 수정되었습니다.",})
    elif request.method == 'DELETE':
        comment = Comment.objects.get(id = comment_id)
        comment.delete()
        return Response({
                "message":"성공적으로 삭제 되었습니다. ",} )
```



### serializers.py

```python
from rest_framework import serializers
from .models import Artist,Music,Comment


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title',]


class ArtistDetailSerializer(serializers.ModelSerializer):
    musics = MusicSerializer(many=True, read_only=True)
    musics_count = serializers.SerializerMethodField(read_only=True)
    def get_musics_count(self,artist):
        return artist.musics.count()

    class Meta:
        model = Artist
        fields = ['id','name','musics','musics_count']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content']

class MusicDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only = True)
    class Meta:
        model = Music
        fields = ['id','title','comments']
```





### 결과 화면

#### 1. artists/

![image-20200511210921991](0511_workshop.assets/image-20200511210921991.png)



#### 2. artists/<int : artist_id >

​	![image-20200511211000200](0511_workshop.assets/image-20200511211000200.png)





#### 3.  musics/

![image-20200511211032751](0511_workshop.assets/image-20200511211032751.png)





#### 4. musics/<int : music_id>

![image-20200511211127371](0511_workshop.assets/image-20200511211127371.png)





#### 5. musics/<int : music_id >/comments/

![image-20200511234451714](0511_workshop.assets/image-20200511234451714.png)





#### 6. comments/<int : comment_id > /

- PUT

![image-20200511234558949](0511_workshop.assets/image-20200511234558949.png)

![image-20200511234620693](0511_workshop.assets/image-20200511234620693.png)



- DELETE

  ![image-20200511234649255](0511_workshop.assets/image-20200511234649255.png)