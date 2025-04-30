<template>
  <div class="sidebar h-screen bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-white" :class="{ 'w-64': !collapsed, 'w-16': collapsed }">
    <div class="p-4 flex justify-between items-center">
      <div v-if="!collapsed" class="text-xl font-bold">TrackIt 2.0</div>
      <button @click="toggleSidebar" class="p-1 rounded hover:bg-gray-200 dark:hover:bg-gray-800">
        <span v-if="collapsed">»</span>
        <span v-else>«</span>
      </button>
    </div>
    
    <nav class="mt-4">
      <router-link 
        v-for="(link, index) in navLinks" 
        :key="index"
        :to="link.to"
        class="flex items-center p-4 hover:bg-gray-200 dark:hover:bg-gray-800"
      >
        <span class="icon">{{ link.icon }}</span>
        <span v-if="!collapsed" class="ml-3">{{ link.text }}</span>
      </router-link>
    </nav>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const collapsed = ref(false);
const navLinks = [
  { icon: '📊', text: 'Projects', to: '/dashboard/projects' },
  { icon: '📋', text: 'Scrum Board', to: '/dashboard/scrum' },
  { icon: '🎯', text: 'Priority Matrix', to: '/dashboard/matrix' },
  { icon: '📜', text: 'History', to: '/dashboard/history' },
  { icon: '👤', text: 'Profile', to: '/dashboard/profile' }
];

const toggleSidebar = () => {
  collapsed.value = !collapsed.value;
};
</script>
