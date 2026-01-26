from src.api.base_endpoint import BaseAPI


class AuthAPI(BaseAPI):
    CREATE_ACCOUNT = "/api/createAccount"
    DELETE_ACCOUNT = "/api/deleteAccount"
    LOGIN_VERIFY = "/api/verifyLogin"
    UPDATE_ACCOUNT = "/api/updateAccount"
    USER_DETAIL = "/api/getUserDetailByEmail"

    def __init__(self, base_url):
        super().__init__(base_url)

    def login_user(self, email=None, password=None):
        payload = {k: v for k, v in {"email": email, "password": password}.items() if v is not None}
        return self.post(self.LOGIN_VERIFY, data=payload, raise_for_status="False")

    def create_user(self, user_data):
        return self.post(self.CREATE_ACCOUNT, data=user_data, raise_for_status="False")

    def delete_user(self, email, password):
        payload = {"email": email, "password": password}
        return self.delete(self.DELETE_ACCOUNT, data=payload, raise_for_status="False")
