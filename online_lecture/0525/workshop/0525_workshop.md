# 0525_workshop

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Cat Image!</h1>
  <div id="app">
    <button v-on:click="getCatImg">야옹이</button>
    <img v-bind:src="caturl" alt="" width="200px" height="auto">
    <hr>
    <button v-on:click="addingCatImg">고양이 추가</button>
    <hr>
    <div id="catadd">
      <div v-if="catlist.length !== 0" >
      <img v-for="cat in catlist"   v-bind:src="cat" alt="" height="200px">
      </div>
      <img v-else src="https://www.seoularts.ac.kr/Web-home/func/familyCompany/images/noimg.jpg" alt="">
    </div>
    </div>

  </div>


  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const app = new Vue({
      el : '#app',
      data :{
        caturl : undefined,
        catlist : [],
      },
      methods :{
        getCatImg : function(event){
          console.log(this.caturl)
          const url = 'https://api.thecatapi.com/v1/images/search'
          axios.get(url)
          /// methods안의 또 다른 함수는 arrow function을 쓴다.
            .then((response)=>{
              this.caturl = response.data[0].url
            
            })
            console.log(this.caturl)
        },
        // addingCatImg : function(event){
        //   const url = 'https://api.thecatapi.com/v1/images/search'
        //   axios.get(url)
        //   .then((response)=>{
        //     const catDiv = document.querySelector('#catadd')
        //     const catImg = document.createElement('img')
        //     const addCatUrl = response.data[0].url
        //     catImg.src = addCatUrl
        //     catImg.height = "200px"
        //     catDiv.appendChild(catImg)
            
        //   })
        // }
        addingCatImg : function(enent){
          const url = 'https://api.thecatapi.com/v1/images/search'
          axios.get(url)
          .then((response)=>{
            this.catlist.push(response.data[0].url)
          })
        }
        }

    })



    
    
  </script>
  

</body>
</html>
```

