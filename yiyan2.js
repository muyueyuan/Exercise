[rewrite_local]
#一言验证
^https:\/\/app\.yiyan\.art\/yiyan\/checkpro url script-response-body yiyan2.js

[MITM]
hostname = app.yiyan.art

var body = $response.body; // 声明一个变量body并以响应消息体赋值
var obj = JSON.parse(body); // JSON.parse()将json形式的body转变成对象处理

obj.data.viptype = "4";

body = JSON.stringify(obj); // 重新打包回json字符串
$done(body); // 结束修改
