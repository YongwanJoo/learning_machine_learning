from googleapiclient.discovery import build
from .models import YouTubeVideo

API_KEY = "AIzaSyC3CTEnxt1T_Ye2ecxwYoE_HzEtyyQ1FmM"

def fetch_videos(query, max_results=50):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    
    # YouTube API를 통해 검색 요청
    search_response = youtube.search().list(
        q=query,
        part="id,snippet",
        type="video",
        maxResults=max_results,
    ).execute()

    for item in search_response["items"]:
        video_id = item["id"]["videoId"]

        # 동영상 세부 정보 가져오기
        video_details = youtube.videos().list(
            part="statistics,snippet",
            id=video_id
        ).execute()

        for detail in video_details["items"]:
            title = detail["snippet"]["title"]
            description = detail["snippet"].get("description", "")
            stats = detail["statistics"]
            view_count = int(stats.get("viewCount", 0))  # 조회 수 가져오기
            like_count = int(stats.get("likeCount", 0))  # 좋아요 수 가져오기
            url = f"https://www.youtube.com/watch?v={video_id}"

            # YouTubeVideo 모델 데이터 저장 또는 업데이트
            YouTubeVideo.objects.update_or_create(  # 오타 수정
                url=url,  # URL로 고유한 동영상 식별
                defaults={
                    "title": title,
                    "description": description,
                    "view_count": view_count,
                    "like_count": like_count,
                }
            )
