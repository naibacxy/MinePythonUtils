# -*-  coding: utf-8 -*-
# coder : naibacxy
# codeTime : 20160525074818
# 压力测试工具,用来测试网页运载压力
import threading, time, httplib, random
# 需要测试的url列表, 每一次的访问都会随机取一个
urls = {
    "/universe/login"
}
MAX_PAGE = 10000
SERVER_NAME = "localhost:8088"
TEST_COUNT = 10000
# 由于会使用到多线程,所以这里要开始创建线程的派生类
class RequestThread(threading.Thread):
    # 定义线程的构造函数
    def _init_(self, thread_name):
        threading.Thread._init_(self)
        self.test_count = 0

    # 线程运行的入口函数
    def run(self):
        # 不直接把代码写在run里面是因为也许我们还需要做其他的测试
        i = 0
        while i < TEST_COUNT:
            self.test_performace()
            i += 1
            # self.test_other_things()

    def test_performace(self):
        conn = httplib.HTTPConnection(SERVER_NAME)
        # 模拟Keep-Alive 的访问,HTTP 1.1
        for i in range(0,random.randint(0,100)):
            # 构造一个url,提供随机参数的能力
            url = urls[random.randint(len(urls) - 1)]
            url += str(random.randint(MAX_PAGE))
            # 拼接好url后就开始连接到服务器上
            # print url
            try:
                conn.request("GET",url)
                response = conn.getresponse()
                if response.status == 200:
                    # 状态良好则开始读取返回的数据
                    data = response.read()
                self.test_count += 1
            except:
                continue
        # 记得关闭连接
        conn.close()
























