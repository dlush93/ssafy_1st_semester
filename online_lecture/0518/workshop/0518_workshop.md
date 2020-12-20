# 0518_workshop

```javascript
const createTodo = (todoName) =>{ 
      const newList = document.createElement('li')
      // 생성하는 List

      //// 1. 체크박스를 만드는과정
      const newTodoCheckbox = document.createElement('input')
      newTodoCheckbox.type = 'checkbox'
      newList.appendChild(newTodoCheckbox)

      //// 1-1.체크박스를 체크했을때 발생하는 EVENT
      newTodoCheckbox.addEventListener('click',function(event){
        console.log(event)
        console.log(event.target)              
        console.log(event.target.checked) // 이벤트가 발생한 타겟의 checked를 확인하는것인데. 그냥 바로 
                                          //newTodoCheckbox.checked도 되지만 일반적이지 않다.
        if (event.target.checked){
          TodoListLabel.style.textDecoration = "line-through"
          todoComplete.append(newList)


        }
        else{
          TodoListLabel.style.textDecoration = ""  
          toDoList.append(newList)
        }
      })            

      //// 2. 라벨을 만드는 과정 : 이것은 todoName을 입력받아 자동적으로 Text로 넣어준다.
      const TodoListLabel = document.createElement('label')
      TodoListLabel.innerText = todoName+':'
      newList.appendChild(TodoListLabel)


      /// 3.  내가 넣을 ul 태그를 찾아오는 과정
      const toDoList = document.querySelector('#toDoList')
      
      /// 4. 그리고 모든 것을 넣어주는 과정
      toDoList.appendChild(newList)


      // event 과정에서 completed Todo로 옮기기 위해 Selector한 과정
      const todoComplete = document.querySelector('#todoComplete')


      //// 여기는 내가 추가로 workshop을 더 공부하는 과정
      /// edit을 위한 Input태그를 만들어준 과정
      const newTodoEditInput = document.createElement('input')
      newTodoEditInput.type ='text'
      newList.appendChild(newTodoEditInput)

      /// 수정버튼을 만드는 과정
      const newTodoEditBtn = document.createElement('button')
      /// ToDoListLabel 은 TodoList의 Label을 의미한다.
      /// newList 는 TodoList의 ul을 나타내는 것이다.
      newTodoEditBtn.innerText = 'Edit'
      newTodoEditBtn.addEventListener('click',function(){
        TodoListLabel.innerText = newTodoEditInput.value+':'
        newTodoEditInput.value = null
      })
      newList.appendChild(newTodoEditBtn)
      //// 삭제 버튼
      //// newTodoDeleteBtn은 삭제버튼이다.
      const newTodoDeleteBtn = document.createElement('button')
      newTodoDeleteBtn.innerText = 'Delete'
      newTodoDeleteBtn.addEventListener('click',function(){
        newList.remove()
      })
      newList.appendChild(newTodoDeleteBtn)




    }

```

