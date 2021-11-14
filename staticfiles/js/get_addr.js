
$(function(){
  $('.next_btn_input').click(function(event){
    let inputs = document.querySelector('#address_kakao').value;
    console.log(inputs)
    if(inputs.length < 1) {
      console.log('123')
      alert('주소 입력란을 클릭하여 주소를 입력하세요.');
      return false;
    } else {

    }
  });
});