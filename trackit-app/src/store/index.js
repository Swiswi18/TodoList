import { defineStore } from 'pinia'
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
