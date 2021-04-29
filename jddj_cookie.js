//nodejs专用,手机用boxjs填写
//cookie只要里面的deviceid_pdj_jd=xxx-xxx-xxx;o2o_m_h5_sid=xxx-xxx-xxx关键信息
let cookies = [
  'ck1',
  'ck2'
];
// 判断环境变量里面是否有京东ck
if (process.env.JDDJ_COOKIE) {
  if (process.env.JDDJ_COOKIE.indexOf('&') > -1) {
    cookies = process.env.JDDJ_COOKIE.split('&');
  } else if (process.env.JDDJ_COOKIE.indexOf('\n') > -1) {
    cookies = process.env.JDDJ_COOKIE.split('\n');
  } else {
    cookies = [process.env.JDDJ_COOKIE];
  }
}

module.exports = cookies;