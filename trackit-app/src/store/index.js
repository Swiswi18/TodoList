// src/store/index.js
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
    isDarkTheme: (state) => 
      ['midnight-code', 'galaxy-grape', 'forest-night', 'cyber-noir', 'solar-void'].includes(state.theme)
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
      console.log('Setting theme to:', themeName);
      
      // Update store state
      this.theme = themeName;
      
      // Apply theme to document
      document.documentElement.className = themeName;
      
      // Check if we are in dark mode and update accordingly
      if (this.isDarkTheme) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
      
      // Save to local storage as fallback
      localStorage.setItem('user-theme', themeName);
      
      // Try to save to Supabase if user is logged in
      if (this.user) {
        this.saveUserPreferences().catch(err => {
          console.error('Failed to save theme to Supabase:', err);
        });
      }
    },
    
    setFont(fontName) {
      console.log('Setting font to:', fontName);
      
      // Update store state
      this.font = fontName;
      
      // Apply font to document
      document.documentElement.style.setProperty('--font-body', fontName);
      document.documentElement.style.setProperty('--font-heading', fontName);
      
      // Save to local storage as fallback
      localStorage.setItem('user-font', fontName);
      
      // Try to save to Supabase if user is logged in
      if (this.user) {
        this.saveUserPreferences().catch(err => {
          console.error('Failed to save font to Supabase:', err);
        });
      }
    },
    
    toggleToDo() {
      this.isToDoOpen = !this.isToDoOpen;
    },
    
    async loadUserPreferences() {
      console.log('Loading user preferences...');
      
      // Try to load from Supabase first
      try {
        if (this.user) {
          console.log('Loading preferences for user:', this.user.id);
          
          const { data, error } = await supabase
            .from('users')
            .select('theme, font')
            .eq('id', this.user.id)
            .single();
          
          console.log('Preferences data from Supabase:', data, 'Error:', error);
          
          if (data && !error) {
            if (data.theme) this.setTheme(data.theme);
            if (data.font) this.setFont(data.font);
            return;
          }
        }
      } catch (error) {
        console.error('Error loading preferences from Supabase:', error);
      }
      
      // Fall back to localStorage if Supabase fails or user not logged in
      const storedTheme = localStorage.getItem('user-theme');
      const storedFont = localStorage.getItem('user-font');
      
      if (storedTheme) this.setTheme(storedTheme);
      if (storedFont) this.setFont(storedFont);
    },
    
    async saveUserPreferences() {
      console.log('Saving user preferences...');
      
      if (!this.user) {
        console.log('No user logged in, saving to localStorage only');
        localStorage.setItem('user-theme', this.theme);
        localStorage.setItem('user-font', this.font);
        return;
      }
      
      try {
        console.log('Saving preferences to Supabase for user:', this.user.id);
        
        // Check if profile already exists
        const { data: existing } = await supabase
          .from('users')
          .select('id')
          .eq('id', this.user.id)
          .single();
        
        let result;
        
        if (existing) {
          // Update existing profile
          result = await supabase
            .from('users')
            .update({
              theme: this.theme,
              font: this.font
            })
            .eq('id', this.user.id);
        } else {
          // Insert new profile
          result = await supabase
            .from('users')
            .insert({
              id: this.user.id,
              theme: this.theme,
              font: this.font
            });
        }
        
        console.log('Save result:', result);
        
        if (result.error) {
          throw result.error;
        }
      } catch (error) {
        console.error('Error saving preferences to Supabase:', error);
        // Still save to localStorage as fallback
        localStorage.setItem('user-theme', this.theme);
        localStorage.setItem('user-font', this.font);
      }
    }
  }
})