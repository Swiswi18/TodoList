<template>
  <div class="projects-page">
    <div class="mb-6 flex justify-between items-center">
      <h1 class="text-2xl font-bold text-gray-800 dark:text-white">My Projects</h1>
      <button @click="showProjectForm = true" class="btn-primary">
        <span class="mr-1">+</span> New Project
      </button>
    </div>
    
    <div class="mb-4">
      <input 
        v-model="searchQuery"
        type="text"
        placeholder="Search projects..."
        class="w-full md:w-64 p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
      />
    </div>
    
    <div v-if="loading" class="text-center py-8">
      <p class="text-gray-600 dark:text-gray-400">Loading projects...</p>
    </div>
    
    <div v-else-if="filteredProjects.length === 0" class="text-center py-8 bg-white dark:bg-gray-800 rounded-lg p-6">
      <p class="text-xl text-gray-600 dark:text-gray-400 mb-4">No projects found</p>
      <button @click="showProjectForm = true" class="btn-primary">Create your first project</button>
    </div>
    
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <ProjectCard 
        v-for="project in filteredProjects" 
        :key="project.id" 
        :project="project"
        @edit="editProject"
        @delete="deleteProject"
      />
    </div>
    
    <!-- Project Form Modal -->
    <ProjectForm 
      v-if="showProjectForm"
      :project="currentProject"
      @close="closeProjectForm"
      @save="saveProject"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useStore } from '@/store';
import { supabase } from '@/supabase/client';
import ProjectCard from '@/components/ProjectCard.vue';
import ProjectForm from '@/components/ProjectForm.vue';

const store = useStore();
const projects = ref([]);
const loading = ref(true);
const searchQuery = ref('');
const showProjectForm = ref(false);
const currentProject = ref(null);

onMounted(async () => {
  await loadProjects();
});

const loadProjects = async () => {
  try {
    loading.value = true;
    
    // In a real implementation, you'd use store.loadProjects()
    const { data, error } = await supabase
      .from('projects')
      .select('*')
      .eq('user_id', store.user?.id)
      .order('created_at', { ascending: false });
    
    if (error) throw error;
    
    projects.value = data || [];
  } catch (error) {
    console.error('Error loading projects:', error);
  } finally {
    loading.value = false;
  }
};

const filteredProjects = computed(() => {
  if (!searchQuery.value) return projects.value;
  
  const query = searchQuery.value.toLowerCase();
  return projects.value.filter(project => 
    project.name.toLowerCase().includes(query) ||
    project.description.toLowerCase().includes(query)
  );
});

const editProject = (project) => {
  currentProject.value = project;
  showProjectForm.value = true;
};

const closeProjectForm = () => {
  showProjectForm.value = false;
  currentProject.value = null;
};

const saveProject = async (projectData) => {
  try {
    if (projectData.id) {
      // Update existing project
      const { error } = await supabase
        .from('projects')
        .update({
          title: projectData.title,         // Changed from 'name' to 'title'
          description: projectData.description,
          due_date: projectData.due_date,
          status: 'active',                 // Fixed to match your schema
          // no progress field in your schema
        })
        .eq('id', projectData.id);
      
      if (error) throw error;
      
      // Update local state...
    } else {
      // Create new project
      const { data, error } = await supabase
        .from('projects')
        .insert({
          user_id: store.user.id,
          title: projectData.title,         // Changed from 'name' to 'title'
          description: projectData.description,
          due_date: projectData.due_date,
          status: 'active',                 // Fixed to match your schema
          // no progress field in your schema
        })
        .select();
      
      if (error) throw error;
      
      // Add to local state
      if (data && data.length > 0) {
        projects.value.unshift(data[0]);
      }
    }
    
    // Close the form
    closeProjectForm();
  } catch (error) {
    console.error('Error saving project:', error);
    alert('Failed to save project. Please try again.');
  }
};

const deleteProject = async (projectId) => {
  try {
    const { error } = await supabase
      .from('projects')
      .delete()
      .eq('id', projectId);
    
    if (error) throw error;
    
    // Remove from local state
    projects.value = projects.value.filter(p => p.id !== projectId);
  } catch (error) {
    console.error('Error deleting project:', error);
    alert('Failed to delete project. Please try again.');
  }
};
</script>
