<template>
  <div class="register-page min-h-screen flex items-center justify-center bg-background">
    <div class="max-w-md w-full p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
      <div class="text-center mb-6">
        <h1 class="text-3xl font-bold text-gray-800 dark:text-white">Create Account</h1>
        <p class="text-gray-600 dark:text-gray-400">Join TrackIt 2.0 to boost your productivity</p>
      </div>
      
      <form @submit.prevent="handleRegister">
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
              placeholder="Create a password"
            />
            <p class="text-xs text-gray-500 mt-1">Password must be at least 6 characters long</p>
          </div>
          
          <div>
            <label for="confirm-password" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Confirm Password</label>
            <input 
              id="confirm-password"
              v-model="confirmPassword"
              type="password"
              required
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
              placeholder="Confirm your password"
            />
          </div>
          
          <div class="flex items-center">
            <input id="terms" type="checkbox" v-model="agreeToTerms" class="h-4 w-4 text-primary" required />
            <label for="terms" class="ml-2 block text-sm text-gray-700 dark:text-gray-300">
              I agree to the 
              <a href="#" class="text-primary hover:text-secondary">Terms of Service</a>
              and
              <a href="#" class="text-primary hover:text-secondary">Privacy Policy</a>
            </label>
          </div>
          
          <div v-if="errorMessage" class="text-red-500 text-sm">
            {{ errorMessage }}
          </div>
          
          <button 
            type="submit"
            class="w-full py-2 px-4 bg-primary text-white rounded-md hover:bg-secondary focus:outline-none focus:ring-2 focus:ring-primary focus:ring-opacity-50"
            :disabled="loading || !agreeToTerms || password !== confirmPassword"
          >
            {{ loading ? 'Creating Account...' : 'Create Account' }}
          </button>
        </div>
      </form>
      
      <div class="mt-6 text-center">
        <p class="text-gray-600 dark:text-gray-400">
          Already have an account? 
          <router-link to="/login" class="text-primary hover:text-secondary">
            Sign in
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import { supabase } from '@/supabase/client';

const router = useRouter();
const email = ref('');
const password = ref('');
const confirmPassword = ref('');
const agreeToTerms = ref(false);
const loading = ref(false);
const errorMessage = ref('');

// Watch for password mismatch
watch([password, confirmPassword], ([newPassword, newConfirmPassword]) => {
  if (newConfirmPassword && newPassword !== newConfirmPassword) {
    errorMessage.value = 'Passwords do not match';
  } else {
    errorMessage.value = '';
  }
});

const handleRegister = async () => {
  if (password.value !== confirmPassword.value) {
    errorMessage.value = 'Passwords do not match';
    return;
  }
  
  if (password.value.length < 6) {
    errorMessage.value = 'Password must be at least 6 characters long';
    return;
  }
  
  try {
    loading.value = true;
    errorMessage.value = '';
    
    const { data, error } = await supabase.auth.signUp({
      email: email.value,
      password: password.value
    });
    
    if (error) {
      errorMessage.value = error.message;
      return;
    }
    
    // Redirect to dashboard or confirmation page
    router.push('/dashboard');
    
  } catch (error) {
    errorMessage.value = 'An unexpected error occurred. Please try again.';
    console.error('Registration error:', error);
  } finally {
    loading.value = false;
  }
};
</script>
