import { createRouter, createWebHistory } from 'vue-router'
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
