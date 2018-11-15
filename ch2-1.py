# 使用session 展示application context的運作方式
from hello import app
from flask import current_app
current_app.name
app_ctx = app.app_context()
app_ctx.push()  # 將請求應用上下文存入_request_ctx_stack中
current_app.name
app_ctx.pop()  # 將_request_ctx_stack中的應用上下文卸除清空此APP實例
