from django.db import models

class YouTubeVideo(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)  # 자동 생성 날짜/시간
    id = models.BigAutoField(primary_key=True)  # 자동 증가 ID
    like_count = models.BigIntegerField(null=True, blank=True)  # 좋아요 수
    view_count = models.BigIntegerField(null=True, blank=True)  # 조회 수
    description = models.CharField(max_length=100, null=True, blank=True)  # 설명
    title = models.CharField(max_length=255, null=True, blank=True)  # 제목
    url = models.URLField(max_length=255, null=True, blank=True)  # URL
    tag = models.CharField(
        max_length=8, 
        choices=[('NEGATIVE', 'NEGATIVE'), ('NEUTRAL', 'NEUTRAL'), ('POSITIVE', 'POSITIVE')],
        null=True, 
        blank=True
    )  # 태그 (NEGATIVE, NEUTRAL, POSITIVE)

    def __str__(self):
        return self.title or "Untitled Video"
