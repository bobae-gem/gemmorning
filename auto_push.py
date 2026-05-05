"""
서치 완료 후 manifest.json 업데이트 + GitHub 자동 push
사용법: python auto_push.py
"""
import json, os, subprocess, glob
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(BASE, "output")

def update_manifest():
    files = sorted(glob.glob(os.path.join(OUTPUT, "search_*.json")), reverse=True)
    rel_files = ["output/" + os.path.basename(f) for f in files]

    # 최신 파일에서 sequence·누적 소재 수 읽기
    total, seq = 0, 0
    if files:
        try:
            with open(files[0], encoding="utf-8") as f:
                d = json.load(f)
            seq   = d.get("run_sequence", 0)
            total = int(d.get("report", {}).get("note", "0개").split("누적 소재 ")[1].split("개")[0]) if "누적 소재" in d.get("report", {}).get("note", "") else seq * 3
        except Exception:
            pass

    manifest = {
        "updated_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "total_materials": total,
        "latest_sequence": seq,
        "files": rel_files
    }
    path = os.path.join(OUTPUT, "manifest.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"✅ manifest.json 업데이트 ({len(rel_files)}개 파일, {total}개 소재)")

def git_push():
    cmds = [
        ["git", "add", "output/", "dashboard.html"],
        ["git", "commit", "-m", f"서치 자동 업데이트 {datetime.now().strftime('%Y-%m-%d %H:%M')}"],
        ["git", "push"],
    ]
    for cmd in cmds:
        result = subprocess.run(cmd, cwd=BASE, capture_output=True, text=True)
        if result.returncode != 0 and "nothing to commit" not in result.stdout + result.stderr:
            print(f"⚠️ {' '.join(cmd)}: {result.stderr.strip()}")
        else:
            print(f"✅ {' '.join(cmd)}")

if __name__ == "__main__":
    update_manifest()
    git_push()
