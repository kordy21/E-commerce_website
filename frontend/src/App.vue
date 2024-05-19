<script >
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import Navbar from './components/base/Navbar.vue'
import MenuMobile from '../src/components/base/MenuMobile.vue';


import { ref } from 'vue';

export default {
  components: {
    Navbar,
    HelloWorld,
    MenuMobile
  },
  setup() {
    const darkMode = ref(false);

    const toggleDarkMode = () => {
      darkMode.value = !darkMode.value;
      if (darkMode.value) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    };
    return { darkMode,toggleDarkMode };
  },
};
</script>

<template>
  <header>
    <div class="wrapper">
      <Navbar :darkMode="darkMode" @toggleDM="toggleDarkMode"/>
      
      <RouterView />
      <HelloWorld msg="You did it!" />

      <!-- <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav> -->
    </div>
  </header>

</template>

<style>
h1, h2, h3 {
  font-family: "Cormorant Garamond", serif;
}
</style>
