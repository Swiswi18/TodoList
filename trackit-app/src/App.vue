<template>
  <div id="app" class="min-h-screen bg-background text-text transition-colors duration-300">
    
    <router-view />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

import { useStore } from '@/store';
import { supabase } from '@/supabase/client';

const router = useRouter();
const store = useStore();

onMounted(() => {
  // Setup auth listener
  supabase.auth.onAuthStateChange((event, session) => {
    if (event === 'SIGNED_IN' && session) {
      store.setUser(session.user);
      store.loadUserPreferences();
    } else if (event === 'SIGNED_OUT') {
      store.clearUser();
      router.push('/');
    }
  });
  
  // Check for existing session
  const checkSession = async () => {
    const { data } = await supabase.auth.getSession();
    if (data.session) {
      store.setUser(data.session.user);
      store.loadUserPreferences();
    }
  };
  
  checkSession();
});
</script>

<style>
@import './styles//index.css';
@import './styles/themes.css';
</style>
