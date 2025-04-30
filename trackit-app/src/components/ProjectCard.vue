<template>
    <div class="project-card bg-white dark:bg-gray-800 rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow">
      <div class="flex justify-between items-start">
        <div>
          <h3 class="text-lg font-semibold text-gray-800 dark:text-white">{{ project.title }}</h3>
          <p class="text-sm text-gray-600 dark:text-gray-400 mt-1">{{ project.description }}</p>
        </div>
        
        <div class="flex space-x-2">
          <button @click="openEdit" class="text-blue-500 hover:text-blue-700">
            ✏️
          </button>
          <button @click="deleteProject" class="text-red-500 hover:text-red-700">
            🗑️
          </button>
        </div>
      </div>
      
      <div class="mt-4">
        <div class="flex justify-between text-sm">
          <span class="text-gray-600 dark:text-gray-400">Due date: {{ formatDate(project.due_date) }}</span>
          <span :class="statusClass">{{ project.status }}</span>
        </div>
        
        <div class="mt-2 flex justify-between items-center">
          <div class="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2.5">
            <div class="bg-primary h-2.5 rounded-full" :style="{ width: `${project.progress}%` }"></div>
          </div>
          <span class="ml-2 text-xs text-gray-600 dark:text-gray-400">{{ project.progress }}%</span>
        </div>
      </div>
    </div>
  </template>

  <script setup>
  import { computed } from 'vue';

  const props = defineProps({
    project: {
      type: Object,
      required: true
    }
  });

  const emit = defineEmits(['edit', 'delete']);

  const statusClass = computed(() => {
    switch (props.project.status) {
      case 'Completed':
        return 'text-green-500';
      case 'In Progress':
        return 'text-blue-500';
      case 'On Hold':
        return 'text-yellow-500';
      case 'Overdue':
        return 'text-red-500';
      default:
        return 'text-gray-500';
    }
  });

  const formatDate = (date) => {
    if (!date) return 'No due date';
    return new Date(date).toLocaleDateString();
  };

  const openEdit = () => {
    emit('edit', props.project);
  };

  const deleteProject = () => {
    if (confirm(`Are you sure you want to delete ${props.project.title }?`)) {
      emit('delete', props.project.id);
    }
  };
  </script>
  