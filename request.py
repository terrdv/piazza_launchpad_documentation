import requests

url = "https://piazza.com/logic/api?method=network.get_my_feed"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "Sec-Fetch-Site": "same-origin",
    "Accept-Language": "en-CA,en-US;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Sec-Fetch-Mode": "cors",
    "Origin": "https://piazza.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15",
    "Referer": "https://piazza.com/class/mebo7f6nbjr6i5",
    "Content-Length": "89",
    "Sec-Fetch-Dest": "empty",
    "Cookie": "AWSALB=nfQaNtFhVFPKOaVBpLLkx1irqfmY1NNGrU5WR0FzC4Wb1IuHFBcUSGRWbUhsTT8vkfyCCA0hB91lCS/x5HrnGcRSuT03GdP1K9Nb39VcPDVDgZ8zYi5BaDtu6U0i; AWSALBCORS=nfQaNtFhVFPKOaVBpLLkx1irqfmY1NNGrU5WR0FzC4Wb1IuHFBcUSGRWbUhsTT8vkfyCCA0hB91lCS/x5HrnGcRSuT03GdP1K9Nb39VcPDVDgZ8zYi5BaDtu6U0i; piazza_session=2.eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzM4NCJ9.eyJuYmYiOjE3NjIwMjQ2NDQsImRhdGEiOnsiZXhwaXJlcyI6MTc2MzIzNDI0NCwicGVybSI6IjAiLCJsb2dnaW5nX2luIjp0cnVlLCJjcmVhdGVkX2F0IjoxNzYyMDI0NjQ0LCJ3aGVuIjoxNzYyMDI0NjQ0LCJob21lIjoiLyIsInJlbWVtYmVyIjoib24iLCJzZXNzaW9uX3Rva2VuIjoic3RfaHV1RDdOQ0RkTUtPbDNLOE1GdDgiLCJuaWRzIjoibWVibzdmNm5ianI2aTU6MDtsejdlbXNmajl2ZTFmbTowO21kcml0MWhodHlmMTRyOjA7IiwidGFnIjoiIiwidXNlciI6Im0wc3c5NjZ5ZWc1MnBsIiwiZW1haWwiOiJ0ZXJyZHZAc3R1ZGVudC51YmMuY2EifSwiaXNzIjoicGlhenphLmNvbSIsImV4cCI6MTc2MzIzNDI0NH0._gq5ROllW3WaYnVlHtsr9x1saVW3Zx1VrEMeE0NYeJawANgk3UE33wvYuiQASryTroJvSFigINlXOulTPvZgvx3njH5HT0FMzerXaPkpy87OVJHPzTpmZmamV1emDE3V; session_id=7c7836dad5387d136299ea5843fd8738ad40aeea291852c2",
    "CSRF-Token": "7c7836dad5387d136299ea5843fd8738ad40aeea291852c2",
    "Priority": "u=3, i"
}

data = {
    "method": "network.get_my_feed",
    "params": {
        "nid": "mebo7f6nbjr6i5",
        "offset": 10,
        "limit": 10
    }
}

response = requests.post(url, headers=headers, json=data)



# if the API returns gzip, requests automatically handles decompression
print(response.status_code)
print(response.json())  # pretty-prints parsed JSON
