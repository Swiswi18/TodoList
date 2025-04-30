<template>
  <div class="theme-selector">
    <h3 class="text-lg font-semibold mb-4 text-gray-800 dark:text-white">Choose Theme</h3>
    
    <div class="mb-6">
      <h4 class="text-md font-medium mb-2 text-gray-700 dark:text-gray-300">Light Themes</h4>
      <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
        <div 
          v-for="theme in lightThemes" 
          :key="theme.name"
          @click="selectTheme(theme.value)"
          class="theme-option p-3 rounded-lg cursor-pointer transition-transform hover:scale-105"
          :class="{ 'ring-2 ring-primary': currentTheme === theme.value }"
          :style="{ backgroundColor: theme.bg, color: theme.text }"
        >
          <div class="text-xs font-medium">{{ theme.name }}</div>
          <div class="w-full h-2 mt-1 rounded-full" :style="{ backgroundColor: theme.accent }"></div>
        </div>
      </div>
    </div>
    
    <div>
      <h4 class="text-md font-medium mb-2 text-gray-700 dark:text-gray-300">Dark Themes</h4>
      <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
        <div 
          v-for="theme in darkThemes" 
          :key="theme.name"
          @click="selectTheme(theme.value)"
          class="theme-option p-3 rounded-lg cursor-pointer transition-transform hover:scale-105"
          :class="{ 'ring-2 ring-primary': currentTheme === theme.value }"
          :style="{ backgroundColor: theme.bg, color: theme.text }"
        >
          <div class="text-xs font-medium">{{ theme.name }}</div>
          <div class="w-full h-2 mt-1 rounded-full" :style="{ backgroundColor: theme.accent }"></div>
        </div>
      </div>
    </div>
    
    <div class="mt-6">
      <h3 class="text-lg font-semibold mb-4 text-gray-800 dark:text-white">Choose Font</h3>
      <div class="grid grid-cols-2 gap-3">
        <div 
          v-for="font in fonts" 
          :key="font.value"
          @click="selectFont(font.value)"
          class="font-option p-3 rounded-lg cursor-pointer border border-gray-200 dark:border-gray-700 transition-colors hover:bg-gray-100 dark:hover:bg-gray-800"
          :class="{ 'ring-2 ring-primary border-0': currentFont === font.value }"
          :style="{ fontFamily: font.value }"
        >
          <div class="text-sm font-medium text-gray-800 dark:text-white">{{ font.name }}</div>
          <div class="text-xs text-gray-600 dark:text-gray-400">Sample text</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from '@/store';

const store = useStore();

const currentTheme = computed(() => store.theme);
const currentFont = computed(() => store.font);

const lightThemes = [
  { name: 'Ocean Breeze', value: 'ocean-breeze', bg: '#f0f9ff', text: '#0f172a', accent: '#38bdf8' },
  { name: 'Sunrise Glow', value: 'sunrise-glow', bg: '#fff7ed', text: '#431407', accent: '#fb923c' },
  { name: 'Minimal Mist', value: 'minimal-mist', bg: '#f8fafc', text: '#0f172a', accent: '#64748b' },
  { name: 'Soft Leaf', value: 'soft-leaf', bg: '#f7fee7', text: '#1a2e05', accent: '#84cc16' },
  { name: 'Neon Day', value: 'neon-day', bg: '#eff6ff', text: '#1e3a8a', accent: '#3b82f6' },
];

const darkThemes = [
  { name: 'Midnight Code', value: 'midnight-code', bg: '#0f172a', text: '#e2e8f0', accent: '#22d3ee' },
  { name: 'Galaxy Grape', value: 'galaxy-grape', bg: '#1a103d', text: '#e9d5ff', accent: '#c084fc' },
  { name: 'Forest Night', value: 'forest-night', bg: '#0d160b', text: '#dcfce7', accent: '#4ade80' },
  { name: 'Cyber Noir', value: 'cyber-noir', bg: '#18181b', text: '#f5f5f5', accent: '#ec4899' },
  { name: 'Solar Void', value: 'solar-void', bg: '#030711', text: '#fef3c7', accent: '#fcd34d' },
];

const fonts = [
  { name: 'Inter', value: 'Inter' },
  { name: 'Roboto', value: 'Roboto' },
  { name: 'Montserrat', value: 'Montserrat' },
  { name: 'Poppins', value: 'Poppins' },
  { name: 'Source Code Pro', value: 'Source Code Pro' },
  { name: 'Playfair Display', value: 'Playfair Display' },
];

const selectTheme = (theme) => {
  store.setTheme(theme);
};

const selectFont = (font) => {
  store.setFont(font);
};
</script>
