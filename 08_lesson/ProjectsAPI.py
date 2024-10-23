import requests


class Project:

    def __init__(self, url):
        self.url = url
        self.api_key = self.get_key()

    def get_company_id(self):
        body = {
            "login": "",
            "password": "",
            "name": "Поток_100"
        }
        my_headers = {"Content-Type": "application/json"}
        company_id = requests.post(
            self.url + "/api-v2/auth/companies", headers=my_headers, json=body)
        return company_id.json()["content"][0]["id"]

    def get_key(self):
        body = {
            "login": "",
            "password": "",
            "companyId": self.get_company_id()
        }
        resp = requests.post(self.url + "/api-v2/auth/keys/get", json=body)
        return resp.json()[0]['key']

    def get_project_list(self):
        my_headers = {"Content-Type": "application/json"}
        my_headers["Authorization"] = f"Bearer {self.api_key}"

        projects_list = requests.get(
            self.url + "/api-v2/projects", headers=my_headers)
        return projects_list.json()["content"]


    def get_users_list(self):
        my_headers = {"Content-Type": "application/json"}
        my_headers["Authorization"] = f"Bearer {self.api_key}"

        users_list = requests.get(
            self.url + "/api-v2/users", headers=my_headers)
        return users_list.json()["content"][0]["id"]

    def add_project(self, title, user_id, user_role):
        my_headers = {"Content-Type": "application/json"}
        my_headers["Authorization"] = f"Bearer {self.api_key}"

        body = {
            "title": title,
            "users": {user_id: user_role}
        }

        new_project = requests.post(
            self.url + "/api-v2/projects", headers=my_headers, json=body)
        return new_project.json()

    def edit_title(self, id, new_title):
        my_headers = {"Content-Type": "application/json"}
        my_headers["Authorization"] = f"Bearer {self.api_key}"

        body = {
            "title": new_title
        }
        edited_project = requests.put(
            self.url + "/api-v2/projects/" + id, headers=my_headers, json=body)
        return edited_project.json()["id"]

    def edit_user_role(self, id, user_id, new_user_role):
        my_headers = {"Content-Type": "application/json"}
        my_headers["Authorization"] =f"Bearer {self.api_key}"

        body = {
            "users": {user_id: new_user_role}
        }
        edited_user_role = requests.put(
            self.url + "/api-v2/projects/" + id, headers=my_headers, json=body)
        return edited_user_role.json()["id"]

    def delete_project(self, id, deleted):
        my_headers = {"Content-Type": "application/json"}
        my_headers["Authorization"] = f"Bearer {self.api_key}"

        body = {
            "deleted": deleted
        }
        delete = requests.put(
            self.url + "/api-v2/projects/" + id, headers=my_headers, json=body)
        return delete.json()["id"]

    def get_project_by_id(self, id):
        my_headers = {"Content-Type": "application/json"}
        my_headers["Authorization"] = f"Bearer {self.api_key}"

        get_project = requests.get(
            self.url + "/api-v2/projects/" + str(id), headers=my_headers)
        return get_project.json()
