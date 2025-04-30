<template>
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
