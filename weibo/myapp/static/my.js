function pressThumb(element){
    element.src="static/icon/thumb-2.jpg";
}

function count(e){
  var count=e.value.length;
  document.getElementById('count').innerHTML=count+'/128';

}

function setNewCommentdisply(newcomment){
    if (newcomment.style.display=="inline"){
        newcomment.style.display='none';
    }
    else {
        newcomment.style.display='inline';
    }
}

function getById(id){
    var e=document.getElementById(id);
   return e;
}
function changeDisply(id){
    var e=getById(id);
    setNewCommentdisply(e);
}

function createAcomment(element){//element= <span>
    var newcomment=element.parentNode.nextElementSibling;

    var post_id=newcomment.parentNode.getAttribute('id').replace('post_','');

    var form=newcomment.children[0]

    var textarea=form.children[0];

    var action=form.getAttribute('action')
    action= action.replace('newreply','newcomment');

    action=action.replace(/\d+$/i,post_id);


    form.setAttribute('action',action);
    console.log(form.getAttribute('action'));
    textarea.setAttribute('placeholder','comment');
    // console.log(newcomment);
    setNewCommentdisply(newcomment);
}



function createReplyRect(element){//element = comment <li>

    var name=element.getAttribute('username');
    // console.log(name);
    var comment_id=element.getAttribute('id').replace('comment_','');
    var newcomment=element.parentNode.parentNode.parentNode.children[2];
    console.log(newcomment);
    var form=newcomment.children[0]
    var textarea=form.children[0];


    var action=form.getAttribute('action')

    action=action.replace('newcomment','newreply')
    action=action.replace(/\d+$/i,comment_id);
    // console.log(comment_id);
    form.setAttribute('action',action);
    console.log(form.getAttribute('action'));
    textarea.setAttribute('placeholder','Reply:'+name);
    //
    //
    setNewCommentdisply(newcomment);

}
// function funtime(time){
//     // var time=element.getAttribute('datetime');
//      var now = new Date().getTime();
//      // 下面两种转换格式都可以。
//
//      var tmpTime = Date.parse(time.replace(/-/gi, "/"));
//
//      // 返回值
//
//      var result;
//
//      // 一分钟 1000 毫秒 乘以 60
//
//      var minute = 1000 * 60;
//
//      var hour = minute * 60;
//
//      var day = hour * 24;
//
//      var week = day * 7;
//
//      var month = day * 30;
//
//      var year = day * 365;
//
//      // 现在时间 减去 传入时间 得到差距时间
//
//      var diffValue = now - tmpTime;
//
//      // 小于 0 直接返回
//
//      if (diffValue < 0) {
//
//        return 0;
//
//      }
//
//      // 计算 差距时间除以 指定时间段的毫秒数
//
//      var yearC = diffValue / year;
//
//      var monthC = diffValue / month;
//
//      var weekC = diffValue / week;
//
//      var dayC = diffValue / day;
//
//      var hourC = diffValue / hour;
//
//      var minC = diffValue / minute;
//
//      if (yearC >= 1) {
//
//        console.log("年前");
//
//        result = "" + parseInt(yearC) + "月前";
//
//      } else if (monthC >= 1) {
//
//        console.log(parseInt(monthC) + "月前")
//
//        result = "" + parseInt(monthC) + "月前";
//
//      } else if (weekC >= 1) {
//
//        console.log(parseInt(weekC) + "周前")
//
//        result = "" + parseInt(weekC) + "周前";
//
//      } else if (dayC >= 1) {
//
//        console.log(parseInt(dayC) + "天前")
//
//        result = "" + parseInt(dayC) + "天前";
//
//      } else if (hourC >= 1) {
//
//        console.log(parseInt(hourC) + "小时前")
//
//        // result = "" + parseInt(hourC) + "小时前";
//
//        result = { time: parseInt(hourC), dw: '时' }
//
//      } else if (minC >= 1) {
//
//        console.log(parseInt(minC) + "分钟前")
//
//        result = {time: parseInt(minC),dw:'分'}
//
//        // result = "" + parseInt(minC) + "分钟前";
//
//      } else {
//
//        result = "刚刚";
//
//      }
//
//
//      console.log(result);
//
// }
// function test(test){
//     console.log(test);
// }
