# 0512_homework

1.  “Javascript는 __(a)__를 조작할 수 있는 유일한 언어이며 전세계에서 가장 인기 있는 프로그래밍 언어 중 하나 이다.” __(a)__에 들어 갈 말을 작성하시오.

   - (a) = 브라우저

2.  Javascript에서 변수를 다룰 때 사용하는 키워드는 크게 var, let, const 3가지가 있다. 각각의 핵심 특징을 나열하고 block scope와 function scope의 차이를 나타내는 예시를 작성하시오. 

   - var :  `funtion-level-scope`를 가지고 , 재할당 및 재선언이 가능하다.

   - let : `block-level-scope`를 가지고, 재할당은 가능하지만, 재선언이 불가하다.

   - const : `block-level-scope`를 가지고 재할당 및 재선언이 모두 불가하다.

     ```javascript
     /** var 경우 */
     var str = "문자열 변수";
      
     if(typeof str === "string"){
         var result = true;
     } else {
         var result = false;
     }        
     console.log("var : " + result);
      
     /** let 경우 */
     var str = "문자열 변수";
      
     if(typeof str === "string"){
         let result = true;
     } else {
         let result = false;
     }        
     console.log("let : " + result);
     // Uncaught ReferenceError: result is not defined
      
     /** const 경우 */
     var str = "문자열 변수";
      
     if(typeof str === "string"){
         const result = true;
     } else {
         const result = false;
     }
     console.log("const : " + result);
     // Uncaught ReferenceError: result is not defined
     ```

     

   - `block-scope` : 우리가 변수를 `{}` 괄호 안에 `const`나 `let`키워드로 선언했을 때, 우리는 `{}`괄호 안에서만 이 변수에 접근할 수 있습니다. 
     블록 스코프는 함수 스코프의 부분집합입니다. 함수는 `{}`괄호로 작성되어야 하기 때문이죠. 물론 화살표 함수로 즉시 리턴하면 `{}`없이 함수를 만들 수도 있습니다. 그렇지 않은 경우에는 모두 `{}`괄호로 작성되어야 하죠.

   - `function-scope` : 함수 내에서 변수를 선언했을 때, 우리는 함수 안에서만 이 변수에 접근할 수 있습니다. 우리가 함수 밖으로 나오게 된 이후에는 함수 내부에 있는 변수에 접근할 수 없습니다.

3.  아래의 설명을 읽고 T/F 여부를 작성하시오. 

   - T
   - F
   - F
   - F 

4.  동등 연산자(==)와 일치 연산자(===)의 차이를 간략히 설명하시오.

   - **동등 연산자**로, 피연산자가 서로 다른 타입이면 타입을 강제로 변환하여 비교한다.
   - **일치 연산자**로, 두 피연산자를 더 정확하게 비교한다.

