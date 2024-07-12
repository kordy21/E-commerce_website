<template>
    <div class="py-12">
      <div class="flex overflow-hidden justify-around flex-wrap">
        <div
          class="bg-white w-64"
          v-for="(product, index) in visibleProducts"
          :key="index"
        >
          <img :src="product.image" :alt="product.name" class="w-full h-auto mb-4" />
          <main class="text-center">
            <div class="rating flex justify-center mb-2">
              <span
                v-for="star in 5"
                :key="star"
                class="star text-xl"
                :class="{ 'text-secondary-100': star <= product.rating, 'text-gray-300 ': star > product.rating }"
              >★</span>
            </div>
            <h3 class="text-xl font-semibold mb-2">{{ product.name }}</h3>
            <p class="text-lg text-secondary-100">LE {{ product.price }}</p> 
          </main>
        </div>
      </div>
      <div class="navigation-buttons flex justify-around mt-12">
        <button
          @click="prev"
          :disabled="currentIndex === 0"
          class="nav-button text-2xl mx-2 p-2"
          :class="{ 'text-gray-500': currentIndex === 0, 'text-secondary-100': currentIndex > 0 }"
        >
        <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M872 474H286.9l350.2-304c5.6-4.9 2.2-14-5.2-14h-88.5c-3.9 0-7.6 1.4-10.5 3.9L155 487.8a31.96 31.96 0 0 0 0 48.3L535.1 866c1.5 1.3 3.3 2 5.2 2h91.5c7.4 0 10.8-9.2 5.2-14L286.9 550H872c4.4 0 8-3.6 8-8v-60c0-4.4-3.6-8-8-8z"></path></svg>
        </button>
        <button
          @click="next"
          :disabled="currentIndex >= products.length - itemsPerPage"
          class="nav-button text-2xl mx-2 p-2"
          :class="{ 'text-gray-500': currentIndex >= products.length - itemsPerPage, 'text-secondary-100': currentIndex < products.length - itemsPerPage }"
        >
        <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M869 487.8L491.2 159.9c-2.9-2.5-6.6-3.9-10.5-3.9h-88.5c-7.4 0-10.8 9.2-5.2 14l350.2 304H152c-4.4 0-8 3.6-8 8v60c0 4.4 3.6 8 8 8h585.1L386.9 854c-5.6 4.9-2.2 14 5.2 14h91.5c1.9 0 3.8-.7 5.2-2L869 536.2a32.07 32.07 0 0 0 0-48.4z"></path></svg>        </button>
      </div>
    </div>
</template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue';
  
  const products = ref([
    {
      name: 'Product 1',
      rating: 4,
      price: 29.99,
      image: '../../../public/images/products/product-1-2.jpg'
    },
    {
      name: 'Product 2',
      rating: 5,
      price: 39.99,
      image: '../../../public/images/products/product-1-1.jpg'
    },
    {
      name: 'Product 3',
      rating: 3,
      price: 49.99,
      image: '../../../public/images/products/product-11-1.webp'
    },
    {
      name: 'Product 4',
      rating: 4,
      price: 19.99,
      image: '../../../public/images/products/product-11-2.webp'
    },
    {
      name: 'Product 5',
      rating: 2,
      price: 24.99,
      image: '../../../public/images/products/product-2-1.webp'
    },
    {
      name: 'Product 6',
      rating: 5,
      price: 34.99,
      image: '../../../public/images/products/product-10-1.webp'
    },
    {
      name: 'Product 7',
      rating: 4,
      price: 29.99,
      image: '../../../public/images/products/product-30-15.webp'
    },
    {
      name: 'Product 8',
      rating: 5,
      price: 39.99,
      image: '../../../public/images/products/product-6-2.webp'
    },
    {
      name: 'Product 9',
      rating: 3,
      price: 49.99,
      image: '../../../public/images/products/product-9-1.jpg'
    },
    {
      name: 'Product 10',
      rating: 4,
      price: 19.99,
      image: '../../../public/images/products/product-56-2.webp'
    },
  ]);
  
  const currentIndex = ref(0);
  const itemsPerPage = ref(5);
  
  const updateItemsPerPage = () => {
    if (window.innerWidth >= 1024) {
      itemsPerPage.value = 5;
    } else if (window.innerWidth >= 768) {
      itemsPerPage.value = 3;
    } else {
      itemsPerPage.value = 2;
    }
  };
  
  const visibleProducts = computed(() => {
    return products.value.slice(currentIndex.value, currentIndex.value + itemsPerPage.value);
  });
  
  const prev = () => {
    if (currentIndex.value > 0) {
      currentIndex.value -= itemsPerPage.value;
    }
  };
  
  const next = () => {
    if (currentIndex.value < products.value.length - itemsPerPage.value) {
      currentIndex.value += itemsPerPage.value;
    }
  };
  
  onMounted(() => {
    updateItemsPerPage();
    window.addEventListener('resize', updateItemsPerPage);
  });
  
  </script>
  
  <style scoped>
  .star {
    font-size: 1.5rem;
  }
  
  .nav-button:disabled {
    cursor: not-allowed;
  }
  </style>
  