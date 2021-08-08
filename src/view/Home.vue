<template>
  <el-container class="main-page">
    <!-- 头部区域 -->
    <el-header>
      <div>
        <img src="@/assets/images/header.png" alt="" />
        <span>测试小助手</span>
      </div>
    </el-header>
    <!-- 页面主体区域 -->
    <el-container>
      <!-- 侧边栏 -->
      <el-aside width="200px">
        <el-menu background-color="#B0E0E6" text-color="#fff"
          active-text-color="#ffd04b">
          <!-- 一级菜单 -->
          <el-submenu index="1">
            <!-- 一级菜单模板区域 -->
            <template #title>
              <!-- 图标 -->
              <i color="#AFEEEE" class="el-icon-box"></i>
              <!-- 文本 -->
              <span>功能菜单</span>
            </template>
            <!-- 二级菜单 -->
            <el-menu-item index="1-1">
              <template #title>
                <!-- 图标 -->
                <i class="el-icon-search"></i>
                <!-- 文本 -->
                <span>日志查询</span>
              </template>
            </el-menu-item>
            <el-submenu index="1-2">
              <template #title>预留</template>
              <el-menu-item index="1-2-1">预留</el-menu-item>
            </el-submenu>
          </el-submenu>
        </el-menu>
      </el-aside>
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
  background-color: #ADD8E6	;
  padding-left: 0;
  font-size: 22px;
  color: #fff;
  > div {
    display: flex;
    align-items: center;
    span {
      margin-left: 15px;
    }
  }
}

.el-aside {
  background-color: #B0E0E6;
}

.el-main {
  background-color: #F0FFFF;
}
</style>
