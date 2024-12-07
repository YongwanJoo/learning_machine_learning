from django.shortcuts import render
from .models import YouTubeVideo
from .utils import fetch_videos

def video_list(request):
    if request.method == "POST":
        query = request.POST.get("query", "")  # 사용자가 입력한 검색어
        add_music = request.POST.get("add_music", False)  # 'Add Music' 버튼 체크 여부

        if query:
            if add_music:  # 'Add Music'이 체크된 경우
                query += " music"
            fetch_videos(query)  # 검색 실행 후 데이터 업데이트

    # 모든 동영상 데이터 가져오기
    videos = YouTubeVideo.objects.all()

    return render(request, "youtube/video_list.html", {"videos": videos})
