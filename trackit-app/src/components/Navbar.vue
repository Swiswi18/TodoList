<template>
  <div class="navbar flex justify-between items-center bg-white dark:bg-gray-800 shadow-sm p-4">
    <div class="flex items-center">
      <h1 class="text-xl font-bold text-gray-800 dark:text-white">{{ currentPage }}</h1>
    </div>
    
    <div class="flex items-center space-x-4">
      <button @click="toggleTodo" class="p-2 rounded-md hover:bg-gray-200 dark:hover:bg-gray-700">
        <span class="text-xl">📝</span>
      </button>
      
      <div class="relative">
        <button @click="toggleProfileMenu" class="flex items-center space-x-2">
          <div class="w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center">
            {{ userInitials }}
          </div>
          <span class="hidden md:block text-gray-800 dark:text-white">{{ userName }}</span>
        </button>
        
        <div v-if="profileMenuOpen" class="absolute right-0 mt-2 w-48 bg-white dark:bg-gray-800 rounded-md shadow-lg py-1 z-10">
          <router-link to="/dashboard/profile" class="block px-4 py-2 text-gray-800 dark:text-white hover:bg-gray-200 dark:hover:bg-gray-700">
            Profile
          </router-link>
          <button @click="logout" class="block w-full text-left px-4 py-2 text-gray-800 dark:text-white hover:bg-gray-200 dark:hover:bg-gray-700">
            Logout
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useStore } from '@/store';
import { supabase } from '@/supabase/client';

const store = useStore();
const route = useRoute();
const router = useRouter();
const profileMenuOpen = ref(false);

const currentPage = computed(() => {
  const routeName = route.name;
  return routeName ?? 'Dashboard';
});

const userName = computed(() => {
  return store.user?.email ?? 'User';
});

const userInitials = computed(() => {
  if (!store.user) return 'U';
  
  const email = store.user.email;
  if (!email) return 'U';
  
  return email.charAt(0).toUpperCase();
});

const toggleProfileMenu = () => {
  profileMenuOpen.value = !profileMenuOpen.value;
};

const toggleTodo = () => {
  store.toggleToDo();
};

const logout = async () => {
  await supabase.auth.signOut();
  router.push('/');
};
</script>
