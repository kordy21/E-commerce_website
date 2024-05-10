<script >
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import Navbar from './components/base/Navbar.vue'

import { ref } from 'vue';

export default {
  components: {
    Navbar,
    HelloWorld
  },
  setup() {
    const darkMode = ref(false);

    const handleModeChanged = (isDarkMode) => {
      darkMode.value = isDarkMode;
    };

    return { darkMode, handleModeChanged };
  },
};
</script>

<template>
  <header>
    <div class="wrapper">
      <Navbar @modeChanged="handleModeChanged" />
      <HelloWorld msg="You did it!" />

      <!-- <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav> -->
    </div>
  </header>

</template>

<style scoped>
.dark-mode {
  --background-color: #333;
  --text-color: #fff;
}

.light-mode {
  --background-color: #fff;
  --text-color: #333;
}

body {
  background-color: var(--background-color);
  color: var(--text-color);
}
</style>
