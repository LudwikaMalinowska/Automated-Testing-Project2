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
        pass

    def api_put(self, id, data):
        pass

    def api_delete(self, id):
        pass
