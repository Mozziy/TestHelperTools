<template>
  <div id="lq">
    <el-input
      placeholder="请输入键值后点击查询"
      prefix-icon="el-icon-search"
      v-model="keyword"
      class="input-with-select"
      clearable
    >
      <template #prepend>
        <el-select v-model="envValue" placeholder="环境选择"
        default-first-option filterable>
          <el-option v-for="item in EnvList"
          :key="item.value"
          :label="item.label"
          :value="item.label">
          </el-option>
        </el-select>
        <el-select v-model="sysValue" placeholder="系统选择" clearable
        filterable style="width: 130px;" default-first-option>
          <el-option v-for="item in SysList"
          :key="item.value"
          :label="item.label"
          :value="item.label">
          </el-option>
        </el-select>
      </template>
      <template #append>
        <el-button type="primary" icon="el-icon-search" @click="clicktrigger">搜索</el-button>
      </template>
    </el-input>
    <span>{{ getValue }}</span>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import { requestDemoPost } from '@/api/requests.js'

export default defineComponent({
  setup () {
    // 定义基础数据
    const logdata = ref('')
    const getValue = ref('')
    const sysValue = ref('')
    const keyword = ref('')
    const envValue = ref('')
    const data = ref('')
    // 系统列表
    const SysList = [{
      value: '系统1',
      label: 'a'
    }, {
      value: '系统2',
      label: 'b'
    }, {
      value: '系统3',
      label: 'c'
    }, {
      value: '系统4',
      label: 'd'
    }, {
      value: '系统5',
      label: '(๑•̀ㅂ•́)و✧'
    }]
    // 环境列表
    const EnvList = [{
      value: '环境1',
      label: 'st'
    }, {
      value: '环境2',
      label: 'uat'
    }, {
      value: '环境3',
      label: 'pre'
    }]
    // 点击触发事件
    function clicktrigger () {
    // 获取后端数据
      requestDemoPost(data).then(res => {
        if (res.data.code === 200) {
          logdata.value = res.data.result
          getValue.value = logdata.value
        }
      })
      data.value = {
        envValue: envValue.value,
        keyword: keyword.value,
        sysValue: sysValue.value
      }
      logdata.value = ''
    }
    return {
      keyword,
      envValue,
      sysValue,
      logdata,
      SysList,
      EnvList,
      getValue,
      clicktrigger,
      data
    }
  }
})
</script>

<style>
.el-select .el-input {
  width: 130px;
}

.input-with-select .el-input-group__prepend {
  background-color: #fff;
  padding-left: 0;
  padding-right: 2;

}
.el-input-group__prepend {
  margin-inline-start: 15px;
}
</style>
