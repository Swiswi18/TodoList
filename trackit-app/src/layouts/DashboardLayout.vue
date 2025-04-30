<template>
  <div class="dashboard-layout flex h-screen bg-background">
    <Sidebar />
    
    <div class="flex-1 flex flex-col overflow-hidden">
      <Navbar />
      
      <main class="flex-1 overflow-y-auto p-6">
        <router-view />
      </main>
    </div>
    
    <ToDoPane v-if="isToDoOpen" />
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from '@/store';
import Sidebar from '@/components/Sidebar.vue';
import Navbar from '@/components/Navbar.vue';
import ToDoPane from '@/components/ToDoPane.vue';

const store = useStore();
const isToDoOpen = computed(() => store.isToDoOpen);
</script>
