// const kakao_share = document.querySelector('.kakao_share')
$(function(){
  let url = window.location.href;
  let img = $('.result_img img').attr('src');

  $("meta[property='og\\:url']").attr('content', url);
  $("meta[property='og\\:image']").attr('content', img);
});


// kakao.init('{{api_key}}');
// function sendLink() {
//   console.log(Kakao.isInitialized());
//   let result_url = window.location.href;
//   Kakao.Link.sendDefault({
//     objectType: 'feed',
//     content: {
//       title: '나의 건강 상태는?',
//       description: '나의 현재 건강 상태는 어떨까?',
//       imageUrl: 'https://ppusyeo.herokuapp.com/', 
//       link: {
//         mobileWebUrl: 'https://ppusyeo.herokuapp.com/',
//         webUrl: 'https://ppusyeo.herokuapp.com/',
//       },
//     },
    
//     social: {
//       likeCount: 100,
//       commentCount: 10,
//       sharedCount: 100,
//     },
//     buttons: [
//       {
//         title: '결과 확인하기',
//         link: {
//           webUrl: result_url,
//           mobileWebUrl: result_url,
//         },
//       },
//       {
//         title: '테스트 해보기',
//         link: {
//           webUrl: 'https://ppusyeo.herokuapp.com/',
//           mobileWebUrl: 'https://ppusyeo.herokuapp.com/',
//         },
//       },
//     ]
//   });
// };

function copyUrl(){
  let tmp = document.createElement('input');
  let url = location.href;

  document.body.appendChild(tmp);
  tmp.value = url;
  tmp.select();
  document.execCommand("copy");
  document.body.removeChild(tmp);

  alert("URL이 복사되었습니다.");
}

function sharefacebook(){
  let url = window.location.href;
  let facebook = 'http://www.facebook.com/sharer/sharer.php?u=';
  let link = facebook + url;
  window.open(link);
}

// kakao_share.addEventListener('click', sendLink)
