# 0518_exeercise

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>0518 exercise & workshop</title>
</head>
<body>
  <h2>Add New Todo</h2>
  <p id="addNewTodo"></p>
  <hr>

  <h2>Todo List</h2>
  <ul id="toDoList"></ul>
  <hr>

  <h2>Completed Tasks</h2>
  <ul></ul>
  <hr>

  <script>
    // 여기에 코드를 작성하시오.
    const newTodoLabel = document.createElement('label')
    newTodoLabel.innerText='Add New Todo:'

    const newTodoInput = document.createElement('input')

    newTodoInput.type = 'email' 
    // newTodoInput.setAttribute('type','text')

    const newTodoBtn = document.createElement('button')
    newTodoBtn.innerText = 'Add'
    const newTodoArea = document.querySelector('#addNewTodo')
    newTodoArea.append(newTodoLabel,newTodoInput,newTodoBtn)



    const createTodo = (todoName) =>{ 
      const newList = document.createElement('li')
      // 생성하는 List
      const newTodoCheckbox = document.createElement('input')
      newTodoCheckbox.type = 'checkbox'
      newList.appendChild(newTodoCheckbox)


      const TodoListLabel = document.createElement('label')
      TodoListLabel.innerText = todoName
      newList.appendChild(TodoListLabel)



      const toDoList = document.querySelector('#toDoList')
      // 넣을 ul을 찾아오는 거
      toDoList.appendChild(newList)
    
    }
    const myList = ['장고복습','프로젝트마무리']
    myList.forEach(createTodo)
    myList.forEach((item)=>{createTodo(item)})





  </script>
</body>
</html>
```

