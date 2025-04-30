<template>
  <div class="dashboard-redirect">
    <!-- This is just a redirect component -->
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

onMounted(() => {
  // Redirect to projects by default
  router.replace('/dashboard/projects');
});
</script>
