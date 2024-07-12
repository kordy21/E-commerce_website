<script >
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/base/Navbar.vue'
import Footer from './components/base/Footer.vue'
import MenuMobile from '../src/components/base/MenuMobile.vue';


import { ref } from 'vue';

export default {
  components: {
    Navbar,
    MenuMobile,
    Footer
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
      <Footer />
    </div>
  </header>

</template>

<style>
h1, h2, h3 {
  font-family: "Cormorant Garamond", serif;
}
</style>
