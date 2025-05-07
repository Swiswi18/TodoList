<template>
  <div>
    <!-- Button to open modal -->
    <button @click="showProjectForm = true" class="btn-primary">
      New Project
    </button>
    
    <!-- Project Form Modal -->
    <div v-if="showProjectForm" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <ProjectForm 
        :project="editingProject"
        @submitted="handleProjectSubmitted"
        @cancel="closeProjectForm"
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
import { ref, onMounted, computed } from 'vue';
import ProjectCard from '../components/ProjectCard.vue';
import ProjectForm from '@/components/ProjectForm.vue';
import { supabase } from '../supabase/client';

const showProjectForm = ref(false);
const editingProject = ref(null);
const projects = ref([]);

// Load projects
const loadProjects = async () => {
  const { data, error } = await supabase
    .from('projects')
    .select('*')
    .order('created_at', { ascending: false });
    
  if (!error) {
    projects.value = data || [];
  }
};

// Open the form for editing
const editProject = (project) => {
  editingProject.value = project;
  showProjectForm.value = true;
};

// Handle project submission (create or update)
const handleProjectSubmitted = (project) => {
  // Refresh the project list
  loadProjects();
  
  // Close the form
  closeProjectForm();
};
const filteredProjects = computed(() => projects.value);

// Close the project form
const closeProjectForm = () => {
  showProjectForm.value = false;
  editingProject.value = null;
};

// Load projects on mount
onMounted(() => {
  loadProjects();
});
</script>
