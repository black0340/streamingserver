from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ImageSerializer
from .models import Liveimg
from django.http import StreamingHttpResponse
import cv2
# Create your views here.


class PostViewset(viewsets.ModelViewSet):
    queryset = Liveimg.objects.all()
    serializer_class = ImageSerializer

def get_frame(frame):
        try:
            image = frame
            _, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes()
        except:
            pass
def gen():
    while True:
        try:
            frame = cv2.imread(r"/mnt/d/github/django study/streamingserver/media/me.jpg",cv2.IMREAD_COLOR)
            yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' +  get_frame(frame) + b'\r\n\r\n')
        except:
            pass

def livefe(request):
    return StreamingHttpResponse(gen(), content_type="multipart/x-mixed-replace;boundary=frame")