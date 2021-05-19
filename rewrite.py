import json
import mitmproxy.http


class Event:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        # 修改数据在响应体进行修改
        # if 判断该地址是不是在flow体里，为了排除相同地址加了判断条件“x=”
        # flow.request.url  folw包含请求和响应数据，所以要找flow里的request里的url
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.url and "x=" in flow.request.url:
            # 拿到的响应数据是json结构体，需要转换成python结构体，json.loads方法
            data_js = json.loads(flow.response.text)
            # 在结构体里进行精准定位到需要修改数据的名称，并修改
            data_js["data"]["items"][0]["quote"]["name"] = "坨坨"
            data_js["data"]["items"][0]["quote"]["percent"] = "-2"
            data_js["data"]["items"][0]["quote"]["current"] = "9999999"
            # 数据修改完后，再将python结构体转换乘json结构体，json.dump方法
            flow.response.text = json.dumps(data_js)


# 固定写法addons 实列化Event（）
addons = [
    Event()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
# __file__指当前所要执行的文件
    mitmdump(["-p", "8888", "-s", __file__])
