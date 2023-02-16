[rewrite_local]
#阿里
^https:\/\/api\.aliyundrive\.com url script-response-body ali.js

[MITM]
hostname = api.aliyundrive.com

var body = $response.body;
var url = $request.url;
var obj = JSON.parse(body);

const vip = “/business/v1.0/users/vip/info”

if (url.indexOf(vip) != -1) {
      obj.data.expire = 253402255586;
      body = JSON.stringify(obj);
}

$done({body});
