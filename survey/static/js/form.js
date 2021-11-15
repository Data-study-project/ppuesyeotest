function scrollUp() {
  const vheight = $('.test').height();
  $('html, body').animate({
    scrollTop: ((Math.ceil($(window).scrollTop() / vheight) - 1)* vheight)
  }, 500);
}



function scrollDown() {
  const vheight = $('.test').height();
  $('html, body').animate({
    scrollTop: ((Math.floor($(window).scrollTop() / vheight) + 1)* vheight)
  }, 500);
}

$(function(){
  $('.next_btn').click(function(event){
    let divs = $(this).parent().prev().children();
    let inputs = divs.find('input:checked');
    if(inputs.length < 1) {
      alert('아무것도 선택하지 않았습니다.');
      return false;
    }
    event.preventDefault();
    scrollDown();
  });

  $('.next_btn_input').click(function(event){
    let divs = $(this).parent().prev().children();
    let inputs = document.querySelector('.chk').value;
    if(inputs.length < 1) {
      alert('아무것도 선택하지 않았습니다.');
      return false;
    }
    event.preventDefault();
    scrollDown();
  });



  $('.prev_btn').click(function(event){
    event.preventDefault();
    scrollUp();
  });

  $('#form').submit(function(){
    let radios = $('input[type=radio]:checked');
    if(radios.length < 5) {
      alert('아무것도 선택하지 않았습니다!!!');
      return false;
    }
    return true;
  });




  $('html, body').animate({
    scrollTop: 0
  }, 500);
});
