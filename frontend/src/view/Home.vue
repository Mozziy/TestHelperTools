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
      <el-aside :width="isCollapse ? '64px' : '150px'">
        <div class="toggle-button" @click="toggleCollapse">|||</div>
        <el-menu background-color="#B0E0E6" text-color="#696969"
          active-text-color="#ffd04b" :unique-opened="true"
          :collapse="isCollapse" :collapse-transition="false"
          :default-active="activePath" router>
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
            <el-menu-item index="/lq" @click="saveNavState('/lq')">
              <template #title>
                <!-- 图标 -->
                <i class="el-icon-search"></i>
                <!-- 文本 -->
                <span>日志查询</span>
              </template>
            </el-menu-item>
            <el-submenu index="/other">
              <template #title>
                <i class="el-icon-dessert"></i>
                <span>其他功能</span>
              </template>
              <!-- 第三级菜单 -->
              <!-- <el-menu-item index="1-2-1">预留</el-menu-item> -->
            </el-submenu>
          </el-submenu>
        </el-menu>
      </el-aside>
      <!-- 右侧内容区域 -->
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import { ref } from 'vue'
export default {
  name: 'Home',
  setup () {
    const isCollapse = ref(false)
    const activePath = ref('')
    // 点击按钮，实现菜单的折叠和展开
    function toggleCollapse () {
      isCollapse.value = !isCollapse.value
    }
    // 保存链接的激活状态
    function saveNavState (activePath) {
      window.sessionStorage.setItem('activePath', activePath)
    }
    // 改变数据
    function changeData () {
      activePath.value = window.sessionStorage.getItem('activePath')
    }

    return {
      isCollapse,
      activePath,
      toggleCollapse,
      saveNavState,
      changeData
    }
  }
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
  color: #696969;
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
  .el-menu {
    border-right: none;  // 解决右边菜单对不齐的情况
  }
}

.toggle-button {
  background-color: #AFEEEE;
  font-size: 10px;
  line-height: 24px;
  color: #fff;
  text-align: center;
  letter-spacing: 0.3em;
  cursor: pointer;
}
</style>
