<template>
  <div class="flex flex-col items-center p-6 min-h-screen bg-gray-100 dark:bg-gray-900">
    <h1 class="text-2xl font-bold text-gray-800 dark:text-white">SecurePass: Password Strength Checker</h1>
    <input v-model="password" @input="checkPassword" type="password" placeholder="Enter password"
      class="mt-4 p-2 border rounded w-80" />
    <p class="mt-2 text-sm" :class="strengthClass">{{ strengthMessage }}</p>
    <button @click="generatePassword" class="mt-4 px-4 py-2 bg-blue-500 text-white rounded">Generate Strong Password</button>
    <p class="mt-2 text-gray-600 dark:text-gray-300">{{ generatedPassword }}</p>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      password: '',
      strengthMessage: 'Enter a password',
      strengthClass: 'text-gray-500',
      generatedPassword: ''
    };
  },
  methods: {
    async checkPassword() {
      if (this.password.length === 0) {
        this.strengthMessage = 'Enter a password';
        this.strengthClass = 'text-gray-500';
        return;
      }
      try {
        const response = await axios.post('http://localhost:5000/check', { password: this.password });
        this.strengthMessage = response.data.message;
        this.strengthClass = response.data.class;
      } catch (error) {
        console.error('Error checking password:', error);
      }
    },
    async generatePassword() {
      try {
        const response = await axios.get('http://localhost:5000/generate');
        this.generatedPassword = response.data.password;
      } catch (error) {
        console.error('Error generating password:', error);
      }
    }
  }
};
</script>

<style>
.text-red-500 { color: red; }
.text-yellow-500 { color: yellow; }
.text-green-500 { color: green; }
</style>