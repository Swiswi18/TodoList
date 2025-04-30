<template>
  <div class="history-page">
    <div class="mb-6 flex justify-between items-center">
      <h1 class="text-2xl font-bold text-gray-800 dark:text-white">Project History</h1>
      <div class="flex space-x-2">
        <button class="btn-secondary">
          <span class="mr-1">📥</span> Export
        </button>
      </div>
    </div>
    
    <div v-if="loading" class="text-center py-8">
      <p class="text-gray-600 dark:text-gray-400">Loading project history...</p>
    </div>
    
    <div v-else-if="completedProjects.length === 0" class="text-center py-8 bg-white dark:bg-gray-800 rounded-lg p-6">
      <p class="text-xl text-gray-600 dark:text-gray-400 mb-4">No completed projects found</p>
      <p class="text-gray-500 dark:text-gray-400">Your completed and archived projects will appear here</p>
    </div>
    
    <div v-else>
      <!-- Filter and Search -->
      <div class="mb-4 flex flex-col md:flex-row justify-between gap-4">
        <div class="flex">
          <select 
            v-model="filterType"
            class="mr-2 border border-gray-300 dark:border-gray-600 rounded p-2 dark:bg-gray-700 dark:text-white"
          >
            <option value="all">All</option>
            <option value="completed">Completed</option>
            <option value="archived">Archived</option>
          </select>
          
          <select 
            v-model="sortBy"
            class="border border-gray-300 dark:border-gray-600 rounded p-2 dark:bg-gray-700 dark:text-white"
          >
            <option value="recent">Most Recent</option>
            <option value="oldest">Oldest First</option>
            <option value="name">Name (A-Z)</option>
          </select>
        </div>
        
        <div>
          <input 
            v-model="searchQuery"
            type="text"
            placeholder="Search history..."
            class="w-full md:w-64 p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
          />
        </div>
      </div>
      
      <!-- Project History List -->
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow overflow-hidden">
        <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
          <thead class="bg-gray-50 dark:bg-gray-900">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                Project Name
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                Status
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                Completion Date
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                Actions
              </th>
            </tr>
          </thead>
          <tbody class="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">
            <tr v-for="project in filteredProjects" :key="project.id">
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm font-medium text-gray-900 dark:text-white">{{ project.name }}</div>
                <div class="text-sm text-gray-500 dark:text-gray-400">{{ project.description }}</div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span 
                  class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full"
                  :class="getStatusClass(project.status)"
                >
                  {{ project.status }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">
                {{ formatDate(project.completed_at) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                <button @click="restoreProject(project)" class="text-indigo-600 hover:text-indigo-900 dark:text-indigo-400 dark:hover:text-indigo-300 mr-3">
                  Restore
                </button>
                <button @click="deleteProject(project.id)" class="text-red-600 hover:text-red-900 dark:text-red-400 dark:hover:text-red-300">
                  Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useStore } from '@/store';
import { supabase } from '@/supabase/client';

const store = useStore();
const completedProjects = ref([]);
const loading = ref(true);
const filterType = ref('all');
const sortBy = ref('recent');
const searchQuery = ref('');

onMounted(async () => {
  await loadCompletedProjects();
});

const loadCompletedProjects = async () => {
  try {
    loading.value = true;
    
    // In a real implementation, fetch from Supabase
    // For this template we'll use mock data
    completedProjects.value = [
      { id: 1, name: 'Website Redesign', description: 'Company website update', status: 'Completed', completed_at: '2023-11-20' },
      { id: 2, name: 'Marketing Campaign', description: 'Q4 social media campaign', status: 'Archived', completed_at: '2023-10-15' },
      { id: 3, name: 'Product Launch', description: 'New feature release', status: 'Completed', completed_at: '2023-09-30' },
    ];
  } catch (error) {
    console.error('Error loading completed projects:', error);
  } finally {
    loading.value = false;
  }
};

const filteredProjects = computed(() => {
  let filtered = [...completedProjects.value];
  
  // Filter by type
  if (filterType.value !== 'all') {
    filtered = filtered.filter(p => p.status.toLowerCase() === filterType.value);
  }
  
  // Search filter
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase();
    filtered = filtered.filter(p => 
      p.name.toLowerCase().includes(query) || 
      p.description.toLowerCase().includes(query)
    );
  }
  
  // Sort
  if (sortBy.value === 'recent') {
    filtered.sort((a, b) => new Date(b.completed_at) - new Date(a.completed_at));
  } else if (sortBy.value === 'oldest') {
    filtered.sort((a, b) => new Date(a.completed_at) - new Date(b.completed_at));
  } else if (sortBy.value === 'name') {
    filtered.sort((a, b) => a.name.localeCompare(b.name));
  }
  
  return filtered;
});

const formatDate = (dateStr) => {
  if (!dateStr) return 'Unknown';
  return new Date(dateStr).toLocaleDateString();
};

const getStatusClass = (status) => {
  if (status === 'Completed') {
    return 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300';
  } else if (status === 'Archived') {
    return 'bg-gray-100 text-gray-800 dark:bg-gray-900 dark:text-gray-300';
  }
  return '';
};

const restoreProject = (project) => {
  if (confirm(`Are you sure you want to restore "${project.name}"?`)) {
    // In a real app, update the project status in Supabase
    console.log('Restoring project:', project);
  }
};

const deleteProject = (projectId) => {
  if (confirm('Are you sure you want to permanently delete this project?')) {
    // In a real app, delete from Supabase
    completedProjects.value = completedProjects.value.filter(p => p.id !== projectId);
  }
};
</script>
