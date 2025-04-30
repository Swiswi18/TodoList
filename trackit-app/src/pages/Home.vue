<template>
  <div class="home-page min-h-screen font-body text-text bg-background">
    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-primary to-secondary text-white py-24">
      <div class="container mx-auto px-6 text-center">
        <h1 class="text-5xl md:text-7xl font-extrabold mb-6 tracking-tight leading-tight drop-shadow-md">TrackIt 2.0</h1>
        <p class="text-2xl md:text-3xl mb-10 max-w-3xl mx-auto">Your all-in-one productivity toolkit for organizing, prioritizing, and crushing tasks.</p>
        <div class="flex flex-col md:flex-row justify-center gap-4">
          <router-link to="/register" class="btn-primary text-lg py-3 px-8 rounded-xl shadow-md hover:shadow-xl transition-all">Get Started</router-link>
          <router-link to="/login" class="bg-white text-primary py-3 px-8 rounded-xl hover:bg-gray-100 transition-all text-lg font-semibold shadow-md">Login</router-link>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="py-20 bg-background">
      <div class="container mx-auto px-6">
        <h2 class="text-4xl font-bold text-center mb-14 text-text tracking-tight">Powerful Features to Supercharge Your Workflow</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
          <!-- Feature -->
          <div class="bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-lg hover:shadow-xl transition duration-300">
            <div class="text-5xl mb-6 text-primary">📋</div>
            <h3 class="text-2xl font-semibold mb-3">Scrum Board</h3>
            <p class="text-gray-600 dark:text-gray-400">Customize your Kanban workflow and visually track progress like a pro.</p>
          </div>

          <div class="bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-lg hover:shadow-xl transition duration-300">
            <div class="text-5xl mb-6 text-primary">🎯</div>
            <h3 class="text-2xl font-semibold mb-3">Priority Matrix</h3>
            <p class="text-gray-600 dark:text-gray-400">Prioritize with the Eisenhower Matrix and get the most important things done.</p>
          </div>

          <div class="bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-lg hover:shadow-xl transition duration-300">
            <div class="text-5xl mb-6 text-primary">📝</div>
            <h3 class="text-2xl font-semibold mb-3">Quick To-Dos</h3>
            <p class="text-gray-600 dark:text-gray-400">Capture tasks instantly with lightweight, accessible to-do lists.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 bg-gray-100 dark:bg-gray-900">
      <div class="container mx-auto px-6 text-center">
        <h2 class="text-4xl font-bold mb-6 text-text">Ready to boost your productivity?</h2>
        <p class="text-xl mb-10 text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">Join thousands of professionals and teams who organize their tasks with TrackIt 2.0</p>
        <router-link to="/register" class="btn-primary text-lg py-3 px-8 rounded-xl shadow-md hover:shadow-lg transition-all">Get Started for Free</router-link>
      </div>
    </section>

    <!-- Footer -->
    <footer class="py-10 bg-gray-800 text-white">
      <div class="container mx-auto px-6 text-center text-sm">
        <p>&copy; 2025 TrackIt 2.0. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
// Home page component
</script>
