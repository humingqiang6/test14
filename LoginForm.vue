<template>
  <div class="login-form-container">
    <form @submit.prevent="onSubmit" class="login-form">
      <h2>Вход</h2>
      <div class="form-group">
        <label for="username">Имя пользователя:</label>
        <input
          type="text"
          id="username"
          v-model="username"
          required
          placeholder="Введите имя пользователя"
        />
      </div>
      <div class="form-group">
        <label for="password">Пароль:</label>
        <input
          type="password"
          id="password"
          v-model="password"
          required
          placeholder="Введите пароль"
        />
      </div>
      <button type="submit" :disabled="!isFormValid">Войти</button>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    };
  },
  computed: {
    isFormValid() {
      // Простая проверка на заполненность полей
      return this.username.trim() !== '' && this.password.trim() !== '';
    }
  },
  methods: {
    onSubmit() {
      // Сброс предыдущей ошибки
      this.errorMessage = '';

      // Здесь должна быть логика аутентификации
      // Пример: вызов API, проверка данных
      console.log('Попытка входа с данными:', { username: this.username, password: this.password });

      // Симуляция проверки
      if (this.username === 'admin' && this.password === 'password') {
        alert('Успешный вход!');
        // Здесь можно выполнить навигацию или установить токен
      } else {
        this.errorMessage = 'Неверное имя пользователя или пароль.';
      }
    }
  }
};
</script>

<style scoped>
.login-form-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 60vh;
}

.login-form {
  background-color: #f9f9f9;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
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

.error-message {
  color: red;
  margin-top: 1rem;
  text-align: center;
}
</style>