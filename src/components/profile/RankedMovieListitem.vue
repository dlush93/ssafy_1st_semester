<template>
  <tr>
    <th scope="row">{{rankmovie.id}}</th>
      <td>{{ rankmovie.title }}</td>
      <td>{{ rankmovie.rank }}</td>
      <td>{{ rankmovie.content }}</td>
  </tr>
</template>

<script>
export default {
  name : 'RankeMovieList',
  props : {
    rankmovie : {
      type : Object
    }
  }
  

}
</script>

<style scoped>
th {
  color : white;
  font-size : 1.2rem
}
td {
  color : white;
  font-size : 1.2rem
}

</style>