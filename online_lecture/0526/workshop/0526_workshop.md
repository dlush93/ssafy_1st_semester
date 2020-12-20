# 0526_workshop

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>0526 workshop</title>
  <style>
    /* 취소선 */
    .completed{
      text-decoration: line-through;
    }
  </style>
</head>
<body>
  <!-- 여기에 코드를 작성하시오 -->
  <div id="app">
    <select  v-model="category">
      <option value="all">전체</option>
      <option value="completed">완료</option>
      <option value="active">미완료</option>
    </select>

    <input type="text" v-model="newTodo" v-on:keypress.enter="todoPush">
    <button @click="todoPush">+</button>

    <!-- <li v-for="todo in todos" v-if="todo.status === false" v-on:click="changeStatus(todo)"> -->
    <li v-for="todo in todosBystatus" v-bind:key="todo.id">
      <input type="checkbox" v-model="todo.status" >
      <div  v-bind:class = "{completed:todo.status}" style="display: inline-block;">{{todo.content}}</div>
    </li>
    <!-- <li v-else v-on:click="changeStatus(todo)"> [완료]</li> -->
    <button v-on:click="clearCompletd">완료된 일정 삭제</button>


    
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    // 여기에 코드를 작성하시오
    const app = new Vue({
      el:'#app',
      data : {
        category: 'all',
        todos :[
          {
            id : 1,
            content : 'Vue 복습하기',
            status : false
          },
          {
            id : 2,
            content :  'sleep',
            status : false,
          },
          {
            id : 3,
            content : '저녁하기',
            status : false
          }],
        newTodo : ""
      },
      methods:{
        changeStatus : function(todo)
        { 
          todo.status = !todo.status
        },
        
        todoPush : function(){
          if (this.newTodo.length != false){
          const obj = { 
            id : Date.now(),
            content : this.newTodo,
            status : false
        }
        this.todos.push(obj)
        this.newTodo = ""
      }
      },

        clearCompletd : function(){
          const filterTodos =this.todos.filter((todo)=>{
            return !todo.status
          })
          this.todos = filterTodos
        },
        
      },
      

      computed :{
        todosBystatus : function(){
          console.log('computed')
          if (this.category === 'active'){
            return this.todos.filter((todo)=>{
            return !todo.status
          })

          } else if (this.category === 'completed'){
            return this.todos.filter((todo)=>{
            return todo.status
          })

          } else {
            return this.todos
          }

        }
      }
    })
  </script>
</body>
</html>
```

