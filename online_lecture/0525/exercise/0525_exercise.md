# 0525_exercise

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vue.js</title>
</head>
<body>
  <h1>Vue Start!!!</h1>
  <div id="app" v-bind:title="message" >
    {{ message }}
    {{ name }}
    <h3 v-if="seen == false"> 안녕하세요</h3>
    <h5 v-for="menu in menus">
      {{menu}}
    </h5>
    <button v-on:click="popup">click</button>
    <input type="text" name="" id=""  v-model="name"  placeholder="이름을 입력해주세요">
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>

    // var app = new Vue({
    //   el: '#app',
    //   data: {
    //     message: '안녕하세요 Vue!'
    //   }
    // })
    const myObj = {
      el : '#app',
      data :{
        message : 'Hello',
        name : 'change'
      }
    }

    const app = new Vue({
      el : '#app',
      data :{
        message : 'Hello',
        name : 'change',
        seen : true,
        menus : [
          '짜장면',
          '짬뽕',
          '탕수육'
        ]
      },
      methods :{
        popup : function(){
          const rotate = function(arr){
            let new_Arr = arr.slice(1,3)
            new_Arr.push(arr[0])
            return new_Arr
          }
          this.menus = rotate(this.menus)
        }
      }
    })
  </script>


</body>
</html>
```

