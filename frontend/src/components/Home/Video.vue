<template>
    <section class="mb-10 relative h-96">
        <video class="w-full object-cover" playsinline loop autoplay muted>
            <source src="https://cdn.shopify.com/videos/c/vp/33b96d6501564bb9be82ec426072ed06/33b96d6501564bb9be82ec426072ed06.HD-1080p-4.8Mbps-10381755.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <main class="absolute top-1/3 w-full text-center">
            <h1 class="text-4xl sm:text-5xl md:text-6xl lg:text-7xl text-white font-bold my-4">Stand Out In Style</h1>
            <button class="discover">DISCOVER NOW</button>
        </main>
    </section>
</template>

<script setup>

</script>

<style scoped>
section{
    height: 500px;
}
video{
    height: 500px;
}
.discover{
    border: 2px solid #fff;
    cursor: pointer;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 3px;
    background: white;
    padding: 15px;
    position: relative;
    margin-top: 8px;
    z-index: 1;
    transition: all 0.1s ease-in-out
  }
  .discover:hover{
    border: 2px solid #cb8161 ; 
    background: #cb8161 ;
    color:white
  }
</style>