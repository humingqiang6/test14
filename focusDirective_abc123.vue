<template>
  <div>
    <h1>Custom Focus Directive Example</h1>
    <input v-focus type="text" placeholder="This input should be focused on mount" />
    <input type="text" placeholder="This input is not focused" />
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

<style>
input {
  display: block;
  margin: 10px 0;
}
</style>