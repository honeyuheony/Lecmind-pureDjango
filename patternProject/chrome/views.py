import fractions
import imp
import cv2, threading, os
from importlib.resources import contents
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from rest_framework import viewsets
from django.views.decorators import gzip
from numpy import save


# @gzip.gzip_page
def chrom(request):
    # try:
    #     cam = VideoCamera()
    #     # cam.save()
    #     return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    # except:
    #     pass
    return render(request, 'chrom.html')


# to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)    # 윈도우 디폴트 카메라 사용
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
        
    def __del__(self):
        self.video.release()
        
    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)   # 이미지파일 byte단위로 읽고 jpg로 디코딩
        return jpeg.tobytes()   # live video를 바이트단위 프레임으로 얻음
        
    def update(self):   # 이미지로부터 비디오 생성
        # if self.grabbed:
        #     print(f'Frame w: {int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))}, Frame h: {int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))}, FPS: {self.video.get(cv2.CAP_PROP_FPS)}')
        
        # try:
        #     if not os.path.exists('./webcam_video'):
        #         os.makedirs('./webcam_video')
        # except OSError:
        #     print ('Error: Creating directory. ' +  './webcam_video')
        
        
        # w = round(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        # h = round(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # fps = int(self.video.get(cv2.CAP_PROP_FPS))
        
        # fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # # de = round(1000/fps)
        # is_record = False
        # cnt=0
        # # cam = cv2.VideoWriter("webcam_vide_"+str(cnt)+".avi", fourcc, 10, (w,h))
        
        while True:
            (self.grabbed, self.frame) = self.video.read()
            
            # if(self.grabbed):
            #     cv2.imshow('camera', self.frame)
                
            #     key = cv2.waitKey(33)
            #     if key == ord('r'):
            #         if is_record:
            #             print('녹화 중지')
            #             is_record = False
            #             out.release()
            #         else:
            #             print('녹화시작')
            #             is_record = True
            #             out = cv2.VideoWriter("webcam_vide_"+str(cnt)+".avi", fourcc, 10, (w,h))
                
            #     if is_record == True:
            #         print("녹화 중")
            #         out.write(self.frame)
                
            #     if(cv2.waitKey(de) != -1):
            #         break
            #     else:
            #         print('no frame')
            #         break
            # else:
            #     print("can't open camera.")
            
            
            self.video.release()
            # out.release()
            cv2.destroyAllWindows()
            
            
            
        #     key = cv2.waitKey(0)
        #     if key == ord('r'):
        #         if is_record:
        #             is_record = False
        #             cam.release()
        #         else:
        #             is_record = True
        #             cam = cv2.VideoWriter("webcam_vide_"+cnt+".avi", fourcc, fps, (w,h))
        #             cam.write()
            
        #     if is_record == True:
        #         print('hi')
        #         cam.write(self.frame)
        #         cv2.circle(img=self.frame, center=(620,15), radius=5, color=(0,0,225), thickness=-1)
        
        # self.video.release()
        # cv2.destroyAllWindows()
            
    
def gen(camera):    # (위의)특정한 프레임으로부터 인코딩된 비디오 얻음       
    while True:
        frame = camera.get_frame()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
        
@gzip.gzip_page
def detectme(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    
        
    

# 프레임단위로 출력할 수 있는지 
# 이미지를 폴더에 저장하기

# 프레임이 없어서 저장이 안됨
# drf ,  장고프레임워크 작성



# to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)    # 윈도우 디폴트 카메라 사용
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
        
    def __del__(self):
        self.video.release()
        
    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)   # 이미지파일 byte단위로 읽고 jpg로 디코딩
        return jpeg.tobytes()   # live video를 바이트단위 프레임으로 얻음
        
    def update(self):   # 이미지로부터 비디오 생성
        while True:
            (self.grabbed, self.frame) = self.video.read()
            self.video.release()
            cv2.destroyAllWindows()

class WebcamViewset(viewsets.ModelViewset):

    def gen(camera):    # (위의)특정한 프레임으로부터 인코딩된 비디오 얻음       
        while True:
            frame = camera.get_frame()
            
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
    @gzip.gzip_page
    def list(request):
        try:
            cam = VideoCamera()
            return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
        except:
            pass


    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     response = StreamingHttpResponse(
    #         request.accepted_renderer.render(self._stream_serialized_data(queryset)),
    #         status=200,
    #         content_type="text/csv",
    #     )
    #     response["Content-Disposition"] = 'attachment; filename="reports.csv"'
    #     return response

    # def _stream_serialized_data(self, queryset):
    #     serializer = self.get_serializer_class()
    #     paginator = Paginator(queryset, self.PAGE_SIZE)
    #     for page in paginator.page_range:
    #         yield from serializer(paginator.page(page).object_list, many=True).data