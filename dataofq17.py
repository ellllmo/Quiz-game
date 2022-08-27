import requests

recp=requests.get("https://opentdb.com/api.php?amount=10&difficulty=medium&type=multiple")
recp.raise_for_status()
data=recp.json()
question_data=data["results"]
