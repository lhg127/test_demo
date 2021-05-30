import requests


class BaseApi:
    def request(self, data: dict):  # 定义data为字典类型
        if "url" in data:
            return self.http_request(data)   # 如果data里有url 就把data传给http_request函数

    def http_request(self, data):
        return requests.request(**data)  # 获取data数据对data字典进行解包，并获取响应数据
