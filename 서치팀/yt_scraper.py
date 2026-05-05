# gemmorning 서치팀 - 유튜브 자동 수집기
# 실행: python 서치팀/yt_scraper.py

import json
import urllib.request
import urllib.parse
import datetime
import os
import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# 설정
CHANNEL = "gemmorning"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
ENV_FILE = r"C:\Users\user\Desktop\클로드\gemAI\.env파일들\.env"
DASHBOARD_OUTPUT = r"C:\Users\user\Desktop\클로드\practice\dashboard\output"

# gemmorning 채널 키워드 (아침 힐링 방향)
SEARCH_KEYWORDS = [
    "아침 힐링 숏츠",
    "모닝루틴 자존감",
    "아침 명언 영상",
    "힐링 사자성어",
    "아침 동기부여",
    "따뜻한 사회 뉴스",
    "책 속 좋은 말",
]

def load_api_key():
    with open(ENV_FILE, "r") as f:
        for line in f:
            if line.startswith("YOUTUBE_API_KEY="):
                return line.strip().split("=", 1)[1]
    raise ValueError("YOUTUBE_API_KEY not found")

def search_videos(keyword, api_key, hours=24):
    published_after = (
        datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=hours)
    ).strftime("%Y-%m-%dT%H:%M:%SZ")
    params = urllib.parse.urlencode({
        "part": "snippet", "q": keyword, "type": "video",
        "order": "date", "maxResults": 10,
        "publishedAfter": published_after, "relevanceLanguage": "ko",
        "key": api_key
    })
    url = "https://www.googleapis.com/youtube/v3/search?" + params
    try:
        with urllib.request.urlopen(url, timeout=10) as res:
            return json.loads(res.read()).get("items", [])
    except Exception as e:
        print(f"  오류: {e}")
        return []

def get_video_stats(video_ids, api_key):
    if not video_ids: return {}
    params = urllib.parse.urlencode({"part": "statistics", "id": ",".join(video_ids), "key": api_key})
    url = "https://www.googleapis.com/youtube/v3/videos?" + params
    try:
        with urllib.request.urlopen(url, timeout=10) as res:
            items = json.loads(res.read()).get("items", [])
            return {item["id"]: item.get("statistics", {}) for item in items}
    except: return {}

def run():
    print(f"{'='*50}\n  {CHANNEL} 서치팀 - 유튜브 수집\n  {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n{'='*50}")
    api_key = load_api_key()
    all_results = []
    total_videos = 0

    for keyword in SEARCH_KEYWORDS:
        print(f"\n[키워드] '{keyword}'")
        items = search_videos(keyword, api_key)
        if not items:
            print("  최근 24h 새 영상 없음")
            continue
        video_ids = [item["id"]["videoId"] for item in items if item["id"].get("videoId")]
        stats = get_video_stats(video_ids, api_key)
        videos = []
        for item in items:
            vid_id = item["id"].get("videoId")
            if not vid_id: continue
            snippet = item["snippet"]
            stat = stats.get(vid_id, {})
            views = int(stat.get("viewCount", 0))
            likes = int(stat.get("likeCount", 0))
            print(f"  - {snippet.get('title','')[:50]} | 조회수: {views:,}")
            videos.append({
                "video_id": vid_id,
                "url": f"https://www.youtube.com/watch?v={vid_id}",
                "title": snippet.get("title", ""),
                "channel": snippet.get("channelTitle", ""),
                "published_at": snippet.get("publishedAt", ""),
                "views": views, "likes": likes,
            })
        total_videos += len(videos)
        all_results.append({"keyword": keyword, "videos": sorted(videos, key=lambda x: x["views"], reverse=True)})

    report = {
        "channel": CHANNEL,
        "generated_at": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "total_videos": total_videos,
        "keywords": all_results
    }

    os.makedirs(REPORTS_DIR, exist_ok=True)
    today = datetime.datetime.now().strftime("%Y%m%d")
    report_path = os.path.join(REPORTS_DIR, f"yt_report_{today}.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\n  완료! 총 {total_videos}개 | 저장: {report_path}")
    return report

if __name__ == "__main__":
    run()

