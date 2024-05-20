<template>
    <div class="slider-container">
      <div class="slide" v-for="(slide, index) in slides" :key="index" :class="{ active: index === currentIndex }" :style="{ backgroundImage: `url(${slide.image})` }">
        <div class="slide-content">
          <h1>{{ slide.title }}</h1>
          <h2>{{ slide.subTitle }}</h2>
          <button class="explore">EXPLORE SHOP</button>
        </div>
      </div>
      <button @click="prevSlide" class="prev-btn">
        <svg stroke="currentColor" fill="#cb8161" stroke-width="0" viewBox="0 0 1024 1024" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M872 474H286.9l350.2-304c5.6-4.9 2.2-14-5.2-14h-88.5c-3.9 0-7.6 1.4-10.5 3.9L155 487.8a31.96 31.96 0 0 0 0 48.3L535.1 866c1.5 1.3 3.3 2 5.2 2h91.5c7.4 0 10.8-9.2 5.2-14L286.9 550H872c4.4 0 8-3.6 8-8v-60c0-4.4-3.6-8-8-8z"></path></svg>
      </button>
      <button @click="nextSlide" class="next-btn">
        <svg stroke="currentColor" fill="#cb8161" stroke-width="0" viewBox="0 0 1024 1024" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M869 487.8L491.2 159.9c-2.9-2.5-6.6-3.9-10.5-3.9h-88.5c-7.4 0-10.8 9.2-5.2 14l350.2 304H152c-4.4 0-8 3.6-8 8v60c0 4.4 3.6 8 8 8h585.1L386.9 854c-5.6 4.9-2.2 14 5.2 14h91.5c1.9 0 3.8-.7 5.2-2L869 536.2a32.07 32.07 0 0 0 0-48.4z"></path></svg>
      </button>
    </div>
</template>
  
  <script>
  export default {
    data() {
      return {
        currentIndex: 0,
        slides: [
          {
            image: '../../public/images/slider/slider-10-2_1.jpg',
            title: 'Now up to 70% off*',
            subTitle: 'MID YEAR SALE'
          },
          {
            image: '../../public/images/slider/slider-10.jpg',
            title: 'Oh, Hello Newness!',
            subTitle: 'MID YEAR SALE'
          },
          {
            image: '../../public/images/slider/slider-10-1_1.jpg',
            title: 'Best of the Best',
            subTitle: 'MID YEAR SALE'
          }
        ]
      };
    },
    mounted() {
      this.startSlider();
    },
    beforeUnmount() {
      clearInterval(this.interval);
    },
    methods: {
      startSlider() {
        this.interval = setInterval(() => {
          this.nextSlide();
        }, 3000); // Change slide every 10 seconds
      },
      nextSlide() {
        this.currentIndex = (this.currentIndex + 1) % this.slides.length;
      },
      prevSlide() {
        this.currentIndex = (this.currentIndex - 1 + this.slides.length) % this.slides.length;
      }
    }
  };
  </script>
  
  <style scoped>
  .slider-container {
    position: relative;
    width: 100%;
    height: 80vh; 
    overflow: hidden;
    margin: auto;
  }
  
  .slide {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
    background-size: cover;
    background-position: center;
    transition: opacity 1s ease-in-out; 
  }
  
  .slide.active {
    opacity: 1;
  }
  
  .slide-content {
    color: white;
    padding: 10px;
    border-radius: 5px;
    text-align: center;
  }
  
  .prev-btn,
  .next-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    border: none;
    color: white;
    padding: 10px;
    cursor: pointer;
  }
  
  .prev-btn {
    left: 10px;
  }
  
  .next-btn {
    right: 10px;
  }
  h1{
    font-size: 4em;
    font-weight: 700;
  }
  h2{
    font-size: 3em;
    font-weight: 500;
  }
  .explore{
    border: 2px solid #fff;
    cursor: pointer;
    font-size: 11px;
    font-weight: 400;
    letter-spacing: 3px;
    padding: 15px;
    position: relative;
    margin-top: 8px;
    z-index: 1;
    transition: all 0.1s ease-in-out
  }
  .explore:hover{
    border: 2px solid #cb8161 ; 
    background: #cb8161 ;

  }
  </style>
  