<template>
  <div class="login-container">
    <form @submit.prevent="handleSubmit" class="login-form">
      <h2>Вход</h2>
      <div class="form-group">
        <label for="username">Имя пользователя:</label>
        <input
          type="text"
          id="username"
          v-model="username"
          required
          :class="{ 'error': v$.username.$error }"
        />
        <span v-if="v$.username.$error" class="error-message">
          {{ v$.username.$error }}
        </span>
      </div>
      <div class="form-group">
        <label for="password">Пароль:</label>
        <input
          type="password"
          id="password"
          v-model="password"
          required
          :class="{ 'error': v$.password.$error }"
        />
        <span v-if="v$.password.$error" class="error-message">
          {{ v$.password.$error }}
        </span>
      </div>
      <button type="submit" :disabled="v$.$invalid">Войти</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useVuelidate } from '@vuelidate/core';
import { required, minLength } from '@vuelidate/validators';

const username = ref('');
const password = ref('');

const rules = {
  username: { required },
  password: { required, minLength: minLength(6) }
};

const v$ = useVuelidate(rules, { username, password });

const handleSubmit = () => {
  if (!v$.value.$invalid) {
    console.log('Форма валидна!', { username: username.value, password: password.value });
    // Здесь можно вызвать API для входа
  } else {
    console.log('Форма не валидна!');
    v$.value.$touch(); // Показать ошибки валидации
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f0f0f0;
}

.login-form {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input.error {
  border-color: red;
}

.error-message {
  color: red;
  font-size: 0.8rem;
  margin-top: 0.25rem;
  display: block;
}

button {
  width: 100%;
  padding: 0.75rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}
</style>