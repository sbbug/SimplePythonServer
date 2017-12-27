import BaseHTTPServer



#RequestHandler 继承了 BaseHTTPRequestHandler 并重写了 do_GET 方法，

#其效果如代码所示是返回 Page 的内容

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    '''处理请求并返回页面'''

    #页面模板

    Page = '''\
           <html>

           <body>

           <p><span style = "color:#cf0000">Hello world!</span></p>

           </body>

           </html>
           '''

    #处理一个get请求

    def do_GET(self):

        self.send_response(200)

        self.send_header("Content-Type","text/html")

        self.send_header("Content-Length",str(len(self.Page)))

        self.end_headers()

        self.wfile.write(self.Page)



if __name__=='__main__':

   serverAddress = ('',8080)

   server = BaseHTTPServer.HTTPServer(serverAddress,RequestHandler)

   server.serve_forever()

   
