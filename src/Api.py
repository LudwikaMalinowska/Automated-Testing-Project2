import requests


class Api:
    apiLink = 'https://jsonplaceholder.typicode.com/todos/'

    def api_get_all(self):
        r = requests.get(self.apiLink)
        if r.status_code == 200:
            return r.json()
        return None

    def api_get_by_id(self, id):
        r = requests.get(self.apiLink + id)
        if r.status_code == 200:
            return r.json()
        return None

    def api_post(self, data):
        r = requests.get(self.apiLink, data=data)
        if r.status_code == 200:
            return r.json()
        return None

    def api_put(self, id, data):
        r = requests.get(self.apiLink + id, data=data)
        if r.status_code == 200:
            return r.json()
        return None

    def api_delete(self, id):
        pass
