<template>
  <el-container class="main-page">
    <!-- 头部区域 -->
    <el-header>Header</el-header>
    <!-- 页面主体区域 -->
    <el-container>
      <!-- 侧边栏 -->
      <el-aside width="200px">Aside</el-aside>
      <!-- 右侧内容区域 -->
      <el-main>Main</el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style lang="less" scoped>
.main-page {
  height: 100%;
}

.el-header {
  background-color: #6495ED;
}

.el-aside {
  background-color: #87CEEB;
}

.el-main {
  background-color: #F0F8FF;
}
</style>
