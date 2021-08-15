// 需要在这里引入 axios
import requests from 'axios'
requests.defaults.baseURL = '/api'

/**
 *  post请求
 * @param data
 */
export const requestDemoPost = (data) => {
  return requests({
    // url地址（地址可以使用拼接的方法，让我们只需要写后部分，前部分连接地址我们可以固定）
    url: '/',
    // 请求方法
    method: 'post',
    // 数据类型（post请求使用的是data，get请求使用的是params）
    data: data
  })
}

/**
 *  get请求
 */
export const requestDemoGet = (params) => {
  return requests({
    url: '/',
    method: 'get',
    params: params
  })
}
