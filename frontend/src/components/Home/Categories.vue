<template>
    <div class="overflow-hidden w-full relative">
        <div class="text-center py-6">
            <h3 class="text-sm mb-4 font-thin">WE’VE GOT YOU COVERED</h3>
            <h1 class="text-4xl">Explore The Range</h1>
        </div>
      <div class="flex transition-transform duration-500" :style="trackStyle">
        <div class="flex-shrink-0" :class="cardWidthClass" v-for="(card, index) in cards" :key="index">
          <div class="relative">
            <img :src="card.image" class="w-full h-auto object-cover" />
            <div class=" absolute text-center bottom-0 w-full">
              <span class="bg-white text-xl font-thin text-center ">{{ card.title }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>
  
  <script>
  import { ref, computed, onMounted, onUnmounted } from 'vue';
  
  export default {
    setup() {
      const currentIndex = ref(0);
      const cards = ref([
        { id: 1, image: '../../../public/images/category/10-5_180x.avif', title: 'Charms', link: '#' },
        { id: 2, image: '../../../public/images/category/10-4_180x.avif', title: 'Necklaces', link: '#' },
        { id: 3, image: '../../../public/images/category/10-3_180x.avif', title: 'Shop Earrings', link: '#' },
        { id: 4, image: '../../../public/images/category/10-2_180.avif', title: 'Wedding & Bridal', link: '#' },
        { id: 5, image: '../../../public/images/category/earings.avif', title: 'Bracelets', link: '#' },
      ]);
  
      const cardWidthClass = ref('w-1/2 md:w-1/3 lg:w-1/5'); 
  
      const getVisibleCards = () => {
        const width = window.innerWidth;
        if (width >= 1024) return 5;
        if (width >= 768) return 3;
        return 2;
      };
  
      const visibleCards = ref(getVisibleCards());
  
      const trackStyle = computed(() => ({
        transform: `translateX(-${(currentIndex.value * 100) / visibleCards.value}%)`,
      }));
  
      const updateVisibleCards = () => {
        visibleCards.value = getVisibleCards();
      };
  
      const startAutoChange = () => {
        setInterval(() => {
          currentIndex.value = (currentIndex.value + 1) % (cards.value.length - visibleCards.value + 1);
        }, 3000);
      };
  
      onMounted(() => {
        window.addEventListener('resize', updateVisibleCards);
        startAutoChange();
      });
  
      onUnmounted(() => {
        window.removeEventListener('resize', updateVisibleCards);
      });
  
      return {
        cards,
        trackStyle,
        cardWidthClass,
      };
    },
  };
  </script>
  
    <style scoped>

    </style>
  