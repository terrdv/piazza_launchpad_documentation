import requests

#content.get gets the content of a post including replies 
url = "https://piazza.com/logic/api?method=content.get"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "Sec-Fetch-Site": "same-origin",
    "Accept-Language": "en-CA,en-US;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Sec-Fetch-Mode": "cors",
    "Origin": "https://piazza.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15",
    "Referer": "https://piazza.com/class/mebo7f6nbjr6i5/post/427",
    "Sec-Fetch-Dest": "empty",
    "Cookie": "AWSALB=oXbTDkIbrFI6B6k0s2DAgxRvnN5kymwCNP0/gbn9JdB029YF0h+misMWZJXnn86wjzAe0W31mS7+O1O33k2YHPOmoeQ98/MRsut4rDbZzy/5KTfOD3WqFdwQ1TJg; AWSALBCORS=oXbTDkIbrFI6B6k0s2DAgxRvnN5kymwCNP0/gbn9JdB029YF0h+misMWZJXnn86wjzAe0W31mS7+O1O33k2YHPOmoeQ98/MRsut4rDbZzy/5KTfOD3WqFdwQ1TJg; piazza_session=2.eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzM4NCJ9.eyJkYXRhIjp7InBlcm0iOjAsImxvZ2dpbmdfaW4iOnRydWUsIndoZW4iOjE3NjIwMjUzNDUsImhvbWUiOiIvIiwicmVtZW1iZXIiOiJvbiIsIm5pZHMiOiJsejdlbXNmajl2ZTFmbTowO21lYm83ZjZuYmpyNmk1OjA7bWRyaXQxaGh0eWYxNHI6MCIsInRhZyI6IiIsInVzZXIiOiJtMHN3OTY2eWVnNTJwbCIsImVtYWlsIjoidGVycmR2QHN0dWRlbnQudWJjLmNhIiwic2Vzc2lvbl90b2tlbiI6InN0X1l4UWRjdkVoVm1KcldZcnB6TnhtIiwiZXhwaXJlcyI6MTc2MzIzNDk0NiwiY3JlYXRlZF9hdCI6MTc2MjAyNTM0Nn0sIm5iZiI6MTc2MjAyNTM0NiwiZXhwaXJlcyI6MTc2MzIzNDk0NiwiaXNzIjoicGlhenphLmNvbSJ9.Er8SQuAQbOGGJKSJADM3kxEgqXCIN-EFF5bZJuTAUy06dpWdy3nlSBGwgymoFO6WwcD-IUJJWXiinr7zCdhprdTe1LDGQbhgd7uqyNkq6z7k_AUE7VRVjD_GUvHvRdrL; session_id=7c7836dad5387d136299ea5843fd8738ad40aeea291852c2; last_piaz_user=m0sw966yeg52pl",
    "CSRF-Token": "7c7836dad5387d136299ea5843fd8738ad40aeea291852c2",
    "Priority": "u=3, i"
}

payload = {
    "method": "content.get",
    "params": {
        "cid": "427",
        "nid": "mebo7f6nbjr6i5",
        "student_view": None
    }
}

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.json())  # Parse and print as JSON