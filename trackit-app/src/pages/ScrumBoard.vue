<template>
  <div class="scrum-board">
    <div class="mb-6 flex justify-between items-center">
      <h1 class="text-2xl font-bold text-gray-800 dark:text-white">Scrum Board</h1>
      <div class="flex space-x-2">
        <button @click="showTaskForm = true" class="btn-primary">
          <span class="mr-1">+</span> New Task
        </button>
      </div>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
      <!-- To Do Column -->
      <div class="board-column bg-white dark:bg-gray-800 rounded-lg shadow p-4">
        <h2 class="text-lg font-semibold mb-4 text-gray-800 dark:text-white">To Do</h2>
        <div class="space-y-3">
          <div 
            v-for="task in getTasks('todo')" 
            :key="task.id"
            class="task-card bg-gray-50 dark:bg-gray-700 p-3 rounded border-l-4 border-gray-400 cursor-move"
            draggable="true"
            @dragstart="dragStart($event, task)"
          >
            <div class="flex justify-between">
              <h3 class="font-medium text-gray-800 dark:text-white">{{ task.title }}</h3>
              <div class="task-actions">
                <button @click="editTask(task)" class="text-blue-500 hover:text-blue-700 mr-2">✏️</button>
                <button @click="deleteTask(task.id)" class="text-red-500 hover:text-red-700">×</button>
              </div>
            </div>
            <p class="text-sm text-gray-600 dark:text-gray-400 mt-1">{{ task.description }}</p>
            <div class="mt-2 flex justify-between text-xs text-gray-500 dark:text-gray-400">
              <span>Due: {{ formatDate(task.due_date) }}</span>
              <span>{{ task.priority }}</span>
            </div>
          </div>
          <div 
            class="dropzone h-24 border-2 border-dashed border-gray-300 dark:border-gray-600 rounded flex items-center justify-center"
            @dragover.prevent
            @drop="onDrop($event, 'todo')"
          >
            <p class="text-gray-400">Drop here</p>
          </div>
        </div>
      </div>
      
      <!-- In Progress Column -->
      <div class="board-column bg-white dark:bg-gray-800 rounded-lg shadow p-4">
        <h2 class="text-lg font-semibold mb-4 text-gray-800 dark:text-white">In Progress</h2>
        <div class="space-y-3">
          <div 
            v-for="task in getTasks('in-progress')" 
            :key="task.id"
            class="task-card bg-gray-50 dark:bg-gray-700 p-3 rounded border-l-4 border-blue-400 cursor-move"
            draggable="true"
            @dragstart="dragStart($event, task)"
          >
            <div class="flex justify-between">
              <h3 class="font-medium text-gray-800 dark:text-white">{{ task.title }}</h3>
              <div class="task-actions">
                <button @click="editTask(task)" class="text-blue-500 hover:text-blue-700 mr-2">✏️</button>
                <button @click="deleteTask(task.id)" class="text-red-500 hover:text-red-700">×</button>
              </div>
            </div>
            <p class="text-sm text-gray-600 dark:text-gray-400 mt-1">{{ task.description }}</p>
            <div class="mt-2 flex justify-between text-xs text-gray-500 dark:text-gray-400">
              <span>Due: {{ formatDate(task.due_date) }}</span>
              <span>{{ task.priority }}</span>
            </div>
          </div>
          <div 
            class="dropzone h-24 border-2 border-dashed border-gray-300 dark:border-gray-600 rounded flex items-center justify-center"
            @dragover.prevent
            @drop="onDrop($event, 'in-progress')"
          >
            <p class="text-gray-400">Drop here</p>
          </div>
        </div>
      </div>
      
      <!-- Review Column -->
      <div class="board-column bg-white dark:bg-gray-800 rounded-lg shadow p-4">
        <h2 class="text-lg font-semibold mb-4 text-gray-800 dark:text-white">Review</h2>
        <div class="space-y-3">
          <div 
            v-for="task in getTasks('review')" 
            :key="task.id"
            class="task-card bg-gray-50 dark:bg-gray-700 p-3 rounded border-l-4 border-yellow-400 cursor-move"
            draggable="true"
            @dragstart="dragStart($event, task)"
          >
            <div class="flex justify-between">
              <h3 class="font-medium text-gray-800 dark:text-white">{{ task.title }}</h3>
              <div class="task-actions">
                <button @click="editTask(task)" class="text-blue-500 hover:text-blue-700 mr-2">✏️</button>
                <button @click="deleteTask(task.id)" class="text-red-500 hover:text-red-700">×</button>
              </div>
            </div>
            <p class="text-sm text-gray-600 dark:text-gray-400 mt-1">{{ task.description }}</p>
            <div class="mt-2 flex justify-between text-xs text-gray-500 dark:text-gray-400">
              <span>Due: {{ formatDate(task.due_date) }}</span>
              <span>{{ task.priority }}</span>
            </div>
          </div>
          <div 
            class="dropzone h-24 border-2 border-dashed border-gray-300 dark:border-gray-600 rounded flex items-center justify-center"
            @dragover.prevent
            @drop="onDrop($event, 'review')"
          >
            <p class="text-gray-400">Drop here</p>
          </div>
        </div>
      </div>
      
      <!-- Done Column -->
      <div class="board-column bg-white dark:bg-gray-800 rounded-lg shadow p-4">
        <h2 class="text-lg font-semibold mb-4 text-gray-800 dark:text-white">Done</h2>
        <div class="space-y-3">
          <div 
            v-for="task in getTasks('done')" 
            :key="task.id"
            class="task-card bg-gray-50 dark:bg-gray-700 p-3 rounded border-l-4 border-green-400 cursor-move"
            draggable="true"
            @dragstart="dragStart($event, task)"
          >
            <div class="flex justify-between">
              <h3 class="font-medium text-gray-800 dark:text-white">{{ task.title }}</h3>
              <div class="task-actions">
                <button @click="editTask(task)" class="text-blue-500 hover:text-blue-700 mr-2">✏️</button>
                <button @click="deleteTask(task.id)" class="text-red-500 hover:text-red-700">×</button>
              </div>
            </div>
            <p class="text-sm text-gray-600 dark:text-gray-400 mt-1">{{ task.description }}</p>
            <div class="mt-2 flex justify-between text-xs text-gray-500 dark:text-gray-400">
              <span>Due: {{ formatDate(task.due_date) }}</span>
              <span>{{ task.priority }}</span>
            </div>
          </div>
          <div 
            class="dropzone h-24 border-2 border-dashed border-gray-300 dark:border-gray-600 rounded flex items-center justify-center"
            @dragover.prevent
            @drop="onDrop($event, 'done')"
          >
            <p class="text-gray-400">Drop here</p>
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
import { supabase } from '@/supabase/client';

const store = useStore();
const tasks = ref([]);
const showTaskForm = ref(false);
const currentTask = ref(null);
let draggedTask = null;

onMounted(() => {
  loadTasks();
});

const loadTasks = async () => {
  // In a real implementation, fetch tasks from Supabase
  // For this template, we'll use mock data
  tasks.value = [
    { id: 1, title: 'Research competitors', description: 'Analyze top 5 competitors', status: 'todo', priority: 'High', due_date: '2023-12-15' },
    { id: 2, title: 'Create wireframes', description: 'Design basic UI mockups', status: 'in-progress', priority: 'Medium', due_date: '2023-12-20' },
    { id: 3, title: 'Implement auth', description: 'Set up Supabase authentication', status: 'review', priority: 'High', due_date: '2023-12-18' },
    { id: 4, title: 'Write documentation', description: 'Create initial project docs', status: 'done', priority: 'Low', due_date: '2023-12-10' },
  ];
};

const getTasks = (status) => {
  return tasks.value.filter(task => task.status === status);
};

const formatDate = (dateStr) => {
  if (!dateStr) return 'No date';
  return new Date(dateStr).toLocaleDateString();
};

const dragStart = (event, task) => {
  draggedTask = task;
  event.dataTransfer.effectAllowed = 'move';
};

const onDrop = (event, status) => {
  if (draggedTask) {
    // Update task status
    const taskIndex = tasks.value.findIndex(t => t.id === draggedTask.id);
    if (taskIndex !== -1) {
      tasks.value[taskIndex] = { ...tasks.value[taskIndex], status };
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
