# HTTP 基础笔记

## URL 结构

协议://域名/路径?查询参数

示例：

https://httpbin.org/get?keyword=python&page=1

- https：协议
- httpbin.org：域名
- /get：路径
- keyword=python&page=1：查询参数

## 请求方法

- GET：查询
- POST：新增
- PUT：整体修改
- PATCH：部分修改
- DELETE：删除

## Header

- Content-Type：请求体格式
- Authorization：身份凭证
- Accept：期望响应格式

## Body

- 通常用于 POST、PUT、PATCH
- 常见格式是 JSON
- JSON 请求需要设置 Content-Type: application/json

## 常见状态码

- 200：成功
- 201：创建成功
- 400：参数错误
- 401：未登录或 Token 无效
- 403：没有权限
- 404：资源不存在
- 500：服务器错误

## 接口测试检查点

- 状态码是否正确
- 响应字段是否完整
- 错误提示是否清楚
- 响应时间是否正常