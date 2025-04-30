<template>
  <div class="matrix-page">
    <div class="mb-6 flex justify-between items-center">
      <h1 class="text-2xl font-bold text-gray-800 dark:text-white">Priority Matrix</h1>
      <button @click="showTaskForm = true" class="btn-primary">
        <span class="mr-1">+</span> New Task
      </button>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <!-- Urgent & Important -->
      <div class="matrix-quadrant bg-red-50 dark:bg-red-900/20 p-4 rounded-lg border border-red-200 dark:border-red-800">
        <h2 class="text-lg font-semibold mb-3 text-red-700 dark:text-red-400">Urgent & Important</h2>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Do these tasks immediately</p>
        
        <div class="space-y-2">
          <div 
            v-for="task in getQuadrantTasks('urgent-important')" 
            :key="task.id"
            class="task-item bg-white dark:bg-gray-800 p-3 rounded shadow-sm"
          >
            <div class="flex justify-between">
              <h3 class="font-medium text-gray-800 dark:text-white">{{ task.title }}</h3>
              <div class="task-actions">
                <button @click="editTask(task)" class="text-blue-500 hover:text-blue-700 mr-2">✏️</button>
                <button @click="deleteTask(task.id)" class="text-red-500 hover:text-red-700">×</button>
              </div>
            </div>
            <p class="text-sm text-gray-600 dark:text-gray-400">{{ task.description }}</p>
            <div class="mt-2 text-xs text-gray-500 dark:text-gray-400">
              Due: {{ formatDate(task.due_date) }}
            </div>
          </div>
          
          <div
            class="dropzone h-16 border-2 border-dashed border-red-200 dark:border-red-800/50 rounded flex items-center justify-center"
            @dragover.prevent
            @drop="onDrop($event, 'urgent-important')"
          >
            <p class="text-gray-400 text-sm">Drop task here</p>
          </div>
        </div>
      </div>
      
      <!-- Not Urgent & Important -->
      <div class="matrix-quadrant bg-blue-50 dark:bg-blue-900/20 p-4 rounded-lg border border-blue-200 dark:border-blue-800">
        <h2 class="text-lg font-semibold mb-3 text-blue-700 dark:text-blue-400">Important, Not Urgent</h2>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Schedule time for these tasks</p>
        
        <div class="space-y-2">
          <div 
            v-for="task in getQuadrantTasks('important-not-urgent')" 
            :key="task.id"
            class="task-item bg-white dark:bg-gray-800 p-3 rounded shadow-sm"
          >
            <div class="flex justify-between">
              <h3 class="font-medium text-gray-800 dark:text-white">{{ task.title }}</h3>
              <div class="task-actions">
                <button @click="editTask(task)" class="text-blue-500 hover:text-blue-700 mr-2">✏️</button>
                <button @click="deleteTask(task.id)" class="text-red-500 hover:text-red-700">×</button>
              </div>
            </div>
            <p class="text-sm text-gray-600 dark:text-gray-400">{{ task.description }}</p>
            <div class="mt-2 text-xs text-gray-500 dark:text-gray-400">
              Due: {{ formatDate(task.due_date) }}
            </div>
          </div>
          
          <div
            class="dropzone h-16 border-2 border-dashed border-blue-200 dark:border-blue-800/50 rounded flex items-center justify-center"
            @dragover.prevent
            @drop="onDrop($event, 'important-not-urgent')"
          >
            <p class="text-gray-400 text-sm">Drop task here</p>
          </div>
        </div>
      </div>
      
      <!-- Urgent & Not Important -->
      <div class="matrix-quadrant bg-yellow-50 dark:bg-yellow-900/20 p-4 rounded-lg border border-yellow-200 dark:border-yellow-800">
        <h2 class="text-lg font-semibold mb-3 text-yellow-700 dark:text-yellow-400">Urgent, Not Important</h2>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Delegate these if possible</p>
        
        <div class="space-y-2">
          <div 
            v-for="task in getQuadrantTasks('urgent-not-important')" 
            :key="task.id"
            class="task-item bg-white dark:bg-gray-800 p-3 rounded shadow-sm"
          >
            <div class="flex justify-between">
              <h3 class="font-medium text-gray-800 dark:text-white">{{ task.title }}</h3>
              <div class="task-actions">
                <button @click="editTask(task)" class="text-blue-500 hover:text-blue-700 mr-2">✏️</button>
                <button @click="deleteTask(task.id)" class="text-red-500 hover:text-red-700">×</button>
              </div>
            </div>
            <p class="text-sm text-gray-600 dark:text-gray-400">{{ task.description }}</p>
            <div class="mt-2 text-xs text-gray-500 dark:text-gray-400">
              Due: {{ formatDate(task.due_date) }}
            </div>
          </div>
          
          <div
            class="dropzone h-16 border-2 border-dashed border-yellow-200 dark:border-yellow-800/50 rounded flex items-center justify-center"
            @dragover.prevent
            @drop="onDrop($event, 'urgent-not-important')"
          >
            <p class="text-gray-400 text-sm">Drop task here</p>
          </div>
        </div>
      </div>
      
      <!-- Not Urgent & Not Important -->
      <div class="matrix-quadrant bg-gray-50 dark:bg-gray-900/20 p-4 rounded-lg border border-gray-200 dark:border-gray-700">
        <h2 class="text-lg font-semibold mb-3 text-gray-700 dark:text-gray-400">Not Urgent & Not Important</h2>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Eliminate these if possible</p>
        
        <div class="space-y-2">
          <div 
            v-for="task in getQuadrantTasks('not-urgent-not-important')" 
            :key="task.id"
            class="task-item bg-white dark:bg-gray-800 p-3 rounded shadow-sm"
          >
            <div class="flex justify-between">
              <h3 class="font-medium text-gray-800 dark:text-white">{{ task.title }}</h3>
              <div class="task-actions">
                <button @click="editTask(task)" class="text-blue-500 hover:text-blue-700 mr-2">✏️</button>
                <button @click="deleteTask(task.id)" class="text-red-500 hover:text-red-700">×</button>
              </div>
            </div>
            <p class="text-sm text-gray-600 dark:text-gray-400">{{ task.description }}</p>
            <div class="mt-2 text-xs text-gray-500 dark:text-gray-400">
              Due: {{ formatDate(task.due_date) }}
            </div>
          </div>
          
          <div
            class="dropzone h-16 border-2 border-dashed border-gray-200 dark:border-gray-700/50 rounded flex items-center justify-center"
            @dragover.prevent
            @drop="onDrop($event, 'not-urgent-not-important')"
          >
            <p class="text-gray-400 text-sm">Drop task here</p>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Task Modal Form would go here -->
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useStore } from '@/store';

const store = useStore();
const tasks = ref([]);
const showTaskForm = ref(false);
const currentTask = ref(null);
let draggedTask = null;

onMounted(() => {
  loadTasks();
});

const loadTasks = async () => {
  // Mock data for demonstration
  tasks.value = [
    { id: 1, title: 'Fix critical bug', description: 'Production issue affecting users', quadrant: 'urgent-important', due_date: '2023-12-10' },
    { id: 2, title: 'Strategic planning', description: 'Q1 planning session', quadrant: 'important-not-urgent', due_date: '2024-01-15' },
    { id: 3, title: 'Respond to emails', description: 'Clear inbox backlog', quadrant: 'urgent-not-important', due_date: '2023-12-12' },
    { id: 4, title: 'Social media browsing', description: 'Check Twitter for industry news', quadrant: 'not-urgent-not-important', due_date: null },
  ];
};

const getQuadrantTasks = (quadrant) => {
  return tasks.value.filter(task => task.quadrant === quadrant);
};

const formatDate = (dateStr) => {
  if (!dateStr) return 'No due date';
  return new Date(dateStr).toLocaleDateString();
};

const onDrop = (event, quadrant) => {
  if (draggedTask) {
    // Update task quadrant
    const taskIndex = tasks.value.findIndex(t => t.id === draggedTask.id);
    if (taskIndex !== -1) {
      tasks.value[taskIndex] = { ...tasks.value[taskIndex], quadrant };
      // In a real app, save to Supabase here
    }
    draggedTask = null;
  }
};

const editTask = (task) => {
  currentTask.value = task;
  showTaskForm.value = true;
};

const deleteTask = (taskId) => {
  if (confirm('Are you sure you want to delete this task?')) {
    tasks.value = tasks.value.filter(t => t.id !== taskId);
    // In a real app, delete from Supabase here
  }
};
</script>
