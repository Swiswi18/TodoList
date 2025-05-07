<template>
  <form @submit.prevent="handleSubmit" class="p-6 bg-white dark:bg-gray-900 rounded-lg shadow-md w-full max-w-xl mx-auto space-y-4">
    <h2 class="text-2xl font-semibold text-gray-800 dark:text-white">{{ isEditing ? 'Edit Project' : 'New Project' }}</h2>
    
    <!-- Error message display -->
    <div v-if="errorMessage" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative dark:bg-red-900 dark:text-red-300 dark:border-red-600">
      {{ errorMessage }}
    </div>
    
    <div>
      <label class="block text-sm text-gray-700 dark:text-gray-200">Title</label>
      <input v-model="form.title" type="text" required class="input" />
    </div>
    <div>
      <label class="block text-sm text-gray-700 dark:text-gray-200">Description</label>
      <textarea v-model="form.description" rows="3" class="input"></textarea>
    </div>
    <div>
      <label class="block text-sm text-gray-700 dark:text-gray-200">Due Date</label>
      <input v-model="form.due_date" type="date" class="input" />
    </div>
    <div>
      <label class="block text-sm text-gray-700 dark:text-gray-200">Tier</label>
      <select v-model="form.tier" class="input">
        <option value="1">Tier 1</option>
        <option value="2">Tier 2</option>
        <option value="3">Tier 3</option>
      </select>
    </div>
    <div>
      <label class="block text-sm text-gray-700 dark:text-gray-200">GitHub Link</label>
      <input v-model="form.git_link" type="url" placeholder="https://github.com/..." class="input" />
    </div>
    <div>
      <label class="block text-sm text-gray-700 dark:text-gray-200">Tech Stack (comma-separated)</label>
      <input v-model="form.tech_stack" type="text" placeholder="Vue, Supabase, Tailwind" class="input" />
    </div>
    <div class="flex justify-end gap-4">
      <button type="button" @click="$emit('cancel')" class="px-4 py-2 rounded bg-gray-200 dark:bg-gray-700 text-sm">
        Cancel
      </button>
      <button 
        type="submit" 
        class="px-4 py-2 rounded bg-purple-600 text-white hover:bg-purple-700 text-sm"
        :disabled="isSubmitting"
      >
        {{ isSubmitting ? 'Processing...' : (isEditing ? 'Update' : 'Create') }}
      </button>
    </div>
  </form>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { supabase } from '../supabase/client'; // Adjust if your supabase client path is different

const props = defineProps({
  project: { type: Object, default: () => null }
});

const emit = defineEmits(['submitted', 'cancel']);

// Get user from session instead of helper
const user = ref(null);
const isSubmitting = ref(false);
const errorMessage = ref('');

// Get current user
onMounted(async () => {
  const { data } = await supabase.auth.getSession();
  if (data.session) {
    user.value = data.session.user;
  }
});

const isEditing = computed(() => !!props.project);

const form = ref({
  title: '',
  description: '',
  due_date: '',
  tier: 1,
  git_link: '',
  tech_stack: ''
});

// Initialize form with project data if editing
onMounted(() => {
  if (props.project) {
    form.value = {
      title: props.project.title || '',
      description: props.project.description || '',
      due_date: props.project.due_date || '',
      tier: props.project.tier || 1,
      git_link: props.project.git_link || '',
      // Convert array back to comma-separated string if needed
      tech_stack: Array.isArray(props.project.tech_stack) 
        ? props.project.tech_stack.join(', ') 
        : props.project.tech_stack || ''
    };
  }
});

const handleSubmit = async () => {
  if (!user.value) {
    errorMessage.value = 'You must be logged in to create/edit a project';
    return;
  }

  try {
    isSubmitting.value = true;
    errorMessage.value = '';
    
    // Prepare data payload
    const payload = {
      title: form.value.title,
      description: form.value.description,
      due_date: form.value.due_date || null,
      tier: parseInt(form.value.tier, 10),
      git_link: form.value.git_link || null,
      // Convert comma-separated string to array, handle nulls
      tech_stack: form.value.tech_stack ? form.value.tech_stack.split(',').map(t => t.trim()) : []
    };
    
    // Only add user_id for new projects
    if (!isEditing.value) {
      payload.user_id = user.value.id;
      payload.status = 'active'; // Set default status
    }
    
    let result;
    
    if (isEditing.value) {
      // Update existing project
      const { data, error } = await supabase
        .from('projects')
        .update(payload)
        .eq('id', props.project.id)
        .select();
        
      if (error) throw error;
      result = { data, error };
      
    } else {
      // Insert new project
      const { data, error } = await supabase
        .from('projects')
        .insert(payload)
        .select();
        
      if (error) throw error;
      result = { data, error };
    }
    
    // Handle result
    if (result.error) {
      throw result.error;
    }
    
    // On success, emit the submitted event with the data
    emit('submitted', result.data?.[0] || {});
    
  } catch (error) {
    console.error('Error submitting project:', error);
    errorMessage.value = error.message || 'Failed to save project. Please try again.';
  } finally {
    isSubmitting.value = false;
  }
};
</script>

