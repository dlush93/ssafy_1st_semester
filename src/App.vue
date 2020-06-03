<template>
  <div id="app">
    
      <nav class="navbar navbar-dark bg-dark sticky-top  justify-content-start">
         <span class="navbar-brand mb-0 h1">Movie App</span>
      <div class="nav-item">
        <router-link class="nav-link text-light text-decoration-none" to="/">Movie</router-link>
      </div>
      <div class="nav-item">
        <router-link class="nav-link text-light text-decoration-none" to="/video">Video</router-link>
      </div>

      </nav>
      
  
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
