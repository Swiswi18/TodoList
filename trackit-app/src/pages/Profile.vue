<template>
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
