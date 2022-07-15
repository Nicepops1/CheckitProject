import Main from '@/pages/Main'
import Map from '@/pages/Map'
import AddPlace from '@/pages/AddPlace'
import SignIn from '@/pages/SignIn'
import SignUp from '@/pages/SignUp'
import Account from '@/pages/Account'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: Main
  },
  {
    path: '/map',
    component: Map
  },
  {
    path: '/addPlace',
    component: AddPlace
  },
  {
    path: '/signin',
    component: SignIn
  },
  {
    path: '/signup',
    component: SignUp
  },
  {
    path: '/account',
    component : Account
  }
]

const router = createRouter({
  routes,
  history: createWebHistory(process.env.BASE_URL)
})

export default router;