<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 w-full max-w-md">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-xl font-bold text-gray-800 dark:text-white">
          {{ isEditing ? 'Edit Project' : 'Create New Project' }}
        </h2>
        <button @click="closeModal" class="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200">
          &times;
        </button>
      </div>
      
      <form @submit.prevent="submitForm">
        <div class="mb-4">
          <label for="title" class="block text-gray-700 dark:text-gray-300 mb-1">Project Name</label>
          <input 
            id="name"
            v-model="form.title"
            type="text"
            class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
            required
          />
        </div>
        
        <div class="mb-4">
          <label for="description" class="block text-gray-700 dark:text-gray-300 mb-1">Description</label>
          <textarea 
            id="description"
            v-model="form.description"
            class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
            rows="3"
          ></textarea>
        </div>
        
        <div class="mb-4">
          <label for="due_date" class="block text-gray-700 dark:text-gray-300 mb-1">Due Date</label>
          <input 
            id="due_date"
            v-model="form.due_date"
            type="date"
            class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
          />
        </div>
        
        <div class="mb-4">
          <label for="status" class="block text-gray-700 dark:text-gray-300 mb-1">Status</label>
          <select 
            id="status"
            v-model="form.status"
            class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
          >
            <option value="Not Started">Not Started</option>
            <option value="In Progress">In Progress</option>
            <option value="On Hold">On Hold</option>
            <option value="Completed">Completed</option>
          </select>
        </div>
        
        <div class="mb-4">
          <label for="progress" class="block text-gray-700 dark:text-gray-300 mb-1">
            Progress: {{ form.progress }}%
          </label>
          <input 
            id="progress"
            v-model="form.progress"
            type="range"
            min="0"
            max="100"
            class="w-full"
          />
        </div>
        
        <div class="flex justify-end space-x-2">
          <button 
            type="button"
            @click="closeModal"
            class="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
          >
            Cancel
          </button>
          <button 
            type="submit"
            class="px-4 py-2 bg-primary text-white rounded hover:bg-secondary"
          >
            {{ isEditing ? 'Update' : 'Create' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

const props = defineProps({
  project: {
    type: Object,
    default: null
  }
});

const emit = defineEmits(['close', 'save']);

const form = ref({
  title: '',            // Changed from 'name' to 'title'
  description: '',
  status: 'active',     // Changed default to match your schema
  due_date: '',
  progress: 0
});

const isEditing = computed(() => !!props.project);

onMounted(() => {
  if (props.project) {
    form.value = { ...props.project };
    // Format date for input
    if (form.value.due_date) {
      const date = new Date(form.value.due_date);
      form.value.due_date = date.toISOString().split('T')[0];
    }
  }
});

const closeModal = () => {
  emit('close');
};

const submitForm = () => {
  emit('save', {
    ...form.value,
    id: props.project?.id
  });
};
</script>
