# 0601_exercise



#### TodoView.vue

```html
<template>
  <div>
    <h1>TodoView</h1>
    <TodoInput @create-todo="createTodo"/>
    <TodoList v-bind:todos="todos" />
  </div>
</template>

<script>
import TodoInput from '@/components/TodoInput.vue'
import TodoList from '@/components/TodoList.vue'
export default {
  name : 'TodoView',
  components :{
    TodoInput,
    TodoList,
  },
  data() {
    return {
      todos : [
        {
          id : 1,
          content : 'django복습',
          isCompleted : true,
        },
        {
          id : 2,
          content : 'vue복습',
          isCompleted : false,
        }
      ]
    }
  },
  methods:{
    createTodo(newTodo){
      this.todos.push(newTodo)
    }
  } 
}
</script>

<style>

</style>
```



#### TodoList.vue

```html
<template>
  <div>
    <p>List입니다.</p>
    <li v-for="todo in todos" v-bind:key="todo.id" :class="{completed :todo.isCompleted}">
      <input type="checkbox" v-model ="todo.isCompleted">{{todo.content}}
      {{todo.isCompleted}}

    </li>
  </div>
</template>

<script>
export default {
  name : 'TodoList',
  props : {
    todos : {
      type : Array,
      required : true,
    }
  }

}
</script>

<style>
  .completed {
    text-decoration: line-through;
  }
</style>
```





#### TodoInput.vue

```html
<template>
  <div>
    <input type="text" v-model="todo" @keypress.enter="createTodo">
    <button @click="createTodo">제출</button>
  </div>
</template>

<script>
export default {
  name : 'TodoInput',
  data(){
    return {
      todo : ''
    }
  },
  methods :{
    createTodo(){
      const newTodo ={
        id : Date.now(),
        content : this.todo,
        isCompleted : false,
      }
      this.$emit('create-todo',newTodo)
      this.todo = ""
    },

  }

}
</script>

<style>

</style>
```



#### index.vue

```html
import Vue from 'vue'
import VueRouter from 'vue-router'

import TodoView from '@/views/TodoView.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'TodoView',
    component: TodoView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

```

