module.exports = {
    devServer: {
      proxy: {
        '/api': {
          target: 'http://192.168.8.111:9000/',
          ws: true,
          changeOrigin: true,
          pathRewrite: {
              'api': ''
          }
        }
      }
    }
}
