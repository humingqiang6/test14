<template>
  <div>
    <button @click="incrementCount">
      Clicked {{ count }} times
    </button>
  </div>
</template>

<script>
export default {
  name: 'MyButtonComponent',
  data() {
    return {
      count: 0,
    };
  },
  methods: {
    incrementCount() {
      this.count++;
    },
  },
};
</script>

<style scoped>
button {
  padding: 10px 20px;
  font-size: 16px;
}
</style>