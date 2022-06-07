# absolute_import : 라이브러리 충돌 방지
from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

# settings 모듈을 celery프로그램에 환경변수로 전달.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'patternProject.settings')

app = Celery('patternProject')

# 장고 설정을 셀러리 설정으로 사용하기 위한 구문
# namespace='CELERY'는 모든 셀러리 관련 설정 키는 'CELERY_' 라는 접두살르 가져야한다는 뜻.
# ex : broker_url -> CELERY_BROKER_URL
app.config_from_object('django.conf:settings', namespace='CELERY')  

#등록된 장고 앱 설정에서 task를 불러옵니다.  
app.autodiscover_tasks()  

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))