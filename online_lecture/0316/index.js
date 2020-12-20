const form = document.querySelector('form');
const users = ['admin', 'ssafy', 'test'];


function isValid(inputData,subs){
  if (subs.indexOf(inputData.username)>=0){
      alert('존재하는회원입니다.')
  }
  else{
      if (inputData.password===inputData.password_confirmation){
          alert(inputData.username+'님 회원축하합니다.')
      }
      else{
          alert('비밀번호가 일치하지 않습니다.')
      }
  }
}

form.addEventListener('submit', function(event) {
  // 각 변수에 담기 위한 코드 입니다. 수정을 금합니다.
  event.preventDefault();
  const formData = new FormData(event.currentTarget);
  const userName = formData.get('username');
  const password = formData.get('password');
  const passwordConfirmation = formData.get('password_confirmation');
  // 개발자 도구를 통해 해당 값들을 모두 확인하세요.
  console.log(userName, password, passwordConfirmation);
  // 위의 값들을 활용하여, 회원가입 로직을 작성하시오.
  var formDat={
    username: userName,
    password: password,
    password_confirmation:passwordConfirmation
   }
  isValid(formDat,users)
})


