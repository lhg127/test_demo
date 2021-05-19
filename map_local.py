import mitmproxy.http
from mitmproxy import http


class Events:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        # if 判断该地址是不是在flow体里，为了排除相同地址加了判断条件“x=”
        # flow.request.url  folw包含请求和响应数据，所以要找flow里的request里的url
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.url and "x=" in flow.request.url:
            # 先修改好数据再打开js.json文件
            with open("js.json", encoding="utf-8") as f:
                # 由于request请求时response暂时是没有数据的，所以使用http.HTTPResponse.make()方法去创建response
                # 200 状态码
                # f.read()响应体
                flow.response = http.HTTPResponse.make(200, f.read())


# 固定写法addons 实列化Event（）
addons = [
    Events()
]
if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    # __file__指当前所要执行的文件
    mitmdump(["-p", "8888", "-s", __file__])
