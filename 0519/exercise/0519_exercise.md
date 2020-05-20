# 0519_exercise

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>exercise</title>
  
</head>
<body>
  <h1>Dog Image(s)</h1>
  <hr>

  <h2>강아지</h2>
  <div class="dogs"></div>
  <button id="dog">강아지</button>


  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // 여기에 코드를 작성하시오.
    const url = "https://dog.ceo/api/breeds/image/random"
    const dogInput = document.querySelector('#dog')
    dogInput.addEventListener('click',function(){
      axios.get(url)
      .then(function(event){createImageNode(event.data.message)})
    })
    const createImageNode = function (dogimag) {
      const newImageNode = document.createElement('img')
      newImageNode.src = dogimag
      newImageNode.style.width = "200px"
      newImageNode.style.height = "200px"
      newImageNode.style.objectFit = 'fill'
      console.log(newImageNode)
      const divNode = document.querySelector('.dogs')
      
      divNode.append(newImageNode)
      

    }
    </script>
</body>
</html>
```

