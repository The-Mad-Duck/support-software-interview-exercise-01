import urllib.request, json
try:
    with urllib.request.urlopen("http://localhost:5000/batch_jobs?filter[max_nodes]=20") as url:
        data = json.load(url)
        print(json.dumps(data, indent=4))
except Exception as e:
    print(e)