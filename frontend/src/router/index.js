import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import ShopPage from '../views/ShopPage.vue'
import ContactPage from '../views/ContactPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/shop',
      name: 'shop',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: ShopPage
    },
    {
      path: '/contact',
      name: 'contact',
      component: ContactPage
    },
  ]
})

export default router
