<template>
  <div></div>
</template>

<script>
export default {
  name: 'logoutView',
  methods: {
    logout() {
      this.$emit('submit-logout')
    }
  },
  created() {
    this.logout()
  }
}
</script>

<style>

</style>