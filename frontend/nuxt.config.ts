import { defineNuxtConfig } from "nuxt/config"
import yaml from 'js-yaml'
import fs from 'fs'
import path from 'path'

// Load YAML config
const configPath = path.resolve(__dirname, '..', 
  process.env.NODE_ENV === 'development' ? 'configs/bow-config.dev.yaml' : 'bow-config.yaml'
)
const versionPath = process.env.NODE_ENV === 'development'
  ? path.resolve(__dirname, '..', 'VERSION')
  : path.resolve('/app', 'VERSION')
const config = yaml.load(fs.readFileSync(configPath, 'utf8'))
const version = fs.readFileSync(versionPath, 'utf8')

export default defineNuxtConfig({
  devtools: { enabled: true },
  ssr: false,

  modules: [
    "@nuxt/ui",
    "@sidebase/nuxt-auth",
    'nuxt-tiptap-editor',
    '@nuxtjs/mdc',
    '@nuxt-alt/proxy',
    'nuxt-3-intercom',
    'nuxt-echarts'
  ],

  echarts: {
    charts: [
      'BarChart',
      'LineChart',
      'PieChart',
      'ScatterChart',
      'EffectScatterChart',
      'BoxplotChart',
      'CandlestickChart',
      'GaugeChart',
      'FunnelChart',
      'HeatmapChart',
      'LinesChart',
      'MapChart',
      'ParallelChart',
      'RadarChart',
      'SunburstChart',
      'TreeChart',
      'TreemapChart'
    ],
    components: [
      'AriaComponent',
      'AxisPointerComponent',
      'BrushComponent',
      'CalendarComponent',
      'DataZoomComponent',
      'DataZoomInsideComponent',
      'DataZoomSliderComponent',
      'DatasetComponent',
      'GridComponent',
      'LegendComponent',
      'MarkLineComponent',
      'MarkPointComponent',
      'ParallelComponent',
      'RadarComponent'
    ]
  },

  intercom: {
    appId: 'ocwih86k',
    autoBoot: false
  },

  tiptap: {
    prefix: 'Tiptap'
  },

  plugins: [
    '~/plugins/vue-draggable-resizable.client.js',
    '~/plugins/vue-flow.client.js'
  ],

  icon: {
    localApiEndpoint: '/_nuxt_icon'
  },

  colorMode: {
    preference: 'light'
  },

  proxy: {
    debug: true,
    experimental: {
        listener: true
    },
    proxies: {
        '/ws/api': {
            target: 'ws://127.0.0.1:8000',
            ws: true,
            changeOrigin: true,
            secure: false,
            rewrite: (path) => path,
            headers: {
                'Upgrade': 'websocket',
                'Connection': 'Upgrade'
            }
        },
        '/api': {
            target: 'http://127.0.0.1:8000',
            changeOrigin: true,
            secure: false,
            rewrite: (path) => path
        }
    }
},

  auth: {
    baseURL: '/api/', // Proxy now handled by NGINX
    provider: {
      type: 'local',
      pages: {
        login: '/users/sign-in',
        signup: '/users/sign-up'
      },
      endpoints: {
        signIn: { path: '/auth/jwt/login', method: 'post' },
        signOut: { path: '/auth/jwt/logout', method: 'post' },
        signUp: { path: '/auth/jwt/register', method: 'post' },
        getSession: { path: '/users/whoami', method: 'get' }
      },
      token: {
        signInResponseTokenPointer: '/access_token',
        type: 'Bearer',
        maxAgeInSeconds: 60 * 60 * 24, // 24 hours
        cookie: {
          name: 'auth_token',
          options: {
            path: '/',
            secure: process.env.NODE_ENV === 'production',
            sameSite: 'lax'
          }
        }
      },
      sessionDataType: { id: 'integer', name: 'string', email: 'string', is_superuser: 'boolean',
        organizations: '{ name: string, description: string | null, id: string, role: string }[]'
      },
    },
    session: {
      enableRefreshOnWindowFocus: true,
      enableRefreshPeriodically: false
    },
    globalAppMiddleware: {
      isEnabled: true
    },
    rewriteRedirects: true,
    fullPathRedirect: true
  },

  runtimeConfig: {
    public: {
      baseURL: '/api',
      wsURL: '/ws/api',
      googleSignIn: config.google_oauth?.enabled || false,
      deployment: config.deployment?.type || 'development',
      version: version,
      environment: process.env.NODE_ENV,
      app_url: config.base_url || 'http://localhost:3000',
      intercom: config.intercom?.enabled || false
    },
  },

  nitro: {
    experimental: {
      websocket: false
    }
  },

  compatibilityDate: '2024-08-21',
})