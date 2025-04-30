<template>
  <div class="login-page min-h-screen flex items-center justify-center bg-background">
    <div class="max-w-md w-full p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
      <div class="text-center mb-6">
        <h1 class="text-3xl font-bold text-gray-800 dark:text-white">Welcome Back</h1>
        <p class="text-gray-600 dark:text-gray-400">Sign in to your TrackIt 2.0 account</p>
      </div>
      
      <form @submit.prevent="handleLogin">
        <div class="space-y-4">
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Email</label>
            <input 
              id="email"
              v-model="email"
              type="email"
              required
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
              placeholder="Enter your email"
            />
          </div>
          
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Password</label>
            <input 
              id="password"
              v-model="password"
              type="password"
              required
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
              placeholder="Enter your password"
            />
          </div>
          
          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <input id="remember-me" type="checkbox" class="h-4 w-4 text-primary" />
              <label for="remember-me" class="ml-2 block text-sm text-gray-700 dark:text-gray-300">
                Remember me
              </label>
            </div>
            
            <a href="#" class="text-sm text-primary hover:text-secondary">
              Forgot password?
            </a>
          </div>
          
          <div v-if="errorMessage" class="text-red-500 text-sm">
            {{ errorMessage }}
          </div>
          
          <button 
            type="submit"
            class="w-full py-2 px-4 bg-primary text-white rounded-md hover:bg-secondary focus:outline-none focus:ring-2 focus:ring-primary focus:ring-opacity-50"
            :disabled="loading"
          >
            {{ loading ? 'Signing in...' : 'Sign In' }}
          </button>
        </div>
      </form>
      
      <div class="mt-6 text-center">
        <p class="text-gray-600 dark:text-gray-400">
          Don't have an account? 
          <router-link to="/register" class="text-primary hover:text-secondary">
            Create one
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { supabase } from '@/supabase/client';

const router = useRouter();
const email = ref('');
const password = ref('');
const loading = ref(false);
const errorMessage = ref('');

const handleLogin = async () => {
  try {
    loading.value = true;
    errorMessage.value = '';
    
    const { data, error } = await supabase.auth.signInWithPassword({
      email: email.value,
      password: password.value
    });
    
    if (error) {
      errorMessage.value = error.message;
      return;
    }
    
    router.push('/dashboard');
    
  } catch (error) {
    errorMessage.value = 'An unexpected error occurred. Please try again.';
    console.error('Login error:', error);
  } finally {
    loading.value = false;
  }
};
</script>
