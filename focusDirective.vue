<template>
  <div>
    <input v-focus type="text" placeholder="This input should be focused on mount" />
  </div>
</template>

<script>
export default {
  name: 'FocusDirectiveExample',
  directives: {
    focus: {
      mounted(el) {
        el.focus();
      }
    }
  }
}
</script>

<style scoped>
input {
  padding: 10px;
  font-size: 16px;
}
</style>