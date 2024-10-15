import requests
import json
import time
import os


# 쿠키 값 설정
ltuid_v2 = os.getenv("UID", "default_uid")
ltoken_v2 = os.getenv("TOKEN", "default_token")

# 게임 설정 객체
games = [
    {
        "enable": True,
        "name": "원신",
        "url": "https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=ko-kr&act_id=e202102251931481",
        "successMessage": "원신 출석체크 성공",
        "failureMessage": "원신 출석체크 실패",
    },
    {
        "enable": True,
        "name": "붕괴: 스타레일",
        "url": "https://sg-public-api.hoyolab.com/event/luna/os/sign?lang=ko-kr&act_id=e202303301540311",
        "successMessage": "스타레일 출석체크 성공",
        "failureMessage": "스타레일 출석체크 실패",
    },
    {
        "enable": True,
        "name": "젠레스 존 제로",
        "url": "https://sg-act-nap-api.hoyolab.com/event/luna/zzz/os/sign?lang=ko-kr&act_id=e202406031448091",
        "successMessage": "ZZZ 출석체크 성공",
        "failureMessage": "ZZZ 출석체크 실패",
    },
    {
        "enable": False,
        "name": "붕괴3rd",
        "url": "https://sg-public-api.hoyolab.com/event/mani/sign?lang=ko-kr&act_id=e202110291205111",
        "successMessage": "붕괴3rd 출석 체크 성공",
        "failureMessage": "붕괴3rd 출석 체크 성공",
    },
    {
        "enable": False,
        "name": "미해결사건부",
        "image": "https://i.imgur.com/sbHeD7R.png",
        "url": "https://sg-public-api.hoyolab.com/event/luna/os/sign?lang=ko-kr&act_id=e202308141137581",
        "successMessage": None,
        "failureMessage": None,
    },
]

def main():
    for game in games:
        if game["enable"]:
            headers = {
                "Cookie": f"ltuid_v2={ltuid_v2};ltoken_v2={ltoken_v2};",
                "Referer": "https://act.hoyolab.com/",
                "Origin": "https://act.hoyolab.com",
            }
            if game["name"] == "젠레스 존 제로":
                headers["x-rpc-signgame"] = "zzz"

            
            response = requests.post(game["url"], headers=headers)
            response_json = response.json()

            message = game["successMessage"] if response_json.get("message") == "OK" else game["failureMessage"]

            print(message)

            time.sleep(1)

if __name__ == "__main__":
    main()
