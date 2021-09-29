let common = require("./function/common");
let $ = new common.env('芥末小程序签到领现金');
$.setOptions({
    headers: {
        'content-type': 'application/json',
        'user-agent': 'jdapp;iPhone;9.4.6;14.2;965af808880443e4c1306a54afdd5d5ae771de46;network/wifi;supportApplePay/0;hasUPPay/0;hasOCPay/0;model/iPhone8,4;addressid/;supportBestPay/0;appBuild/167618;jdSupportDarkMode/0;Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1',
        'referer': 'https://happy.m.jd.com/babelDiy/Zeus/3ugedFa7yA6NhxLN5gw2L3PF9sQC/index.html',
    }
});
eval(common.eval.mainEval($));
async function main(id) {
    let p = {
        url: 'https://api.m.jd.com/',
        form: `functionId=apSignIn_day&body={"linkId":"KRFM89OcZwyjnyOIPyAZxA","serviceName":"dayDaySignGetRedEnvelopeSignService","business":1}&_t=1632877371161&appid=activities_platform`
    }
    await $.curl(p)
    console.log($.source.errMsg)
    p.form = `functionId=signPrizeDetailList&body={"linkId":"KRFM89OcZwyjnyOIPyAZxA","serviceName":"dayDaySignGetRedEnvelopeSignService","business":1,"pageSize":20,"page":1}&_t=1632886260795&appid=activities_platform`
    await $.curl(p)
    for (let i of $.haskey($.source, 'data.prizeDrawBaseVoPageBean.items') || []) {
        if (i.remainTime) {
            console.log(`正在提现:${i.prizeValue}`);
            p.form = `functionId=apCashWithDraw&body={"linkId":"KRFM89OcZwyjnyOIPyAZxA","businessSource":"DAY_DAY_RED_PACKET_SIGN","base":{"prizeType":${i.prizeType},"business":"${i.business}","id":${i.id},"poolBaseId":${i.poolBaseId},"prizeGroupId":${i.prizeGroupId},"prizeBaseId":${i.prizeBaseId}}}&_t=1632886279073&appid=activities_platform`
            await $.curl(p)
            console.log($.source);
        }
    }
}
