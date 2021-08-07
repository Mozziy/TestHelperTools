<template>
  <h1>开始</h1>
  <h1>{{name}}</h1>
</template>

<script>
export default {
  name: 'App',
  setup () {
    const name = '张三'

    return { name }
  }
}
</script>
