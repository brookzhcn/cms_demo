import axios from 'axios'

const service = axios.create({
  baseURL: 'http://127.0.0.1:8006/api/v2/',
  timeout: 5000 // 请求超时时间
})

export default service

