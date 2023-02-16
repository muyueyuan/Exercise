[rewrite_local]
#一言
^https:\/\/app\.yiyan\.art\/yiyan\/getuserinfoandbooklist url script-response-body https://raw.githubusercontent.com/muyueyuan/Exercise/main/yiyan1.js

[MITM]
hostname = app.yiyan.art

var body = $response.body; // 声明一个变量body并以响应消息体赋值
var objc = JSON.parse(body); // JSON.parse()将json形式的body转变成对象处理

objc = {
  "user": {
    "uid": "3936845",
    "smallavatar": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLWMx3KMBra5dibKiciaxexLJce8icYQH3K3ykhGicSF0tCYkVc01iaK7Lq0O8wjJDePjafgb5B4icFLAYWQ/132",
    "actype": "2",
    "gender": "F",
    "viptype": "4",
    "fanscnt": "0",
    "largeavatar": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLWMx3KMBra5dibKiciaxexLJce8icYQH3K3ykhGicSF0tCYkVc01iaK7Lq0O8wjJDePjafgb5B4icFLAYWQ/132",
    "device": "0",
    "followcnt": "1",
    "username": "佳思的唯一爸爸"
  },
  "booklist": [{
    "datetime": "2023-02-16 06:26:50.0",
    "bookname": "默认文集",
    "ava": "1",
    "bookid": "5665728"
  }]
};

body = JSON.stringify(obj); // 重新打包回json字符串
$done(body); // 结束修改

