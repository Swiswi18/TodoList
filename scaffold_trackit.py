#!/usr/bin/env python3
"""
TrackIt 2.0 Project Scaffolder

This script generates a complete project structure for a TrackIt 2.0 application
using Vue 3, Vite, Tailwind CSS, and Supabase.
"""

import os
import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Union


class ProjectScaffolder:
    """Handles the creation of the TrackIt 2.0 project scaffold."""

    def __init__(self, project_path: str = "trackit-app"):
        """
        Initialize the project scaffolder.
        
        Args:
            project_path: The root directory for the project
        """
        self.project_path = Path(project_path)
        self.directories: List[str] = [
            "public",
            "src/assets",
            "src/components",
            "src/layouts",
            "src/pages",
            "src/router",
            "src/store",
            "src/supabase",
            "src/styles",
        ]
        self.files: Dict[str, str] = self._define_files()
        
    def _define_files(self) -> Dict[str, str]:
        """Define the content for all files to be created in the project."""
        return {
            "index.html": self._get_index_html_content(),

            # Config files
            ".env": self._get_env_content(),
            "tailwind.config.js": self._get_tailwind_config_content(),
            "vite.config.js": self._get_vite_config_content(),
            "package.json": self._get_package_json_content(),
            
            # Vue files
            "src/App.vue": self._get_app_vue_content(),
            "src/main.js": self._get_main_js_content(),
            
            # Components
            "src/components/Sidebar.vue": self._get_sidebar_content(),
            "src/components/Navbar.vue": self._get_navbar_content(),
            "src/components/ToDoPane.vue": self._get_todo_pane_content(),
            "src/components/ProjectCard.vue": self._get_project_card_content(),
            "src/components/ProjectForm.vue": self._get_project_form_content(),
            "src/components/ThemeSelector.vue": self._get_theme_selector_content(),
            
            # Layouts
            "src/layouts/DashboardLayout.vue": self._get_dashboard_layout_content(),
            
            # Pages
            "src/pages/Home.vue": self._get_home_content(),
            "src/pages/Login.vue": self._get_login_content(),
            "src/pages/Register.vue": self._get_register_content(),
            "src/pages/Dashboard.vue": self._get_dashboard_content(),
            "src/pages/Projects.vue": self._get_projects_content(),
            "src/pages/ScrumBoard.vue": self._get_scrum_board_content(),
            "src/pages/Matrix.vue": self._get_matrix_content(),
            "src/pages/History.vue": self._get_history_content(),
            "src/pages/Profile.vue": self._get_profile_content(),
            
            # Router
            "src/router/index.js": self._get_router_content(),
            
            # Store
            "src/store/index.js": self._get_store_content(),
            
            # Supabase
            "src/supabase/client.js": self._get_supabase_client_content(),
            
            # Styles
            "src/styles/themes.css": self._get_themes_css_content(),
            "src/styles/tailwind.css": self._get_tailwind_css_content(),
        }
    
    def create_project(self) -> None:
        """Create the entire project structure."""
        print(f"Creating TrackIt 2.0 project at {self.project_path}")
        
        # Create directories
        self._create_directories()
        
        # Create files
        self._create_files()
        
        print(f"Project successfully created at {self.project_path}")
        print("To get started, run:")
        print(f"cd {self.project_path}")
        print("npm install")
        print("npm run dev")
    
    def _create_directories(self) -> None:
        """Create all project directories."""
        for directory in self.directories:
            dir_path = self.project_path / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {dir_path}")
    
    def _create_files(self) -> None:
      """Create all project files with content."""
      for file_path, content in self.files.items():
          full_path = self.project_path / file_path
          full_path.parent.mkdir(parents=True, exist_ok=True)
          
          # Add UTF-8 encoding here
          with open(full_path, 'w', encoding='utf-8') as f:
              f.write(content)
          
          print(f"Created file: {full_path}")

    def _get_index_html_content(self) -> str:
      return """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>TrackIt 2.0</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>
"""
    
    # File content methods
    def _get_env_content(self) -> str:
        return """VITE_SUPABASE_URL=your-supabase-url
VITE_SUPABASE_ANON_KEY=your-supabase-anon-key
"""

    def _get_tailwind_config_content(self) -> str:
        return """/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: 'var(--color-primary)',
        secondary: 'var(--color-secondary)',
        accent: 'var(--color-accent)',
        background: 'var(--color-background)',
        text: 'var(--color-text)',
      },
      fontFamily: {
        sans: ['var(--font-body)', 'sans-serif'],
        heading: ['var(--font-heading)', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
"""

    def _get_vite_config_content(self) -> str:
        return """import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
})
"""

    def _get_package_json_content(self) -> str:
        return """{
  "name": "trackit-app",
  "private": true,
  "version": "0.0.1",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@supabase/supabase-js": "^2.24.0",
    "pinia": "^2.1.4",
    "vue": "^3.3.4",
    "vue-router": "^4.2.2"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^4.2.3",
    "autoprefixer": "^10.4.14",
    "postcss": "^8.4.24",
    "tailwindcss": "^3.3.2",
    "vite": "^4.3.9"
  }
}
"""

    def _get_app_vue_content(self) -> str:
        return """<template>
  <div id="app" class="min-h-screen bg-background text-text transition-colors duration-300">
    <router-view />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from '@/store';
import { supabase } from '@/supabase/client';

const router = useRouter();
const store = useStore();

onMounted(() => {
  // Setup auth listener
  supabase.auth.onAuthStateChange((event, session) => {
    if (event === 'SIGNED_IN' && session) {
      store.setUser(session.user);
      store.loadUserPreferences();
    } else if (event === 'SIGNED_OUT') {
      store.clearUser();
      router.push('/');
    }
  });
  
  // Check for existing session
  const checkSession = async () => {
    const { data } = await supabase.auth.getSession();
    if (data.session) {
      store.setUser(data.session.user);
      store.loadUserPreferences();
    }
  };
  
  checkSession();
});
</script>

<style>
@import '@/styles/tailwind.css';
@import '@/styles/themes.css';
</style>
"""

    def _get_main_js_content(self) -> str:
        return """import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import App from './App.vue'

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(router)
app.mount('#app')
"""

    def _get_router_content(self) -> str:
        return """import { createRouter, createWebHistory } from 'vue-router'
import { supabase } from '@/supabase/client'

// Import components
import Home from '@/pages/Home.vue'
import Login from '@/pages/Login.vue'
import Register from '@/pages/Register.vue'
import DashboardLayout from '@/layouts/DashboardLayout.vue'
import Dashboard from '@/pages/Dashboard.vue'
import Projects from '@/pages/Projects.vue'
import ScrumBoard from '@/pages/ScrumBoard.vue'
import Matrix from '@/pages/Matrix.vue'
import History from '@/pages/History.vue'
import Profile from '@/pages/Profile.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/dashboard',
    component: DashboardLayout,
    meta: { requiresAuth: true },
    children: [
      {
        path: '',
        redirect: '/dashboard/projects'
      },
      {
        path: 'projects',
        name: 'Projects',
        component: Projects
      },
      {
        path: 'scrum',
        name: 'ScrumBoard',
        component: ScrumBoard
      },
      {
        path: 'matrix',
        name: 'Matrix',
        component: Matrix
      },
      {
        path: 'history',
        name: 'History',
        component: History
      },
      {
        path: 'profile',
        name: 'Profile',
        component: Profile
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation guard for auth routes
router.beforeEach(async (to, from, next) => {
  const { data } = await supabase.auth.getSession()
  const isLoggedIn = !!data.session
  
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isLoggedIn) {
      next({ path: '/login' })
    } else {
      next()
    }
  } else {
    // For non-auth pages, redirect to dashboard if already logged in
    if (isLoggedIn && (to.path === '/login' || to.path === '/register' || to.path === '/')) {
      next({ path: '/dashboard' })
    } else {
      next()
    }
  }
})

export default router
"""

    def _get_store_content(self) -> str:
        return """import { defineStore } from 'pinia'
import { supabase } from '@/supabase/client'

export const useStore = defineStore('main', {
  state: () => ({
    user: null,
    theme: 'ocean-breeze', // Default theme
    font: 'Inter', // Default font
    projects: [],
    todos: [],
    isToDoOpen: false
  }),
  
  getters: {
    isLoggedIn: (state) => !!state.user,
    isDarkTheme: (state) => state.theme.includes('midnight') || 
                           state.theme.includes('galaxy') || 
                           state.theme.includes('forest-night') || 
                           state.theme.includes('cyber-noir') ||
                           state.theme.includes('solar-void')
  },
  
  actions: {
    setUser(user) {
      this.user = user;
    },
    
    clearUser() {
      this.user = null;
      this.projects = [];
      this.todos = [];
    },
    
    setTheme(themeName) {
      this.theme = themeName;
      document.documentElement.className = themeName;
      
      if (this.user) {
        this.saveUserPreferences();
      }
    },
    
    setFont(fontName) {
      this.font = fontName;
      document.documentElement.style.setProperty('--font-body', fontName);
      
      if (this.user) {
        this.saveUserPreferences();
      }
    },
    
    toggleToDo() {
      this.isToDoOpen = !this.isToDoOpen;
    },
    
    async loadUserPreferences() {
      if (!this.user) return;
      
      const { data, error } = await supabase
        .from('user_preferences')
        .select('theme, font')
        .eq('user_id', this.user.id)
        .single();
      
      if (data && !error) {
        this.setTheme(data.theme || 'ocean-breeze');
        this.setFont(data.font || 'Inter');
      } else {
        // Set defaults if no preferences
        this.setTheme('ocean-breeze');
        this.setFont('Inter');
      }
    },
    
    async saveUserPreferences() {
      if (!this.user) return;
      
      const { error } = await supabase
        .from('user_preferences')
        .upsert({
          user_id: this.user.id,
          theme: this.theme,
          font: this.font
        });
        
      if (error) {
        console.error('Error saving user preferences:', error);
      }
    },
    
    async loadProjects() {
      if (!this.user) return;
      
      const { data, error } = await supabase
        .from('projects')
        .select('*')
        .eq('user_id', this.user.id)
        .order('created_at', { ascending: false });
        
      if (data && !error) {
        this.projects = data;
      } else {
        console.error('Error loading projects:', error);
      }
    },
    
    async loadTodos() {
      if (!this.user) return;
      
      const { data, error } = await supabase
        .from('todos')
        .select('*')
        .eq('user_id', this.user.id)
        .order('created_at', { ascending: false });
        
      if (data && !error) {
        this.todos = data;
      } else {
        console.error('Error loading todos:', error);
      }
    }
  }
})
"""

    def _get_supabase_client_content(self) -> str:
        return """import { createClient } from '@supabase/supabase-js'

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY

export const supabase = createClient(supabaseUrl, supabaseAnonKey)
"""

    def _get_themes_css_content(self) -> str:
        return """/* Theme Variables */

/* Light Themes */
.ocean-breeze {
  --color-primary: #38bdf8;
  --color-secondary: #0ea5e9;
  --color-accent: #0284c7;
  --color-background: #f0f9ff;
  --color-text: #0f172a;
  --font-body: 'Inter', sans-serif;
  --font-heading: 'Montserrat', sans-serif;
}

.sunrise-glow {
  --color-primary: #fb923c;
  --color-secondary: #f97316;
  --color-accent: #ea580c;
  --color-background: #fff7ed;
  --color-text: #431407;
  --font-body: 'Roboto', sans-serif;
  --font-heading: 'Playfair Display', serif;
}

.minimal-mist {
  --color-primary: #64748b;
  --color-secondary: #475569;
  --color-accent: #334155;
  --color-background: #f8fafc;
  --color-text: #0f172a;
  --font-body: 'Lato', sans-serif;
  --font-heading: 'Helvetica Neue', sans-serif;
}

.soft-leaf {
  --color-primary: #84cc16;
  --color-secondary: #65a30d;
  --color-accent: #4d7c0f;
  --color-background: #f7fee7;
  --color-text: #1a2e05;
  --font-body: 'Nunito', sans-serif;
  --font-heading: 'Nunito Sans', sans-serif;
}

.neon-day {
  --color-primary: #3b82f6; 
  --color-secondary: #2563eb;
  --color-accent: #1d4ed8;
  --color-background: #eff6ff;
  --color-text: #1e3a8a;
  --font-body: 'Quicksand', sans-serif;
  --font-heading: 'Poppins', sans-serif;
}

/* Dark Themes */
.midnight-code {
  --color-primary: #22d3ee;
  --color-secondary: #06b6d4;
  --color-accent: #0891b2;
  --color-background: #0f172a;
  --color-text: #e2e8f0;
  --font-body: 'Source Code Pro', monospace;
  --font-heading: 'Space Mono', monospace;
}

.galaxy-grape {
  --color-primary: #c084fc;
  --color-secondary: #a855f7;
  --color-accent: #9333ea;
  --color-background: #1a103d;
  --color-text: #e9d5ff;
  --font-body: 'Rubik', sans-serif;
  --font-heading: 'Exo 2', sans-serif;
}

.forest-night {
  --color-primary: #4ade80;
  --color-secondary: #22c55e;
  --color-accent: #16a34a;
  --color-background: #0d160b;
  --color-text: #dcfce7;
  --font-body: 'Merriweather', serif;
  --font-heading: 'Bitter', serif;
}

.cyber-noir {
  --color-primary: #ec4899;
  --color-secondary: #db2777;
  --color-accent: #be185d;
  --color-background: #18181b;
  --color-text: #f5f5f5;
  --font-body: 'IBM Plex Sans', sans-serif;
  --font-heading: 'Rajdhani', sans-serif;
}

.solar-void {
  --color-primary: #fcd34d;
  --color-secondary: #fbbf24;
  --color-accent: #f59e0b;
  --color-background: #030711;
  --color-text: #fef3c7;
  --font-body: 'Titillium Web', sans-serif;
  --font-heading: 'Orbitron', sans-serif;
}
"""

    def _get_tailwind_css_content(self) -> str:
        return """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .btn-primary {
    @apply bg-primary text-white py-2 px-4 rounded-md hover:bg-secondary transition-colors;
  }
  
  .btn-secondary {
    @apply bg-secondary/10 text-secondary py-2 px-4 rounded-md hover:bg-secondary/20 transition-colors;
  }
  
  .card {
    @apply bg-white dark:bg-gray-800 rounded-lg shadow-md p-4;
  }
  
  .input {
    @apply rounded-md border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 py-2 px-3;
  }
}
"""

    # Default component contents - placeholders for brevity
    def _get_sidebar_content(self) -> str:
        return """<template>
  <div class="sidebar h-screen bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-white" :class="{ 'w-64': !collapsed, 'w-16': collapsed }">
    <div class="p-4 flex justify-between items-center">
      <div v-if="!collapsed" class="text-xl font-bold">TrackIt 2.0</div>
      <button @click="toggleSidebar" class="p-1 rounded hover:bg-gray-200 dark:hover:bg-gray-800">
        <span v-if="collapsed">»</span>
        <span v-else>«</span>
      </button>
    </div>
    
    <nav class="mt-4">
      <router-link 
        v-for="(link, index) in navLinks" 
        :key="index"
        :to="link.to"
        class="flex items-center p-4 hover:bg-gray-200 dark:hover:bg-gray-800"
      >
        <span class="icon">{{ link.icon }}</span>
        <span v-if="!collapsed" class="ml-3">{{ link.text }}</span>
      </router-link>
    </nav>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const collapsed = ref(false);
const navLinks = [
  { icon: '📊', text: 'Projects', to: '/dashboard/projects' },
  { icon: '📋', text: 'Scrum Board', to: '/dashboard/scrum' },
  { icon: '🎯', text: 'Priority Matrix', to: '/dashboard/matrix' },
  { icon: '📜', text: 'History', to: '/dashboard/history' },
  { icon: '👤', text: 'Profile', to: '/dashboard/profile' }
];

const toggleSidebar = () => {
  collapsed.value = !collapsed.value;
};
</script>
"""

    def _get_navbar_content(self) -> str:
        return """<template>
  <div class="navbar flex justify-between items-center bg-white dark:bg-gray-800 shadow-sm p-4">
    <div class="flex items-center">
      <h1 class="text-xl font-bold text-gray-800 dark:text-white">{{ currentPage }}</h1>
    </div>
    
    <div class="flex items-center space-x-4">
      <button @click="toggleTodo" class="p-2 rounded-md hover:bg-gray-200 dark:hover:bg-gray-700">
        <span class="text-xl">📝</span>
      </button>
      
      <div class="relative">
        <button @click="toggleProfileMenu" class="flex items-center space-x-2">
          <div class="w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center">
            {{ userInitials }}
          </div>
          <span class="hidden md:block text-gray-800 dark:text-white">{{ userName }}</span>
        </button>
        
        <div v-if="profileMenuOpen" class="absolute right-0 mt-2 w-48 bg-white dark:bg-gray-800 rounded-md shadow-lg py-1 z-10">
          <router-link to="/dashboard/profile" class="block px-4 py-2 text-gray-800 dark:text-white hover:bg-gray-200 dark:hover:bg-gray-700">
            Profile
          </router-link>
          <button @click="logout" class="block w-full text-left px-4 py-2 text-gray-800 dark:text-white hover:bg-gray-200 dark:hover:bg-gray-700">
            Logout
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useStore } from '@/store';
import { supabase } from '@/supabase/client';

const store = useStore();
const route = useRoute();
const router = useRouter();
const profileMenuOpen = ref(false);

const currentPage = computed(() => {
  const routeName = route.name;
  return routeName ?? 'Dashboard';
});

const userName = computed(() => {
  return store.user?.email ?? 'User';
});

const userInitials = computed(() => {
  if (!store.user) return 'U';
  
  const email = store.user.email;
  if (!email) return 'U';
  
  return email.charAt(0).toUpperCase();
});

const toggleProfileMenu = () => {
  profileMenuOpen.value = !profileMenuOpen.value;
};

const toggleTodo = () => {
  store.toggleToDo();
};

const logout = async () => {
  await supabase.auth.signOut();
  router.push('/');
};
</script>
"""

    def _get_todo_pane_content(self) -> str:
        return """<template>
  <div class="todo-pane fixed right-0 top-0 h-full w-80 bg-white dark:bg-gray-800 shadow-lg transform transition-transform"
       :class="{'translate-x-0': isOpen, 'translate-x-full': !isOpen}">
    <div class="p-4 border-b border-gray-200 dark:border-gray-700 flex justify-between items-center">
      <h2 class="text-lg font-semibold text-gray-800 dark:text-white">To-Do List</h2>
      <button @click="closeTodo" class="p-1 rounded hover:bg-gray-200 dark:hover:bg-gray-700">
        <span>×</span>
      </button>
    </div>
    
    <div class="p-4">
      <div class="mb-4">
        <input 
          v-model="newTodo" 
          @keyup.enter="addTodo"
          placeholder="Add a new task..."
          class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
        />
      </div>
      
      <div class="space-y-2">
        <div v-for="(todo, index) in todos" :key="index" class="flex items-center p-2 border-b border-gray-200 dark:border-gray-700">
          <input 
            type="checkbox" 
            :checked="todo.completed" 
            @change="toggleTodo(index)"
            class="mr-2"
          />
          <span :class="{'line-through': todo.completed}" class="flex-1 text-gray-800 dark:text-white">
            {{ todo.text }}
          </span>
          <button @click="removeTodo(index)" class="text-red-500 hover:text-red-700">
            ×
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useStore } from '@/store';

const store = useStore();
const newTodo = ref('');
const todos = ref([]);

const isOpen = computed(() => store.isToDoOpen);

onMounted(() => {
  loadTodos();
});

const loadTodos = async () => {
  // In a real app, this would fetch from Supabase
  todos.value = [
    { text: 'Create project structure', completed: true },
    { text: 'Design database schema', completed: false },
    { text: 'Implement authentication', completed: false },
  ];
};

const closeTodo = () => {
  store.toggleToDo();
};

const addTodo = () => {
  if (newTodo.value.trim()) {
    todos.value.push({
      text: newTodo.value,
      completed: false
    });
    newTodo.value = '';
  }
};

const toggleTodo = (index) => {
  todos.value[index].completed = !todos.value[index].completed;
};

const removeTodo = (index) => {
  todos.value.splice(index, 1);
};
</script>
"""

    def _get_project_card_content(self) -> str:
        return """<template>
    <div class="project-card bg-white dark:bg-gray-800 rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow">
      <div class="flex justify-between items-start">
        <div>
          <h3 class="text-lg font-semibold text-gray-800 dark:text-white">{{ project.name }}</h3>
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
    if (confirm(`Are you sure you want to delete ${props.project.name}?`)) {
      emit('delete', props.project.id);
    }
  };
  </script>
  """

    def _get_project_form_content(self) -> str:
        return """<template>
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
          <label for="name" class="block text-gray-700 dark:text-gray-300 mb-1">Project Name</label>
          <input 
            id="name"
            v-model="form.name"
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
  name: '',
  description: '',
  due_date: '',
  status: 'Not Started',
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
"""

    def _get_theme_selector_content(self) -> str:
        return """<template>
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
"""

    def _get_dashboard_layout_content(self) -> str:
        return """<template>
  <div class="dashboard-layout flex h-screen bg-background">
    <Sidebar />
    
    <div class="flex-1 flex flex-col overflow-hidden">
      <Navbar />
      
      <main class="flex-1 overflow-y-auto p-6">
        <router-view />
      </main>
    </div>
    
    <ToDoPane v-if="isToDoOpen" />
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from '@/store';
import Sidebar from '@/components/Sidebar.vue';
import Navbar from '@/components/Navbar.vue';
import ToDoPane from '@/components/ToDoPane.vue';

const store = useStore();
const isToDoOpen = computed(() => store.isToDoOpen);
</script>
"""

    def _get_home_content(self) -> str:
        return """<template>
  <div class="home-page min-h-screen">
    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-primary to-secondary text-white py-20">
      <div class="container mx-auto px-6 text-center">
        <h1 class="text-4xl md:text-6xl font-bold mb-4">TrackIt 2.0</h1>
        <p class="text-xl md:text-2xl mb-8">The ultimate productivity tool for managing your projects and tasks</p>
        <div class="flex flex-col md:flex-row justify-center space-y-4 md:space-y-0 md:space-x-4">
          <router-link to="/register" class="btn-primary text-lg py-3 px-8">Get Started</router-link>
          <router-link to="/login" class="bg-white text-primary py-3 px-8 rounded-md hover:bg-gray-100 transition-colors text-lg">Login</router-link>
        </div>
      </div>
    </section>
    
    <!-- Features Section -->
    <section class="py-16 bg-background">
      <div class="container mx-auto px-6">
        <h2 class="text-3xl font-bold text-center mb-12 text-text">Powerful Features for Every Task</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
            <div class="text-4xl mb-4 text-primary">📋</div>
            <h3 class="text-xl font-semibold mb-2 text-text">Scrum Board</h3>
            <p class="text-gray-600 dark:text-gray-400">Visualize your workflow with customizable kanban boards to track progress effectively.</p>
          </div>
          
          <!-- Feature 2 -->
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
            <div class="text-4xl mb-4 text-primary">🎯</div>
            <h3 class="text-xl font-semibold mb-2 text-text">Priority Matrix</h3>
            <p class="text-gray-600 dark:text-gray-400">Focus on what truly matters with the Eisenhower urgent-important quadrant method.</p>
          </div>
          
          <!-- Feature 3 -->
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
            <div class="text-4xl mb-4 text-primary">📝</div>
            <h3 class="text-xl font-semibold mb-2 text-text">Quick To-Dos</h3>
            <p class="text-gray-600 dark:text-gray-400">Access your to-do list from anywhere in the app for quick task management.</p>
          </div>
        </div>
      </div>
    </section>
    
    <!-- CTA Section -->
    <section class="py-16 bg-gray-100 dark:bg-gray-900">
      <div class="container mx-auto px-6 text-center">
        <h2 class="text-3xl font-bold mb-4 text-text">Ready to boost your productivity?</h2>
        <p class="text-xl mb-8 text-gray-600 dark:text-gray-400">Join thousands of users who have transformed their workflow with TrackIt 2.0</p>
        <router-link to="/register" class="btn-primary text-lg py-3 px-8">Get Started for Free</router-link>
      </div>
    </section>
    
    <!-- Footer -->
    <footer class="py-8 bg-gray-800 text-white">
      <div class="container mx-auto px-6 text-center">
        <p>&copy; 2023 TrackIt 2.0. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
// Home page component
</script>
"""

    def _get_login_content(self) -> str:
        return """<template>
  <div class="login-page min-h-screen flex items-center justify-center bg-background">
    <div class="max-w-md w-full p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
      <div class="text-center mb-6">
        <h1 class="text-3xl font-bold text-gray-800 dark:text-white">Welcome Back</h1>
        <p class="text-gray-600 dark:text-gray-400">Sign in to your TrackIt 2.0 account</p>
      </div>
      
      <form @submit.prevent="handleLogin">
        <div class="space-y-4">
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Email</label>
            <input 
              id="email"
              v-model="email"
              type="email"
              required
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
              placeholder="Enter your email"
            />
          </div>
          
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Password</label>
            <input 
              id="password"
              v-model="password"
              type="password"
              required
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
              placeholder="Enter your password"
            />
          </div>
          
          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <input id="remember-me" type="checkbox" class="h-4 w-4 text-primary" />
              <label for="remember-me" class="ml-2 block text-sm text-gray-700 dark:text-gray-300">
                Remember me
              </label>
            </div>
            
            <a href="#" class="text-sm text-primary hover:text-secondary">
              Forgot password?
            </a>
          </div>
          
          <div v-if="errorMessage" class="text-red-500 text-sm">
            {{ errorMessage }}
          </div>
          
          <button 
            type="submit"
            class="w-full py-2 px-4 bg-primary text-white rounded-md hover:bg-secondary focus:outline-none focus:ring-2 focus:ring-primary focus:ring-opacity-50"
            :disabled="loading"
          >
            {{ loading ? 'Signing in...' : 'Sign In' }}
          </button>
        </div>
      </form>
      
      <div class="mt-6 text-center">
        <p class="text-gray-600 dark:text-gray-400">
          Don't have an account? 
          <router-link to="/register" class="text-primary hover:text-secondary">
            Create one
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { supabase } from '@/supabase/client';

const router = useRouter();
const email = ref('');
const password = ref('');
const loading = ref(false);
const errorMessage = ref('');

const handleLogin = async () => {
  try {
    loading.value = true;
    errorMessage.value = '';
    
    const { data, error } = await supabase.auth.signInWithPassword({
      email: email.value,
      password: password.value
    });
    
    if (error) {
      errorMessage.value = error.message;
      return;
    }
    
    router.push('/dashboard');
    
  } catch (error) {
    errorMessage.value = 'An unexpected error occurred. Please try again.';
    console.error('Login error:', error);
  } finally {
    loading.value = false;
  }
};
</script>
"""

    def _get_register_content(self) -> str:
        return """<template>
  <div class="register-page min-h-screen flex items-center justify-center bg-background">
    <div class="max-w-md w-full p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
      <div class="text-center mb-6">
        <h1 class="text-3xl font-bold text-gray-800 dark:text-white">Create Account</h1>
        <p class="text-gray-600 dark:text-gray-400">Join TrackIt 2.0 to boost your productivity</p>
      </div>
      
      <form @submit.prevent="handleRegister">
        <div class="space-y-4">
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Email</label>
            <input 
              id="email"
              v-model="email"
              type="email"
              required
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
              placeholder="Enter your email"
            />
          </div>
          
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Password</label>
            <input 
              id="password"
              v-model="password"
              type="password"
              required
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
              placeholder="Create a password"
            />
            <p class="text-xs text-gray-500 mt-1">Password must be at least 6 characters long</p>
          </div>
          
          <div>
            <label for="confirm-password" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Confirm Password</label>
            <input 
              id="confirm-password"
              v-model="confirmPassword"
              type="password"
              required
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
              placeholder="Confirm your password"
            />
          </div>
          
          <div class="flex items-center">
            <input id="terms" type="checkbox" v-model="agreeToTerms" class="h-4 w-4 text-primary" required />
            <label for="terms" class="ml-2 block text-sm text-gray-700 dark:text-gray-300">
              I agree to the 
              <a href="#" class="text-primary hover:text-secondary">Terms of Service</a>
              and
              <a href="#" class="text-primary hover:text-secondary">Privacy Policy</a>
            </label>
          </div>
          
          <div v-if="errorMessage" class="text-red-500 text-sm">
            {{ errorMessage }}
          </div>
          
          <button 
            type="submit"
            class="w-full py-2 px-4 bg-primary text-white rounded-md hover:bg-secondary focus:outline-none focus:ring-2 focus:ring-primary focus:ring-opacity-50"
            :disabled="loading || !agreeToTerms || password !== confirmPassword"
          >
            {{ loading ? 'Creating Account...' : 'Create Account' }}
          </button>
        </div>
      </form>
      
      <div class="mt-6 text-center">
        <p class="text-gray-600 dark:text-gray-400">
          Already have an account? 
          <router-link to="/login" class="text-primary hover:text-secondary">
            Sign in
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import { supabase } from '@/supabase/client';

const router = useRouter();
const email = ref('');
const password = ref('');
const confirmPassword = ref('');
const agreeToTerms = ref(false);
const loading = ref(false);
const errorMessage = ref('');

// Watch for password mismatch
watch([password, confirmPassword], ([newPassword, newConfirmPassword]) => {
  if (newConfirmPassword && newPassword !== newConfirmPassword) {
    errorMessage.value = 'Passwords do not match';
  } else {
    errorMessage.value = '';
  }
});

const handleRegister = async () => {
  if (password.value !== confirmPassword.value) {
    errorMessage.value = 'Passwords do not match';
    return;
  }
  
  if (password.value.length < 6) {
    errorMessage.value = 'Password must be at least 6 characters long';
    return;
  }
  
  try {
    loading.value = true;
    errorMessage.value = '';
    
    const { data, error } = await supabase.auth.signUp({
      email: email.value,
      password: password.value
    });
    
    if (error) {
      errorMessage.value = error.message;
      return;
    }
    
    // Redirect to dashboard or confirmation page
    router.push('/dashboard');
    
  } catch (error) {
    errorMessage.value = 'An unexpected error occurred. Please try again.';
    console.error('Registration error:', error);
  } finally {
    loading.value = false;
  }
};
</script>
"""

    def _get_dashboard_content(self) -> str:
        return """<template>
  <div class="dashboard-redirect">
    <!-- This is just a redirect component -->
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

onMounted(() => {
  // Redirect to projects by default
  router.replace('/dashboard/projects');
});
</script>
"""

    def _get_projects_content(self) -> str:
        return """<template>
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
          name: projectData.name,
          description: projectData.description,
          due_date: projectData.due_date,
          status: projectData.status,
          progress: projectData.progress
        })
        .eq('id', projectData.id);
      
      if (error) throw error;
      
      // Update local state
      const index = projects.value.findIndex(p => p.id === projectData.id);
      if (index !== -1) {
        projects.value[index] = { ...projects.value[index], ...projectData };
      }
    } else {
      // Create new project
      const { data, error } = await supabase
        .from('projects')
        .insert({
          user_id: store.user.id,
          name: projectData.name,
          description: projectData.description,
          due_date: projectData.due_date,
          status: projectData.status,
          progress: projectData.progress
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
"""

    def _get_scrum_board_content(self) -> str:
        return """<template>
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
"""

    def _get_matrix_content(self) -> str:
        return """<template>
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
"""

    def _get_history_content(self) -> str:
        return """<template>
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
"""

    def _get_profile_content(self) -> str:
        return """<template>
  <div class="profile-page">
    <div class="mb-6">
      <h1 class="text-2xl font-bold text-gray-800 dark:text-white">Profile Settings</h1>
      <p class="text-gray-600 dark:text-gray-400">Manage your account and preferences</p>
    </div>
    
    <!-- Profile and Settings Tabs -->
    <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden">
      <div class="flex border-b border-gray-200 dark:border-gray-700">
        <button 
          @click="activeTab = 'account'" 
          class="flex-1 py-4 px-6 text-center font-medium"
          :class="activeTab === 'account' ? 'text-primary border-b-2 border-primary' : 'text-gray-500 dark:text-gray-400'"
        >
          Account
        </button>
        <button 
          @click="activeTab = 'theme'" 
          class="flex-1 py-4 px-6 text-center font-medium"
          :class="activeTab === 'theme' ? 'text-primary border-b-2 border-primary' : 'text-gray-500 dark:text-gray-400'"
        >
          Appearance
        </button>
        <button 
          @click="activeTab = 'security'" 
          class="flex-1 py-4 px-6 text-center font-medium"
          :class="activeTab === 'security' ? 'text-primary border-b-2 border-primary' : 'text-gray-500 dark:text-gray-400'"
        >
          Security
        </button>
      </div>
      
      <div class="p-6">
        <!-- Account Tab -->
        <div v-if="activeTab === 'account'">
          <div class="flex flex-col md:flex-row md:items-center mb-6">
            <div class="w-24 h-24 rounded-full bg-gray-300 dark:bg-gray-600 flex items-center justify-center mb-4 md:mb-0 md:mr-6">
              <span v-if="!profileImage" class="text-3xl text-gray-600 dark:text-gray-300">
                {{ userInitials }}
              </span>
              <img v-else :src="profileImage" class="w-full h-full rounded-full object-cover" alt="Profile" />
            </div>
            
            <div class="flex-1">
              <h2 class="text-xl font-semibold text-gray-800 dark:text-white mb-2">{{ userName }}</h2>
              <p class="text-gray-600 dark:text-gray-400">{{ userEmail }}</p>
              
              <div class="mt-4">
                <label class="btn-secondary cursor-pointer">
                  <span>Change Profile Picture</span>
                  <input type="file" class="hidden" @change="handleProfileImageChange" accept="image/*" />
                </label>
              </div>
            </div>
          </div>
          
          <form @submit.prevent="updateProfile" class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                Full Name
              </label>
              <input 
                v-model="profileForm.name"
                type="text"
                class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                Email
              </label>
              <input 
                v-model="profileForm.email"
                type="email"
                class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
                disabled
              />
              <p class="text-xs text-gray-500 mt-1">To change email, please contact support</p>
            </div>
            
            <div>
              <button type="submit" class="btn-primary">
                Update Profile
              </button>
            </div>
          </form>
        </div>
        
        <!-- Theme Tab -->
        <div v-if="activeTab === 'theme'">
          <ThemeSelector />
        </div>
        
        <!-- Security Tab -->
        <div v-if="activeTab === 'security'">
          <form @submit.prevent="changePassword" class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                Current Password
              </label>
              <input 
                v-model="passwordForm.currentPassword"
                type="password"
                class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
                required
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                New Password
              </label>
              <input 
                v-model="passwordForm.newPassword"
                type="password"
                class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
                required
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                Confirm New Password
              </label>
              <input 
                v-model="passwordForm.confirmPassword"
                type="password"
                class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded dark:bg-gray-700 dark:text-white"
                required
              />
            </div>
            
            <div v-if="passwordError" class="text-red-500 text-sm">
              {{ passwordError }}
            </div>
            
            <div>
              <button 
                type="submit" 
                class="btn-primary"
                :disabled="passwordForm.newPassword !== passwordForm.confirmPassword"
              >
                Change Password
              </button>
            </div>
          </form>
          
          <div class="mt-8 pt-8 border-t border-gray-200 dark:border-gray-700">
            <h3 class="text-lg font-medium text-red-600 dark:text-red-400 mb-4">Danger Zone</h3>
            <button 
              @click="confirmLogout"
              class="bg-gray-100 text-red-600 dark:bg-gray-700 dark:text-red-400 py-2 px-4 rounded-md hover:bg-gray-200 dark:hover:bg-gray-600 mr-4"
            >
              Logout
            </button>
            <button 
              @click="confirmDeleteAccount"
              class="bg-red-100 text-red-600 dark:bg-red-900/30 dark:text-red-400 py-2 px-4 rounded-md hover:bg-red-200 dark:hover:bg-red-800/30"
            >
              Delete Account
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from '@/store';
import { supabase } from '@/supabase/client';
import ThemeSelector from '@/components/ThemeSelector.vue';

const router = useRouter();
const store = useStore();
const activeTab = ref('account');
const profileImage = ref(null);
const passwordError = ref('');

const profileForm = ref({
  name: 'John Doe', // In a real app, get from store or Supabase
  email: store.user?.email || 'user@example.com'
});

const passwordForm = ref({
  currentPassword: '',
  newPassword: '',
  confirmPassword: ''
});

const userName = computed(() => {
  return profileForm.value.name || 'User';
});

const userEmail = computed(() => {
  return profileForm.value.email || 'No email';
});

const userInitials = computed(() => {
  if (!userName.value) return 'U';
  return userName.value.charAt(0).toUpperCase();
});

const handleProfileImageChange = (event) => {
  const file = event.target.files[0];
  if (!file) return;
  
  // In a real app, upload to Supabase storage
  const reader = new FileReader();
  reader.onload = (e) => {
    profileImage.value = e.target.result;
  };
  reader.readAsDataURL(file);
};

const updateProfile = async () => {
  try {
    // In a real app, save to Supabase
    alert('Profile updated successfully!');
  } catch (error) {
    console.error('Error updating profile:', error);
    alert('Failed to update profile');
  }
};

const changePassword = async () => {
  try {
    passwordError.value = '';
    
    if (passwordForm.value.newPassword !== passwordForm.value.confirmPassword) {
      passwordError.value = 'Passwords do not match';
      return;
    }
    
    if (passwordForm.value.newPassword.length < 6) {
      passwordError.value = 'Password must be at least 6 characters long';
      return;
    }
    
    // In a real app, change password via Supabase
    const { error } = await supabase.auth.updateUser({
      password: passwordForm.value.newPassword
    });
    
    if (error) throw error;
    
    alert('Password changed successfully!');
    passwordForm.value = {
      currentPassword: '',
      newPassword: '',
      confirmPassword: ''
    };
  } catch (error) {
    console.error('Error changing password:', error);
    passwordError.value = error.message || 'Failed to change password';
  }
};

const confirmLogout = () => {
  if (confirm('Are you sure you want to log out?')) {
    supabase.auth.signOut();
    router.push('/');
  }
};

const confirmDeleteAccount = () => {
  if (confirm('Are you sure you want to delete your account? This action cannot be undone.')) {
    // In a real app, delete the user account in Supabase
    alert('Account deletion would be implemented here');
  }
};
</script>
"""

    # Entry point for script execution
    def main(self) -> None:
        """Execute the scaffolding process."""
        self.create_project()


if __name__ == "__main__":
    scaffolder = ProjectScaffolder()
    scaffolder.main()